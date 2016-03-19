#!/usr/bin/env python

import glob
import sgf
import StringIO


for filename in glob.glob("examples/*.sgf"):
    with open(filename) as f:
        sgf.parse(f.read())


example = "(;FF[4]GM[1]SZ[19];B[aa];W[bb];B[cc];W[dd];B[ad];W[bd])"
collection = sgf.parse(example)

for game in collection:
    for node in game:
        pass

out = StringIO.StringIO()
collection[0].nodes[1].output(out)
assert out.getvalue() == ";B[aa]"
out.close()

out = StringIO.StringIO()
collection.output(out)
assert out.getvalue() == example
out.close()

example2 = "(;FF[4]GM[1]SZ[19];B[aa];W[bb](;B[cc];W[dd];B[ad];W[bd])" \
    "(;B[hh];W[hg]))"

collection = sgf.parse(example2)
out = StringIO.StringIO()
collection.output(out)
assert out.getvalue() == example2
out.close()

example3 = "(;C[foo\\]\\\\])"
collection = sgf.parse(example3)
assert collection[0].nodes[0].properties["C"] == ["foo]\\"]
out = StringIO.StringIO()
collection.output(out)
assert out.getvalue() == example3
out.close()


sgf.parse("foo(;)")  # junk before first ( is supported

sgf.parse("(  ;)")  # whitespace after ( is allowed

sgf.parse("(;;)")  # a node after an empty node is allowed
sgf.parse("(;(;))")  # a gametree after an empty node is allowed


# errors

try:
    sgf.parse("()")
    assert False  # pragma: no cover
except sgf.ParseException:
    pass

try:
    sgf.parse("(W[tt])")
    assert False  # pragma: no cover
except sgf.ParseException:
    pass

try:
    sgf.parse("(;)W[tt]")
    assert False  # pragma: no cover
except sgf.ParseException:
    pass

try:
    sgf.parse("(;1)")
    assert False  # pragma: no cover
except sgf.ParseException:
    pass
