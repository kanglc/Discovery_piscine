#!/usr/bin/env python3
import sys
def downcase_it(string):
    return string.lower()

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        print(downcase_it(sys.argv[i]))
else:
    print("none")
