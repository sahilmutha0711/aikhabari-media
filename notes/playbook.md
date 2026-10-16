# THE AI KHABARI — Content Playbook (single source of truth)
Read this FIRST before making any Reel, carousel or cover. Where older notes (style.md, the daily message) disagree, THIS FILE WINS. After every round of owner feedback, update this file and the feedback log at the bottom in the same session.

## 00. GROWTH ENGINE (owner, 10-16) — read before choosing or scripting anything
Goal: reach + SHARES (DM sends) first, saves second, likes last. Instagram's ranking for non-followers leans on: watch time / completion and the 3-second hold, sends per reach, saves per reach, then likes/comments. Everything below serves those.

**Baseline (10-16, 17 posts):** reels 90-195 views, avg watch 4-8 s, SKIP RATE 66-90% (most people leave in the first 3 s), 1 share and 0 saves in total. Diagnosis: openings too slow (logo flash + whisper intro before the payoff), Reels too long (55-70 s), nothing "send-worthy". The new 10-15 style already improved skip rate to 66% (best so far).

### A. The first 2 seconds (fixes the skip rate)
- Frame 1 = the payoff promise as BIG on-screen text + a moving visual. No logo, no title card, no "today's AI news". The sound logo plays UNDER the hook; the whisper "Psst... the AI Khabri here" moves to AFTER the first reveal (~4-6 s), or is skipped on short Reels.
- On-screen hook text ≤ 7 words, scroll-stopping, honest: "This AI tool is basically cheating", "Your smart TV could hide an AI", "He built Spotify's recs. Now he's worth billions", "Delete this app before Monday" (only if true). Must be literally true or clearly framed as a take.
- Spoken hook and text hook can differ; text = curiosity, voice = context.
- Pattern interrupt every 2-3 s (cut, zoom, number pop, new box). No static frame longer than 3 s.

### B. Length and loops (fixes watch time)
- Default Reel length 25-40 s (hard max 50 s). One story, one idea. Cut background ruthlessly.
- End on a line that loops back into the first frame (last words lead into the hook sentence) so replays count.
- Put the best reveal at ~70% of the runtime, "wait for it" promised in the hook.

### C. Make it SEND-WORTHY (fixes shares)
Before building any piece, answer in one line: "Who would the viewer send this to, and why?" If there's no clear answer, change the angle or drop the story. Send-worthy angles that work for tech news:
- "My coworker needs this": a tool or trick that saves hours or money (tool swaps, free alternatives, prompt fixes).
- "Whoa" factor: an unbelievable but true number or event (dead man speaks in court, 0.81 s 0-60).
- "Warn someone": something that affects their money, privacy or job (surveillance pricing, scams, kids + AI).
- "Settle an argument": a clear verdict (X vs Y ranked), "you were right about...".
- Identity: "only people in tech will get this", "for every founder who...".
Share trigger names the PERSON TYPE + reason ("send this to the coworker still paying for X"); on-screen near the end AND in the caption's last line. Never generic.

### D. Carousels (built for saves + sends)
- Slide 1 = a bold promise with a number ("7 free AI tools that replace $200/month of apps", "Stop typing these into ChatGPT"). ≤ 8 words, huge type, one visual.
- Slide 2 delivers value immediately (no intro slide).
- One idea per slide, readable in 2 s; a "SCREENSHOT THIS" cheat-sheet slide near the end.
- Last slide: "SAVE THIS for later" + "Follow @theaikhabari for daily AI news you'll actually use" + the send trigger.
- 6-10 slides for value packs (swipes count as engagement); 4-5 for quick news.

### E. Captions, SEO, timing
- Caption line 1 = the hook again (shows above the fold). Then 3-6 short lines of value, then the share trigger, then ONE question that invites an opinion comment.
- Instagram search reads captions and on-screen text: include 2-3 plain keywords people search ("ChatGPT tips", "AI tools", "Tesla Roadster"). 3-5 relevant hashtags max.
- Alt text on carousels (API alt_text) with the keywords.
- Post Reels at 7-9 AM PT or 5-7 PM PT; carousels evenings. Space posts ≥ 3 h apart; never 2 Reels in the same hour.

### F. Legit algorithm levers we automate (API) — NO fake engagement
- Daily metrics loop (step 0 of every run): pull insights for every post from the last 7 days (views, reach, shares, saved, likes, ig_reels_avg_watch_time, reels_skip_rate) via INSTAGRAM_GET_IG_MEDIA_INSIGHTS, append to notes/metrics.md, and write one line "what worked / what didn't" that changes today's choices (hook type, length, topic, voice). Monday: weekly summary to the owner (one short message).
- Comment-keyword DMs: on value posts say "Comment TOOLS and I'll DM you the full list" (only when we actually have the list ready). Reply privately to each commenter (official private-reply/messaging API, inside Instagram's 24 h window; follow the instagram:qualification playbook). Comments + DMs are strong signals and the DM gets forwarded.
- Reply to every comment within the first hours (INSTAGRAM_POST_IG_COMMENT_REPLIES), ending with a question to keep threads going.
- Post our own first comment with the extra fact / source (INSTAGRAM_POST_IG_MEDIA_COMMENTS); ask the owner to pin it in the app.
- Owner-side (suggest, can't automate): share each Reel to Stories with a poll, use "Trial Reels" for risky hooks, invite collab posts with friendly AI pages.
- NEVER: bots, bought likes/followers, follow-unfollow, engagement pods, mass DMs, scraping or auto-commenting on other accounts. These violate Instagram's terms and get accounts throttled or banned.

### G. Quality gate before sending posts to the owner
Every piece must pass: (1) hook text stops the scroll in frame 1, (2) one clear "send to ___ because ___", (3) a smart line / takeaway, (4) ≤ 40 s for Reels unless the story truly needs more, (5) facts verified with 2 sources, theories labelled. If any fails, fix it or drop the piece. Quality over quantity: 2 great posts beat 4 average ones.

## 0. NORTH STAR (owner, 10-15): make the viewer feel smarter than everyone around them
Every Reel and post must leave the viewer holding something most people DON'T know yet, so they feel ahead and want to show it off ("wait, you didn't know this?"). Shares come from that feeling, not from asking.
- **Insider-knowledge framing.** Position every story as early, inside information: "90% of people using ChatGPT don't know...", "Your friends will hear about this next month. You're hearing it now.", "Investors just quietly bet $X on this. Here's why." Make it true (cite the data/source on screen), never fake scarcity.
- **The "smart line".** Every piece ends its body with ONE quotable, repeatable sentence the viewer can say at work or in the group chat (on screen in a box labelled "SAY THIS AT WORK" / "SOUND SMART:"). E.g. "AI agents already spend money on their own; the question is who sets the limit."
- **Voice tone.** Confident, slightly conspiratorial insider, like a friend leaning in with a secret; quick, no hedging filler, but opinions labelled. Use [whispering] for the reveal line and [excited] for the "most people missed this" turn. Talk TO the viewer ("you"), and position them above the crowd ("most people scroll past this; you won't").
- **Script spine (Reels):** hook (knowledge gap: "Most people think X. They're wrong.") → whisper intro → the news in 1 line → the thing nobody's saying (hidden number, second-order effect, who really wins/loses) → why it matters for YOU (money, job, tools) → the catch → "do THIS instead / try THIS" (concrete action or tool swap) → SMART LINE → share trigger.
- **Share triggers (replace "send this to a friend").** Make sharing a status move or a useful favour, specific to the story and named to a person type:
  - test/challenge: "Send this to the friend who thinks they know AI. Bet they didn't know number 3."
  - tag-the-person: "Tag the one person in your team still paying for X."
  - saved-them-money/time: "Someone you know is overpaying for this. Send it."
  - quiz moment on screen: "Pause. Guess the number before I say it." (reveal → people share to test others)
  - "Screenshot this slide" on the most useful carousel slide (cheat-sheet slides, tool-swap tables, prompt boxes).
  Rotate them; never the same line twice in a row. Captions open with the hook, end with the share trigger + one question that invites a hot-take comment.
- **Hypotheses / predictions are allowed (~1 in 4 posts), clearly labelled.** Section titled "MY THEORY" / "HYPOTHESIS" / "PREDICTION" on screen and said aloud ("here's my theory — not confirmed"). Build only on verified facts, give the reasoning in 2-3 steps, name what would prove it wrong. Never state a theory as fact, never invent numbers, quotes or deals.

## 0b. CONTENT MIX from 10-16 (owner)
Daily, across the 2-4 pieces, keep a balance of:
1. **Top companies** (OpenAI, Google, Anthropic, Meta, Apple, Microsoft, Nvidia, Amazon) — still covered, major launches always.
2. **Startup money** — at least ONE piece per day on startup funding / investments / acquisitions from the last 24-48 h (sources: TechCrunch funding, Crunchbase News, The Information, Axios Pro Rata, company blogs, SEC/press releases; verify amount, round, lead investor with 2 sources). Always answer "why should YOU care": what the startup does, which tool you can use today, what this money signals (where jobs/opportunities are moving), and who it threatens. Formats: "$X just went into Y. Here's what they know that you don't", "3 startups that raised this week that you can use for free today", investor "follow the money" breakdowns.
3. **New tech / new tools** — fresh launches people can try today, with a **"Stop using X, use Y instead" tool-swap** angle: compare the new tool to the one people already use (price, what it does better, what it does worse, who should switch). Honest: say where the old tool still wins. No paid tool pushes without the Paid Partnership label; no affiliate claims.
4. Prompt carousels on alternate days (unchanged).
Rule of thumb per day: 1 big-company story + 1 startup-money story + 1 tool-swap/prompt piece (+ optional 4th of any type).
Carousel formats that drive saves AND shares: tool-swap tables ("Paying for X? Use Y"), "Startups that raised this week + what they do in 1 line", "Before vs after" prompt swaps, "Explain this news to your boss in 3 lines" cheat sheets. Put a "SCREENSHOT THIS" tag on the cheat-sheet slide.

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
- Order: hook text + visual in frame 1 with the sound logo UNDER it (no separate logo beat) → knowledge-gap hook → first reveal → whisper (after the first reveal, ~4-6 s, or skip on short Reels) "[whispering] Psst... the AI Khabri here." → the news in one line → the thing nobody's saying → why it matters for YOU → the catch → do THIS instead / try THIS → SMART LINE (on-screen box) → specific share trigger (see §0, never generic "send this to a friend").
- **Chaos Meter only in ~1 of 3 Reels** ("Today's AI chaos level? Stick around." gauge stops on "?", number revealed before the CTA). Not every Reel.
- Length 25-40 s, hard max 50 s (10-16: 55-70 s Reels had 4-8 s average watch). Fast pace, cut filler.
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
- Cut-outs: tools/reel/cutout.py (u2net; copy to /home/claude/tools/ if missing). Model at /home/claude/models/u2net.onnx.
- Repo hygiene: after every post of the day is live, delete that day's media and squash history (see daily message).

## 8. Feedback log (newest first) — add a line every time the owner reacts
- 10-16: Owner-recorded Reels: owner on camera only for the hook (2-3 s) and short 2-3 s pops at twists / "most people get this wrong" / takeaway / share line; news graphics in between. Remove pauses, ums, repeated takes and fumbled lines (keep the best take); clean the voice. Pipeline: tools/examples/selfie/ (whisper base.en on the Composio sandbox for word times, cut.py energy-snapped edits, 1080p60 proxy + select-filter cut, transparent PNG overlay composite).
- 10-16: Growth engine (§00): optimise for shares/saves and watch time; catchy scroll-stopping text hooks in frame 1; carousels = bold promise slide 1 + "save this / follow" last slide; daily metrics loop; legit API levers only. Baseline skip rate 66-90%, avg watch 4-8 s → Reels now 25-40 s.
- 10-15 eve: New north star: viewers should crave feeling smarter than others and share to show it (§0). From 10-16: daily startup-funding piece + "use this instead of that" tool swaps alongside top-company news; engineered share triggers, not "share with friends"; labelled hypotheses allowed, never untrue.
- 10-15: Paper & Cobalt prompt carousel = "no colours, bland" → vivid cobalt + lime with chat-window UI. Green-mesh agents Reel + robot cover rejected (bad gradients, weak fonts, cover not clickable) → rebuilt in approved sun/sea/neon style with Brian Armstrong photo. Voice (Laura) liked. Name said "khoo-bri" → must be "kh-bbb-ri"; spell "Khabri".
- 10-14: Hooks should make people wait for the ending (rankings, bold takes, "playing dumb or real?"); sometimes go wild. Prompt carousels on alternate days; variable slide counts; contrast-tested single-accent palettes; purple/yellow OK sometimes.
- 10-14: Dialogue Reels with a second character (Bunty) ~2/week.
- 10-14: ElevenLabs voices Roger/Laura/Harry/Matilda; one take only; full name "AI Khabari" said "KHUB-ree"; Chaos Meter only ~1 in 3; no more test spending without asking.
- 10-14: Carousel gradients (blue+orange, then loud cyan) rejected — "eyes go to the background, not the text". Calm, text-first won (approved to post, "still not that good"): keep improving within that direction; ask for reference screenshots.
- 10-14: OpenAI v2 Reel (vivid moving gradients, coral/orange duotone cover) = "perfect".
- 10-13: Motion-first v2 Reel style approved; keyword must be fully visible above the head; covers designed separately; hooks start from what people know.
- 10-12/13: Don't repeat cover people/photos; no emoji in art; news only; 45-60 s Reels; don't overwhelm the owner.
