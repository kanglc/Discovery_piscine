#!/usr/bin/env python3

def find_the_redheads(names):
    array_of_redheads = []
    for firstname, lastname in names.items():
        if lastname == "red":
            array_of_redheads.append(firstname)
    return array_of_redheads

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))

