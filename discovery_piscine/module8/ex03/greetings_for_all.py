#!/usr/bin/env python3
def greetings(arg=None):
    if arg is None:
        print("Hello, noble stranger.")
    elif not isinstance(arg, str):
        print("Error! It was not a name.")
    else:
        print("Hello,", arg)

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
