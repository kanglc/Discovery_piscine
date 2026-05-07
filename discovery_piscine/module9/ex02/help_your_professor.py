#!/usr/bin/env python3

def average(classlist):
    average = 0.0
    for name, grade in classlist.items():
        average = average + grade
    return average/len(classlist)


class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")

