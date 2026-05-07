#!/usr/bin/env python3

def array_of_names(names):
    array_of_names = []
    for firstname, lastname in names.items():
        fullname = firstname.capitalize() + " " + lastname.capitalize()
        array_of_names.append(fullname)
    return array_of_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))

