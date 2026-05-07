#!/usr/bin/env python3
import sys
if (len(sys.argv) == 2) and (sys.argv[1].count("z") > 0):
    for i in range(1, sys.argv[1].count("z")+1):
        print("z", end="")
    print()
else:
    print("none")
