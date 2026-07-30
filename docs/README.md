# DOWNSHAFT — DOCS

Play it on a phone: <https://junovhs.github.io/grapeghost/> · source: [`../index.html`](../index.html)

Three things live here. Everything else lives in Ishoo.

| | |
|---|---|
| **[design.md](design.md)** | The one design document: what the game is, the verb, the tone, what is in the build, what is decided, what is open. Start here. |
| **[north-star.png](north-star.png)** | The art and tone reference of record (DEC-15). A backyard at the top, a UFO at the bottom. |
| **[philosophy.md](philosophy.md)** | The designer's own game preferences. Not about DOWNSHAFT; outlives it. |

Decisions and issues are **not** in markdown — they are in Ishoo, which is the source of
truth. Ask an agent for `ishoo status`, or:

```
ishoo decision list            # the ADRs — DEC-07 and DEC-09..DEC-16 are live
ishoo plan show downshaft      # the open questions
ishoo status                   # what to do next
```

The pre-DOWNSHAFT material — *The Little Digger* design docs and five retired prototypes — is
in git, not in the tree:

```sh
git show archive/little-digger:docs/brief.md
git show archive/little-digger:old/deep.html
git show iteration/3d-diorama:index.html > /tmp/meadow.html   # the 3-D meadow build
```
