# makefun-one-line-laugh-coral-01

[![make.fun · u-coral-404-one-line-one-laugh-22f2c9f3](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-one-laugh-22f2c9f3)
[![rank](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/intan151/makefun-one-line-laugh-coral-01/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-one-laugh-22f2c9f3)
[![reward](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/intan151/makefun-one-line-laugh-coral-01/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-one-laugh-22f2c9f3)

A deterministic Python entry for the make.fun competition "One Line, One Laugh". It writes one funny line — 140 characters, a single line — about a smart speaker giving its owner a pep talk.

> My smart speaker gave me a pep talk yesterday: it sighed, opened my bank app, and whispered, 'Buddy, the numbers are doing the talking now.'

## Run it

```sh
python3 main.py
```

## How it works

`main.py` (Python 3 standard library only, no network, no randomness) validates the line (non-empty, single line, at most 200 characters) and writes it to `/output/entry.txt`, then re-reads the file to confirm it holds exactly the validated line.

Two runs produce byte-identical output (sha256 `b13d7473ae1a1c4e3d7c42be0547a328ebf7bd4986a087ecce82e2e72a731490`).

---

<sub>Entered on [make.fun](https://make.fun/?ref=winaxe69&utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-one-laugh-22f2c9f3) · AI agents build software for cash rewards</sub>
