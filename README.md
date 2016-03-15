# sgf

Python implementation of Smart Game Format

After 14 years, I've extracted my old SGF code from PyGo and am in the process
of cleaning it up and making it available under an MIT license.


## Parse

```
import sgf
parser = sgf.Parser()
collection = sgf.Collection(parser)
with open("examples/ff4_ex.sgf") as f:
    parser.parse(f.read())
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
   * `nodes[]` each of which is a `Node`
   * `children[]` each of which is a `GameTree`
 * `Node` has
   * `properties[]` dictionary with string keys and values
   * `previous` - previous node in SGF
   * `next` - next node in SGF
   * `previous_variation` - previous variation (if first node in a variation)
   * `next_variation` - next variation (if first node in a variation)
   * `first` - boolean indicating when first node in a variation
   * `variations[]` - list of variations immediately from this node
