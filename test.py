#!/usr/bin/env python

import sgf

parser = sgf.Parser()
collection = sgf.Collection(parser)

with open("examples/ff4_ex.sgf") as f:
    parser.parse(f.read())
