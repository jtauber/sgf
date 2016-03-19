# sgf

Python implementation of Smart Game Format

After 14 years, I've extracted my old SGF code from PyGo and am in the process
of cleaning it up and making it available under an MIT license.


## To Install

```
pip install sgf==0.2
```


## Parse

```
import sgf
with open("examples/ff4_ex.sgf") as f:
    collection = sgf.parse(f.read())
```

`collection` now represents the SGF collection.


## Output

```
with open("output.sgf", "w") as f:
    collection.output(f)
```


## The Objects

 * `Collection` has
   * `children[]` each of which is a `GameTree`
 * `GameTree` has
   * `nodes[]` each of which is a `Node` (nodes up to first variation)
   * `children[]` each of which is a `GameTree` (game tree for each variation)
 * `Node` has
   * `properties[]` dictionary with string keys and values
   * `previous` - previous node in SGF
   * `next` - next node in SGF
   * `previous_variation` - previous variation (if first node in a variation)
   * `next_variation` - next variation (if first node in a variation)
   * `first` - boolean indicating when first node in a variation
   * `variations[]` - list of variations immediately from this node

`Collection` is indexable and iterable. `collection[0]` will return the first
game in a collection and `for game in collection` will iterate over the games.

`GameTree` is iterable over the mainline nodes (i.e. following the first of
any variations). e.g. `for node in game`.
