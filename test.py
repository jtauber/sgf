#!/usr/bin/env python

import glob
import sgf


for filename in glob.glob("examples/*.sgf"):
    parser = sgf.Parser()
    collection = sgf.Collection(parser)

    with open(filename) as f:
        parser.parse(f.read())
