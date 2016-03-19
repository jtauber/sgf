#!/usr/bin/env python

import glob
import sgf


for filename in glob.glob("examples/*.sgf"):
    with open(filename) as f:
        sgf.parse(f.read())
