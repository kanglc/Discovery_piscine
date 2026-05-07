#!/usr/bin/env python3
def add_one(arg=None):
    return int(arg)+1

x = 42
print(f"x = {x}")

x_add_one = add_one(x)
print(f"x add one = {x_add_one}")

print(f"x = {x}")
