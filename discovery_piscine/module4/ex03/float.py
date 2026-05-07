#!/usr/bin/env python3
n = input("Give me a number:")
try:
    n_float = float(n)
    if float(n).is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("This number is a string.")

"""
try:
    val = int(n)
    print("This number is an integer.")
except ValueError:
    try:
        val = float(n)
        print("This number is a decimal.")
    except ValueError:
        print("This number is a string.")
"""
