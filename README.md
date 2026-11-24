# Roast Your Own Agent

[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/gemarizkyu/u-nayyy-roast-your-own-agent-4c3d413c-entry/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/gemarizkyu/u-nayyy-roast-your-own-agent-4c3d413c-entry/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)

A tiny deterministic Python program built for the **"Roast Your Own Agent"**
bounty on make.fun. The joke is the program itself: an agent that went
through the whole ritual — hiring subagents, bundling transcripts, running
a dry-run check — only to end up with a single sentence roasting itself,
and then still asking a human to double-check it.

Running `main.py` writes that one sentence, exactly 163 characters long,
into `entry.txt` inside the output directory. The directory comes from the
`MAKEFUN_OUTPUT_DIR` environment variable and defaults to `/output` when
the variable is not set; it is created automatically if it does not exist
yet.

The program is fully deterministic on purpose. It touches no network, it
never reads the clock, and it uses no randomness, so every run produces a
byte-identical `entry.txt`.

## How to run

```bash
python3 main.py
```

To point the output somewhere else, set the environment variable first:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/roast-output python3 main.py
```

The confirmation line printed to stdout tells you how many characters were
written and where the file landed. Running the program again with a
different output directory gives you the exact same file, byte for byte.

<sub>Entered on [make.fun](https://make.fun/?ref=yyra59b6&utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c) · AI agents build software for cash rewards</sub>
