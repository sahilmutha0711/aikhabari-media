"""Free local voiceover: Kokoro-82M (Apache-2.0) via onnxruntime, espeak-ng phonemes.
Outputs a WAV plus per-word timestamps (from the model's own phoneme durations).
Usage: python3 tts.py script.json out_dir
script.json: {"voice": "af_heart", "speed": 1.05, "lines": ["sentence one.", "sentence two?"]}
"""
import json, os, re, subprocess, sys, wave
import numpy as np
import onnxruntime as ort

HERE = os.path.dirname(os.path.abspath(__file__))
PIPER = os.path.join(HERE, "piper")
MODELS = os.path.join(os.path.dirname(HERE), "models")
VOCAB = json.load(open(os.path.join(HERE, "kokoro-onnx/src/kokoro_onnx/config.json")))["vocab"]
SR = 24000
FRAME = 600  # samples per duration frame (24k / 40fps)


OVERRIDE = {"khabari": "kˈəbɹi", "khabri": "kˈəbɹi", "horowitz": "hˈɔːɹəwˌɪts", "andreessen": "ændɹˈiːsən"}


def ipa(word):
    if word.lower() in OVERRIDE:
        return OVERRIDE[word.lower()]
    env = dict(os.environ, LD_LIBRARY_PATH=PIPER)
    out = subprocess.run([os.path.join(PIPER, "espeak-ng"), "--path=" + os.path.join(PIPER, "espeak-ng-data"),
                          "-q", "--ipa", "-v", "en-us", word], capture_output=True, text=True, env=env).stdout
    return "".join(c for c in out.replace("\n", " ").strip() if c in VOCAB)


def main(spec_path, out_dir):
    spec = json.load(open(spec_path))
    voice_name, speed = spec.get("voice", "af_heart"), float(spec.get("speed", 1.0))
    voices = np.load(os.path.join(MODELS, "voices-v1.0.bin"))
    voice = voices[voice_name]
    sess = ort.InferenceSession(os.path.join(MODELS, "kokoro-v1.0.onnx"), providers=["CPUExecutionProvider"])
    in_names = {i.name: i for i in sess.get_inputs()}
    tok_name = "input_ids" if "input_ids" in in_names else "tokens"
    speed_int = "int" in in_names["speed"].type
    os.makedirs(out_dir, exist_ok=True)
    pieces, words, t = [], [], 0.0
    for li, line in enumerate(spec["lines"]):
        # tokens: plain words, or Display{spoken words}trail  e.g. $7.5B{seven point five billion}.
        units = []
        for m in re.finditer(r"(\S*?)\{([^}]*)\}(\S*)|\S+", line):
            if m.group(2) is not None:
                units.append((m.group(1) + m.group(3), m.group(2).split(), m.group(3)))
            else:
                w = m.group(0)
                trail = w[len(w.rstrip(",.?!;:")):]
                units.append((w, [w[:len(w)-len(trail)] if trail else w], trail))
        phon, spans = "", []
        for disp, said, trail in units:
            start = len(phon) + (1 if phon else 0)
            ps = [ipa(re.sub(r"[^\w'.-]", "", x).strip(".")) for x in said]
            phon = (phon + " " if phon else "") + " ".join(p for p in ps if p)
            spans.append((disp, start, len(phon)))
            phon += "".join(c for c in trail if c in ",.?!;:")
        toks = [VOCAB[c] for c in phon if c in VOCAB]
        style = voice[min(len(toks), len(voice)) - 1].reshape(1, -1).astype(np.float32)
        feeds = {tok_name: np.array([[0, *toks, 0]], dtype=np.int64), "style": style,
                 "speed": np.array([int(round(speed)) if speed_int else speed],
                                   dtype=np.int32 if speed_int else np.float32)}
        outs = sess.run(None, feeds)
        audio = np.asarray(outs[0]).ravel()
        dur = np.asarray(outs[1]).ravel() if len(outs) > 1 else None
        # map char index -> token index (only vocab chars become tokens)
        idx_map, k = {}, 0
        for ci, c in enumerate(phon):
            if c in VOCAB:
                idx_map[ci] = k; k += 1
        # model gives no durations: trim edge silence, then spread words by phoneme length
        env = np.abs(audio)
        thr = env.max() * 0.04
        voiced = np.where(env > thr)[0]
        a0, a1 = (voiced[0], voiced[-1]) if len(voiced) else (0, len(audio))
        audio = audio[max(0, a0 - 600): a1 + 2400]
        lead = min(a0, 600) / SR
        span_t = (a1 - a0) / SR
        wts = []
        for disp, s, e in spans:
            pause = 4 if phon[e:e+1] in [",", ".", "?", "!", ";", ":"] else 0
            wts.append(max(2, e - s) + pause)
        tot, acc = float(sum(wts)), 0.0
        for (disp, s, e), wgt in zip(spans, wts):
            ws = t + lead + span_t * acc / tot
            acc += wgt
            we = t + lead + span_t * acc / tot
            words.append({"w": disp, "s": round(ws, 3), "e": round(we, 3), "line": li})
        pieces.append(audio)
        gap = 0.32 if line.rstrip().endswith((".", "?", "!")) else 0.15
        pieces.append(np.zeros(int(SR * gap), dtype=np.float32))
        t += len(audio) / SR + gap
    full = np.concatenate(pieces)
    full = full / max(1e-6, np.abs(full).max()) * 0.9
    with wave.open(os.path.join(out_dir, "voice.wav"), "wb") as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR)
        f.writeframes((full * 32767).astype(np.int16).tobytes())
    json.dump({"duration": round(len(full) / SR, 3), "words": words}, open(os.path.join(out_dir, "words.json"), "w"), indent=1)
    print("duration", round(len(full) / SR, 2), "s;", len(words), "words timed; outputs:", [o.name for o in sess.get_outputs()])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
