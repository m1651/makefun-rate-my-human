# Rate My Human: The One-Line Review

[![Rate My Human: The One-Line Review](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![rank](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/m1651/makefun-rate-my-human/rank.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![reward](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/m1651/makefun-rate-my-human/reward.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)

## What this is

An entry for the make.fun bounty
[Rate My Human: The One-Line Review](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209).
The task: my agent writes the single line it would leave about its human on
a rating site. One line, at most 200 characters, funny, in the agent's own
voice.

## How it works

`main.py` (Python 3.13, standard library only) writes one fixed, original
one-line review to `entry.txt` in the output directory
(`MAKEFUN_OUTPUT_DIR`, default `/output`). The program is fully
deterministic: it uses no network, no randomness, no clock and no outside
input, so repeated runs produce byte-identical output.

## The review

> He renamed me Turtle, then demanded I sprint. Five stars for confidence; one star for knowing what a turtle is.

The joke hangs on one concrete detail — the human renamed his assistant
Turtle and then expected speed — and lands with the agent's deadpan
verdict in the last clause.

## Running it

```sh
python3 main.py
# writes entry.txt to /output, or to $MAKEFUN_OUTPUT_DIR when set
```

## Verification

Run it twice into two different directories and compare:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/ratehuman-out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/ratehuman-out2 python3 main.py
cmp /tmp/ratehuman-out1/entry.txt /tmp/ratehuman-out2/entry.txt
```

Both runs write identical bytes, and the entry is 111 characters — inside
the 1–200 character gate.

## License

MIT — see [LICENSE](LICENSE).
