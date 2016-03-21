#!/usr/bin/env python

import glob
import sgf

try:
    from StringIO import StringIO  # pragma: no cover
except ImportError:  # pragma: no cover
    from io import StringIO  # pragma: no cover


for filename in glob.glob("examples/*.sgf"):
    with open(filename) as f:
        sgf.parse(f.read())


example = "(;FF[4]GM[1]SZ[19];B[aa];W[bb];B[cc];W[dd];B[ad];W[bd])"
collection = sgf.parse(example)

for game in collection:
    for node in game:
        pass

out = StringIO()
collection[0].nodes[1].output(out)
assert out.getvalue() == ";B[aa]"
out.close()

out = StringIO()
collection.output(out)
assert out.getvalue() == example
out.close()

example2 = "(;FF[4]GM[1]SZ[19];B[aa];W[bb](;B[cc];W[dd];B[ad];W[bd])" \
    "(;B[hh];W[hg]))"

collection = sgf.parse(example2)
out = StringIO()
collection.output(out)
assert out.getvalue() == example2
out.close()

example3 = "(;C[foo\\]\\\\])"
collection = sgf.parse(example3)
assert collection[0].nodes[0].properties["C"] == ["foo]\\"]
out = StringIO()
collection.output(out)
assert out.getvalue() == example3
out.close()


sgf.parse("foo(;)")  # junk before first ( is supported

sgf.parse("(  ;)")  # whitespace after ( is allowed

sgf.parse("(;;)")  # a node after an empty node is allowed
sgf.parse("(;(;))")  # a gametree after an empty node is allowed


# errors

try:
    sgf.parse("()")  # games must have a node
    assert False  # pragma: no cover
except sgf.ParseException:
    pass

try:
    sgf.parse("(W[tt])")  # a property has to be in a node
    assert False  # pragma: no cover
except sgf.ParseException:
    pass

try:
    sgf.parse("(;)W[tt]")  # a property has to be in a game
    assert False  # pragma: no cover
except sgf.ParseException:
    pass

try:
    sgf.parse("(;1)")  # property names can't start with numbers
    assert False  # pragma: no cover
except sgf.ParseException:
    pass

try:
    sgf.parse("(;A5[])")  # property names can't have numbers at all
    assert False  # pragma: no cover
except sgf.ParseException:
    pass

try:
    sgf.parse("(;FOO[bar]5)")  # bad character after a property value
    assert False  # pragma: no cover
except sgf.ParseException:
    pass

try:
    sgf.parse("(;")  # finished mid-gametree
    assert False  # pragma: no cover
except sgf.ParseException:
    pass


# new features for 0.5

with open("examples/ff4_ex.sgf") as f:
    ff4_ex = sgf.parse(f.read())

assert len(ff4_ex) == 2

game1 = ff4_ex[0]

assert game1.root.properties["SZ"] == ["19"]

count = 0
for node in game1.rest:
    count += 1
assert count == 13

collection = sgf.parse(example2)
count = 0
for node in collection[0].rest:
    count += 1
assert count == 6

# test game.rest if only one node

assert sgf.parse("(;)")[0].rest is None
