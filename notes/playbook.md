# THE AI KHABARI — Content Playbook (single source of truth)
Read this FIRST before making any Reel, carousel or cover. Where older notes (style.md, the daily message) disagree, THIS FILE WINS. After every round of owner feedback, update this file and the feedback log at the bottom in the same session.

## 1. Owner communication
- Don't overwhelm. Research and decide silently. Send only finished posts: preview, caption, suggested time, then "Reply 'post' to publish all, or 'post 1,3' / tell me what to change."
- Never publish without the owner's "post". Instagram's API can't delete posts; if a redo is needed, the owner deletes the old one in the app.

## 2. What we post
- AI + startup NEWS from the last 24 h (launch radar on official pages; major launches must be covered), plus "WHAT YOU CAN TAKE FROM THIS" in every post.
- Daily: up to 2 Reels + 2 carousels, different stories. Quality over quantity.
- **Alternate days: one carousel is a PROMPT carousel** (copy-paste prompts for productivity): "Stop saying THIS to ChatGPT/Claude, say THIS", role packs ("Architects / teachers / marketers / founders / students / Amazon sellers: try these"), "1 prompt per workday task", or prompts for that week's new model/feature.
- ~2 Reels a week are **"Ask the AI Khabari" dialogue Reels**: the owl (answers, ElevenLabs voice) + an original curious character "Bunty" (asks the viewer's question, free Kokoro voice of the opposite gender). Lit speaker scales up and lip-flaps to the audio; owl swaps poses (point/think/celebrate/closeup in /home/claude/kit/owl); Bunty is an original flat SVG character with jointed arms (palms up on questions, head-scratch, hands-on-head shock), blinking, head tilt. Shape: hook → Bunty "what does that mean for me?" → 2-3 Khabari turns → Bunty's real worry → catch + takeaway → Bunty's funny reaction → CTA.

## 3. Hooks (most important for watch time)
- Hook lands in the first 1.5 s and makes people NEED the ending. Rotate types, never the same twice in a row:
  ranking with #1 revealed last ("I ranked... wait for number one") · bold take ("X is better than Y, let me explain why") · "playing dumb or is it real? I think..." · personal stakes ("If you use ChatGPT at work, stop scrolling") · shock number + mystery · insider secret ("Nobody's talking about the scariest part").
- **Sometimes go wild** (owner: "sometimes go wild in initial hooks too"): about 1 in 3 Reels gets an unexpected, funny or provocative opener — a cheeky comparison, a dramatic cold open, a playful roast of a company, a ridiculous-but-true framing ("Google just paid $20 million for a dead chatbot's homework"). Still factual; still opinion labelled as opinion.
- Start from what people already know (famous name / product first). Open a loop, close it in the last 10 s. Mirror the hook on the cover and in the caption's first line.
- Honesty guardrail: bold, never false. Label opinions ("I think", "our take"); never invent claims or misrepresent the story.

## 4. Reel structure, voice, pronunciation
- Order: sound logo (0-0.5 s owl-eye flash + "hoo-hoot" + whoosh, synthesised locally, under the hook) → hook → whisper "[whispering] Psst... the AI Khabri here." → who/what → what happened → why it matters (comparison) → the catch → what you can take from this → CTA question + "send this to a friend who...".
- **Chaos Meter only in ~1 of 3 Reels** ("Today's AI chaos level? Stick around." gauge stops on "?", number revealed before the CTA). Not every Reel.
- Length 45-60 s, hard max 70 s. Calm pace, cut filler not context.
- Name: always the FULL "the AI Khabari". Pronunciation (owner, 10-15): "kh-bbb-ri" — a near-silent vowel after KH, straight into a hard "bri" (like Hindi "khabri"). NOT "kha-baaa-ree" (10-14) and NOT "khoo-bree" (the "Khubree" spelling made ElevenLabs say "oo" — retired). In ElevenLabs scripts spell it "the AI Khabri"; if a voice still stretches it, try "the AI Kh'bri". Kokoro IPA override: kˈəbɹi (tools/reel/tts.py).
- Voices: ElevenLabs free plan, ONE Reel/day max, generations_count=1, eleven_v4; rotate Laura (FGY2WhTYpPnrIDTdsKH5, female quirky — use first), Matilda (XrExE9yKIg1WjnnlVkGX, female pro), Roger (CwhRBWXzGAHq8TQ4Fs17, male laid-back), Harry (SOYHLrjzK2X1ezoPC6cr, male fierce); never the same voice twice in a row; caption credit "Voice: ElevenLabs". Other Reels: Kokoro. Log voice per Reel in covers.md; Mondays compare performance by voice (one-line report).
- ElevenLabs timings: one call per script; phrase boundaries via ffmpeg silencedetect; spread words in a phrase by character length.

## 5. Reel visuals
- MOTION FIRST: every scene moves and matches the words — 3D cut-out person (u2net) with the big keyword FULLY visible above the head, recreated product UIs (chat, terminal, app) labelled ILLUSTRATION, animated diagrams, racing bars/counters landing on the spoken number, kinetic type, alerts typed like code errors, ticking checklists, punch-zoom on big beats, swipe+blur transitions, grain. Still photo + text is a last resort.
- NEVER build a Reel on one green/mono gradient family (10-15 green "cash" Reel rejected: "templates very bad, green gradients look bad, fonts not emphasised"). Use the approved engine look: BigShoulders UPPERCASE display at 150-330px, Gloock serif lines, key word in a solid colour BOX (white/black/accent), scenes rotating sun/sea/neon/alert, a real photo of the known person/company (duotone bg + cut-out) early in the Reel.
- Reel colour (owner called the OpenAI v2 Reel "perfect"): vivid MOVING mesh gradients per scene (sun / sea / neon / alert sets in tools/examples/spy/tpl.html), single-hue duotone photos (coral→orange OR blue→cyan, never coral+blue together = purple mud), white captions with the current word in a white box. Mix dark and bright scenes.
- Covers must make people CLICK: giant 2-word hook (300px+), a real recognisable face cut-out large (head ~1/4 of frame), a big stamped number/claim box, flying UI stickers (receipts, notifications). A flat illustration/robot cover was rejected 10-15 ("not hook enough").
- Covers: separate designed cover (never the first frame); cut-out person on a bold colour, keyword above the head, short headline + italic serif line, key text inside the centre 3:4 (y 240-1680). Never reuse a cover photo; no same person on a cover within 12 posts (check covers.md).

## 6. Carousel visuals
- 10-15 UPDATE: "calm" went too far — paper/near-black carousels read as "bland, no colours". Now: a VIVID saturated background (e.g. electric cobalt #2340F5) with ONE punchy accent (lime #D4FF3F), white text, and RELATABLE UI on every slide: recreated chat windows (dark chat app, user bubble, input bar, typing dots, labelled ILLUSTRATION), faint chat-bubble shapes in the background. Final slide flips to the accent colour. Template: tools/examples/agents/prompt_carousel_v2.py. Still one accent only; still high contrast.
- Calm, text-first: quiet background (flat or a faint 8-10% glow) so the eye goes to the text; ONE accent colour per post on key words, numbers, cards and the cover; never two clashing hues (the blue+orange gradient carousel was rejected; loud cyan gradients were rejected).
- Strong contrast like a top Instagram brand. Rotate tested palettes (text ≥16:1, accent ≥5.5:1), alternate dark and light posts: Ink & Mint #0F1214/#F2F2EF/#5DD6B0 · Ink & Coral #121010/#F4EFEA/#FF7A66 · Ink & Sky #0E1116/#EEF2F6/#7DB7E8 · Ink & Lime #0D0F0A/#F1F3EA/#C8F25A · Ink & Lilac #100E14/#F1EEF6/#B9A6FF · Ink & Saffron #110F0B/#F5F1E8/#FFC24B · Paper & Ink-Green #F4F1EA/#141414/#0F6E55 · Paper & Tomato #F6F2EC/#151311/#C2361F · Paper & Cobalt #F2F0EB/#101418/#2448D8.
- Purple or yellow accents are allowed SOMETIMES, never on two posts in a row, never as the old navy+amber look.
- Length varies: 4-5 slides for quick packs, 6-8 for full stories. Never pad. Second-to-last = takeaways (numbered, prompt in a copyable mono box), last = CTA (save/send + follow).
- Template: tools/examples/gemini-car/build.py (local Playwright, fonts in /mnt/skills/examples/canvas-design/canvas-fonts/). Rotate font pairs: Boldonse/InstrumentSerif/JetBrainsMono · BigShoulders/Gloock/IBMPlexMono · Bricolage/YoungSerif/DMMono · Tektur/CrimsonPro/GeistMono · Outfit/Lora/RedHatMono · EricaOne/InstrumentSerif/JetBrainsMono.

## 7. Production rules
- No emoji in artwork (fonts show boxes); fine in captions. Photos ≥1080 px from Commons/press kits, credited; Wikimedia UA 'AIKhabariBot/1.0 (https://instagram.com/theaikhabari)'. No other creators' footage or movie/TV clips. Verify facts with 2+ sources.
- Repo hygiene: after every post of the day is live, delete that day's media and squash history (see daily message).

## 8. Feedback log (newest first) — add a line every time the owner reacts
- 10-15: Paper & Cobalt prompt carousel = "no colours, bland" → vivid cobalt + lime with chat-window UI. Green-mesh agents Reel + robot cover rejected (bad gradients, weak fonts, cover not clickable) → rebuilt in approved sun/sea/neon style with Brian Armstrong photo. Voice (Laura) liked. Name said "khoo-bri" → must be "kh-bbb-ri"; spell "Khabri".
- 10-14: Hooks should make people wait for the ending (rankings, bold takes, "playing dumb or real?"); sometimes go wild. Prompt carousels on alternate days; variable slide counts; contrast-tested single-accent palettes; purple/yellow OK sometimes.
- 10-14: Dialogue Reels with a second character (Bunty) ~2/week.
- 10-14: ElevenLabs voices Roger/Laura/Harry/Matilda; one take only; full name "AI Khabari" said "KHUB-ree"; Chaos Meter only ~1 in 3; no more test spending without asking.
- 10-14: Carousel gradients (blue+orange, then loud cyan) rejected — "eyes go to the background, not the text". Calm, text-first won (approved to post, "still not that good"): keep improving within that direction; ask for reference screenshots.
- 10-14: OpenAI v2 Reel (vivid moving gradients, coral/orange duotone cover) = "perfect".
- 10-13: Motion-first v2 Reel style approved; keyword must be fully visible above the head; covers designed separately; hooks start from what people know.
- 10-12/13: Don't repeat cover people/photos; no emoji in art; news only; 45-60 s Reels; don't overwhelm the owner.
