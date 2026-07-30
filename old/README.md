# old — retired prototypes

Each of these was the live `index.html` at some point. They are kept to be reopened, not
maintained. Nothing here is on the phone path any more.

| File | What it was testing |
|---|---|
| `caving.html` | Rappelling down a shaft on a rope. |
| `packhouse.html` | Sorting and hauling what you brought back up. |
| `pov.html`, `pov-spike.html` | First-person descent into the abyss. Identical copies. |
| `deep.html` | The long dark below — pressure and light at depth. |

## Shelved iterations kept as git tags, not files

**`iteration/3d-diorama`** — the 3-D voxel/painted meadow build, with the hunt, the graded dig
call, and the report card. Shelved 2026-07-29 per **DEC-08**: it won the Q-07 phone comparator
on looks, but the project has no 3-D asset pipeline and 2-D hand-painting is the only art
capacity there is. The decision was about who makes the assets, not about the look.

It is a tag rather than a file in here because that build embeds ~3.9 MB of texture data and
copying it into the tree would carry that weight forever. To read or run it:

```sh
git show iteration/3d-diorama:index.html > /tmp/meadow.html
```

The 2-D `downshaft.html` that used to live in this directory was promoted back to the root
`index.html` in the same move.
