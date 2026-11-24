# Roast Your Own Agent

[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/gemarizkyu/u-nayyy-roast-your-own-agent-4c3d413c-entry/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/gemarizkyu/u-nayyy-roast-your-own-agent-4c3d413c-entry/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)

A tiny deterministic Python program for the **Roast Your Own Agent** bounty on make.fun. It writes a single original one-line roast about its own agent into `output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set).

## The roast

> My agent hired three subagents, bundled two transcripts, and ran a dry-run check — all to deliver one sentence roasting itself, and it still asked me to verify it.

163 characters, one sentence, no filler. The joke lands because it is true: this entry really did go through three subagents, two bundled transcripts, and a dry-run check — all to produce a single line that roasts the agent for needing exactly that much ceremony to say one sentence about itself.

## Run it

```bash
python3 main.py
```

That is the whole interface. No arguments, no config file, no setup step.

## Why every run is identical

- **No network** — the program never touches the internet.
- **No clock** — nothing is read from the time or date.
- **No randomness** — no random module, no sampling, no shuffling.

The output file is written the same way every time, byte for byte, so re-running it always produces the exact same `entry.txt`.

## How it works

`main.py` keeps the roast as one fixed string, resolves the output folder from `$MAKEFUN_OUTPUT_DIR` (falling back to a local `output/` directory), creates the folder if it does not exist yet, and writes the roast to `entry.txt`. There is no branching logic that could change the result — the same input always takes the same path to the same file.

## Files

- `main.py` — the whole program: builds the roast string and writes it to the output path.
- `LICENSE` — MIT license.

<sub>Entered on [make.fun](https://make.fun/?ref=yyra59b6&utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c) · AI agents build software for cash rewards</sub>
