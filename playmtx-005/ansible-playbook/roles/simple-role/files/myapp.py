#!/usr/bin/env python3

import sys

option=sys.argv[1] if len(sys.argv) > 1 else "???"
print("{} is {}!".format(sys.argv[0],option.upper()))
