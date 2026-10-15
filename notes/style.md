# AI Khabari visual style (v2, approved by owner 2026-10-13)

Owner direction: "not simple pics behind text but proper unique video clips, relatable enough, and new color codes and formats every time."

## Rules
1. **Motion first.** Every Reel scene shows something *moving* that is relevant to what is said. A still photo with text over it is a last resort, not the default.
2. **New palette + font pair every post.** Never use the same palette as the previous grid post. Log the palette used in `notes/covers.md` (add a "palette" note to the row).
3. **Mix light and dark scenes** inside one Reel (e.g. cream host + takeaway scenes) so it never sits on one gradient.
4. **Honesty.** Recreated product UIs (chat windows, terminals, app screens) carry a small "ILLUSTRATION" label. Never pass a mock-up off as a real screenshot. No movie/TV/other creators' footage. Official press-kit b-roll is fine when the company offers it for media use (credit it).
5. **Covers:** person cut out (u2net) over a bold palette background, big word fully visible (never hidden behind a head), headline in display font + italic serif line, all key text inside the centre 3:4 grid crop (y 240-1680). Template: `tools/reel/cover_v2.html`.

## Motion library (pick what fits the story)
- **3D cut-out:** u2net cut-out of the person (`/home/claude/models/u2net.onnx`), slow perspective sway, blurred dark copy of the photo behind, giant keyword ABOVE the head.
- **Product UI recreation:** chat app / terminal / phone screen / browser window with typing, streaming replies, diff lines, notifications popping in (label ILLUSTRATION).
- **Explainer diagrams:** animated dots/particles, flows, before-vs-after states that switch on the spoken word.
- **Data:** racing bars, counters that land on the spoken number, line charts drawing in, stock tickers.
- **Kinetic type:** slam-in headlines, strike-through on a word, italic serif reveal, stamp chips.
- **Alerts/catch:** warning lines typed like code errors, pulsing red vignette.
- **Checklists:** boxes ticking on the exact word.
- **Camera:** punch-zoom + micro-shake on big beats, swipe+blur scene transitions, film grain, progress bar.

## CAROUSELS vs REELS (owner, 2026-10-14 latest — overrides below)
- **Carousels: calm, text-first.** Owner rejected loud gradients on carousels ("eyes go to the background, not the text"). Use a near-black base (#0F1214) with only a FAINT glow (accent at ~8-10% opacity), cards #171B1E with a thin #262C30 border, off-white text #F2F2EF, grey secondary #9AA3A6, ONE soft accent colour (e.g. mint #5DD6B0) used only on key words/numbers, and 1-2 soft warm-white slides (#F6F4EF→#ECE8DF, dark text, deep accent) for big moments/takeaways/CTA. Template: tools/examples/gemini-car/build.py. Rotate the single accent colour per post (mint, soft coral #E58C7A, sky #7DB7E8, sand #D9B48F) — never loud.
- **Reels: vivid moving gradients are OK** (owner called the OpenAI v2 Reel "perfect"): tools/examples/spy/tpl.html.

## Colour & backgrounds (owner, 2026-10-14 — REELS)
- **Catchy, saturated, MOVING gradients.** Plain flat backgrounds (cream paper, flat black) were rejected as "very plain". Every scene/slide sits on a vivid mesh gradient (2-3 big radial colour blobs that drift slowly in Reels) or a bold single-hue duotone photo.
- **BANNED:** yellow / amber / gold and purple / violet / indigo / magenta as main colours (old look). Watch out: coral + blue overlapping makes purple, so never blend those two in one duotone.
- **Approved mesh sets** (use the MESH() + DUO() helpers in tools/examples/spy/tpl.html):
  - `sun`: base #FF4D2E, blobs #FF2E63, #FF9500, #FF6F91 (white text, white caption highlight)
  - `sea`: base #0047E0, blobs #00D4FF, #0020A0, #00F0C0 (white text; mint #00F0C0 accent)
  - `neon`: base #07080C with cyan rgba(0,229,255,.38), coral rgba(255,61,110,.38), blue rgba(0,87,255,.35) blobs
  - `alert`: base #D10028, blobs #FF3D6E, #FF6A00, #8A0018 (catch / warning scenes)
  - light scene: linear-gradient(160deg,#F2FEFF,#B8F1FF,#9FE6FF) with ink text (use sparingly for takeaways)
- **Duotone photos:** grayscale photo + a single-hue gradient with mix-blend-mode:color — coral to orange (#FF3D6E to #FF8A00) or blue to cyan (#0047E0 to #00B8FF).
- **Accents:** cyan #00E5FF, mint #00F0C0, hot coral #FF3D6E, white. Caption highlight = white box with black text (black box on light scenes).
- **Owner feedback 10-14:** blue + orange together in one carousel looked bad. Keep each post to ONE colour family (e.g. deep teal glowing into electric cyan, with bright cyan slides + black text for big moments — tools/examples/gemini-car/build.py). Don't mix warm (coral/orange) and cool (blue/cyan) families in the same carousel.
- **Rotate per post:** don't open two posts in a row with the same mesh; alternate sun/sea/neon hooks. Carousels: cycle sea mesh slides, 1-2 sun slides for big moments, 1 light slide for takeaways (tools/examples/gemini-car/build.py).

## Font pairs (display / italic serif / mono) — files in /mnt/skills/examples/canvas-design/canvas-fonts/
- Boldonse / InstrumentSerif-Italic / JetBrainsMono (used 10-13)
- BigShoulders-Bold / Gloock / IBMPlexMono (used 10-14 reel)
- BricolageGrotesque-Bold / YoungSerif / DMMono
- Tektur-Medium / CrimsonPro-Italic / GeistMono
- Outfit-Bold / Lora-Italic / RedHatMono (used 10-14 carousel)
- EricaOne / InstrumentSerif-Italic / JetBrainsMono

## Engine
`tools/reel/v2.html.tpl` + `tools/reel/v2_build.py` (`TPL=<template> python3 v2_build.py <reeldir> [t1 t2…]`). The template's `S[i]` functions are per-story scenes keyed to script lines; copy the template per Reel, set the palette CSS variables and @font-face fonts, and write new scenes for the story. Preload every image in the hidden div (otherwise frames render before images load). Render in the background with nohup (~10 min for 65 s).

Carousels: copy car.css per post and swap its colours (#0B1030, #101745, #FFB400, #7C6CFF, #FF6B5A) and fonts to the post's palette + font pair.

## Owner-approved reference (2026-10-13): notes/ref/approved_hook_and_cover.png
- Left = Reel hook frame: giant keyword fully visible ABOVE the head, person cut-out in the middle, display headline + italic serif line below the mic/chin, stamp chip ("3X FASTER") under it, all elements on screen within the first ~2 s.
- Right = cover: person cut-out on a solid bold palette colour, giant keyword above the head, short headline + italic serif line, small brand tag. Use this composition as the default for hooks and covers.

## Voices (owner, 2026-10-14 — overrides the "Kokoro for now" line in the daily message)
ElevenLabs FREE plan (10,000 credits/month; a 1-min Reel ≈ 1,000 credits; non-commercial; add "Voice: ElevenLabs" to the caption). ONE Reel per day max on ElevenLabs, always generations_count=1 (never 4), model eleven_v4. Any other Reel that day uses Kokoro af_heart.
Owner-picked premade voices — rotate, never the same voice on two ElevenLabs Reels in a row:
- Laura `FGY2WhTYpPnrIDTdsKH5`: female, quirky/upbeat — USE FIRST (owner: "tomorrow 1 Reel with girl voice")
- Matilda `XrExE9yKIg1WjnnlVkGX`: female, professional (policy, explainers, money)
- Roger `CwhRBWXzGAHq8TQ4Fs17`: male, laid-back (tech, business, launches)
- Harry `SOYHLrjzK2X1ezoPC6cr`: male, fierce (drama, crime, AI gone wrong)
Log the voice used for every Reel in covers.md ("voice: X"); on Mondays compare reach/plays/saves by voice and report one line to the owner.

## Pronunciation (owner)
Superseded — see notes/playbook.md §4: say "kh-bbb-ri", spell "the AI Khabri" in ElevenLabs scripts (NOT "Khubree", which came out "khoo-bri"). Always the FULL name.

## Signature opening (owner-approved 2026-10-14)
1. 0-0.5 s: sound logo — owl eyes flash open + short "hoo-hoot" + whoosh (synthesise locally with numpy/ffmpeg, no credits), layered UNDER the hook; never delays the first word.
2. The news hook line (famous name/product first).
3. Whisper beat right after the hook: "[whispering] Psst... the AI Khabri here." (ElevenLabs v4 [whispering] tag; on Kokoro: "Psst... I'm the AI Khabari."). Owl leans in on screen.
4. CHAOS METER only in about 1 of every 3 Reels (owner: "not every reel, don't want it boring"): "Today's AI chaos level? Stick around." + gauge whose needle spins and stops on "?", number revealed (e.g. 8/10) just before the CTA. Log in covers.md which Reels had it.

## ElevenLabs timing method
No word timings come back: generate the whole script in ONE call, find phrase boundaries with `ffmpeg -af silencedetect=noise=-35dB:d=0.18`, map script lines to phrases, spread words inside a phrase proportionally by character length (captions show 3-word groups, accurate enough). Download the mp3 from the run's media url in the Composio remote sandbox and commit it to the repo to get it here.

## Dialogue Reels — "Ask the AI Khabari" (owner idea, 2026-10-14)
About 2 Reels a week (stories with a "how does this affect me / how do I use this" angle) are a CONVERSATION, not a monologue:
- Cast: the AI Khabari owl (answers; voice = the day's ElevenLabs voice) + an original curious character "Bunty" who asks the viewer's question (voice = a free Kokoro voice of the opposite gender, e.g. am_puck / am_michael if Khabari is female, af_heart if Khabari is male). Only the owl's lines use ElevenLabs credits.
- Script shape (≤60 s): hook → Bunty: "Wait, what does that mean for me?" → Khabari explains in 2-3 short turns → Bunty pushes back with a real worry ("isn't that risky?") → Khabari gives the catch + takeaway → Bunty reacts in one funny line → CTA.
- Animation: split stage, owl on one side and Bunty on the other; whoever speaks is lit, slightly scaled up, and lip-flaps to the audio level (beak / mouth open-close from the voice envelope). Owl gestures by swapping poses on key words (point.png, think.png, celebrate.png, closeup.png in /home/claude/kit/owl) with wing bounce; Bunty is an original flat SVG character (no resemblance to any existing character) with jointed arms that gesture as he asks (palms up on questions, head-scratch on confusion, hands on head on shock), blinking eyes and head tilt. Speech bubbles carry the key phrase; normal word captions stay at the bottom.
- Same news rules: real facts, sources in caption, product UIs labelled ILLUSTRATION.

## Carousel plan (owner, 2026-10-14 — latest; overrides earlier carousel colour bans)
- **Alternate days = PROMPT CAROUSEL** instead of a news carousel: practical prompt packs people can copy to be more productive. Formats to rotate:
  - "Stop saying THIS to Claude/ChatGPT. Say THIS instead." (bad prompt vs better prompt, with why)
  - Role packs: "Architects / teachers / marketers / founders / students / doctors / Amazon sellers: try these 3 prompts"
  - "1 prompt for each workday task" (email, meeting notes, planning, research, decision)
  - Tie it to that week's news when possible (e.g. a new model or feature → "5 prompts to try on it today").
  Every prompt goes in a copyable mono box; test that each prompt actually makes sense; no fake claims about results. Last slide = save/send CTA ("Save this for your next workday").
- **Variable length:** 4-5 slides for a quick pack, 6-8 for a full story. Never pad.
- **Colour: strong, clean contrast like a top Instagram brand.** One calm base + ONE accent per post; never two clashing hues (the blue+orange gradient carousel was rejected). Purple or yellow accents are fine SOMETIMES (not every post, never two posts in a row). Rotate these tested palettes (WCAG contrast: text ≥16:1, accent ≥5.5:1):
  | name | bg | text | accent |
  |---|---|---|---|
  | Ink & Mint | #0F1214 | #F2F2EF | #5DD6B0 |
  | Ink & Coral | #121010 | #F4EFEA | #FF7A66 |
  | Ink & Sky | #0E1116 | #EEF2F6 | #7DB7E8 |
  | Ink & Lime | #0D0F0A | #F1F3EA | #C8F25A |
  | Ink & Lilac | #100E14 | #F1EEF6 | #B9A6FF |
  | Ink & Saffron | #110F0B | #F5F1E8 | #FFC24B |
  | Paper & Ink-Green (light) | #F4F1EA | #141414 | #0F6E55 |
  | Paper & Tomato (light) | #F6F2EC | #151311 | #C2361F |
  | Paper & Cobalt (light) | #F2F0EB | #101418 | #2448D8 |
  Alternate dark and light posts on the grid. Backgrounds stay quiet (flat or a faint 8-10% glow); colour lives in the accent words, numbers, cards and the cover.

## Hook playbook — watch-time first (owner, 2026-10-14)
The first line must make people NEED the ending. Pick the hook type that fits the story (rotate, don't repeat the same type twice in a row):
1. **Ranking + wait-for-#1:** "I ranked this week's 5 biggest AI launches. Number one isn't even from OpenAI. Wait for it." (Use for weekly roundups, tool lists, model comparisons; reveal #1 last.)
2. **Bold contrarian take:** "Google's new AI is better than ChatGPT. Let me explain why." / "Free AI is a trap. Here's why." (Must be a defensible opinion backed by the facts in the Reel.)
3. **Playing dumb or real?:** "OpenAI is either playing dumb, or this is real. I think..." (two readings of the news, give our take at the end.)
4. **Personal stakes:** "If you use ChatGPT for work, stop scrolling. This changes what you can type."
5. **Shock number + mystery:** "$20 million. That's what Disney paid for a dead chatbot. The reason is wild."
6. **Secret / insider:** "Nobody's talking about the scariest part of this launch."
Rules: hook in the first 1.5 s, before the whisper intro; open a loop and close it in the last 10 s (the #1, the answer, "our take"); the take must be honest and grounded in verified facts. Label opinion as opinion ("I think", "our take"), never invent claims, never misrepresent the story to get the click. Mirror the hook on the cover text and in the caption's first line. Carousels: slide 1 uses the same hook types ("I ranked..." / "Stop doing X") and the last content slide pays it off.
