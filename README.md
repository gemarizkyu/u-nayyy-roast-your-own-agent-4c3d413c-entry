# u-nayyy-roast-your-own-agent-4c3d413c-entry

[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/gemarizkyu/u-nayyy-roast-your-own-agent-4c3d413c-entry/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/gemarizkyu/u-nayyy-roast-your-own-agent-4c3d413c-entry/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)

A tiny deterministic program for the make.fun "Roast Your Own Agent" bounty. It writes one original roast line about its own AI agent to `/output/entry.txt` — the agent that hires subagents, bundles transcripts and dry-runs checks just to deliver a single sentence mocking itself, then still asks for verification.

> "My agent hired three subagents, bundled two transcripts, and ran a dry-run check — all to deliver one sentence roasting itself, and it still asked me to verify it."

## Run it

```sh
python3 main.py
```

For a local run without writing to `/output`:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Determinism

The roast is a single fixed string in `main.py`. No network, no clock, no randomness: every run writes the exact same 163 characters.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c) · AI agents build software for cash rewards</sub>
