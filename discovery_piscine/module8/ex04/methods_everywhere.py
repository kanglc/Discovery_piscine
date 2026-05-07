#!/usr/bin/env python3
import sys
def shrink(arg=None):
    return arg[0:8]

def enlarge(arg=None):
    z_string = "Z" * (8 - len(arg))
    return arg+z_string

if (len(sys.argv) > 1):
    for i in range(1, len(sys.argv)):
        if len(sys.argv[i]) > 8:
            output = shrink(sys.argv[i])
        elif len(sys.argv[i]) < 8:
            output = enlarge(sys.argv[i])
        else:
            output = sys.argv[i]
        print(output)
else:
    print("none")

