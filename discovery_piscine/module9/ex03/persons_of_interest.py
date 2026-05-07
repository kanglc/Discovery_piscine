#!/usr/bin/env python3

def famous_births(namelist):
    extracted = {}
    for name, details in namelist.items():
        x1 = None
        x2 = None
        for key, value in details.items():
            if key == "name":
                x1 = value
            elif key == "date_of_birth":
                x2 = value
        if x1 is not None and x2 is not None:
            extracted[x1] = x2

    # Sort by the second element of the tuple (the year of birth, which is at index 1)
    sorted_dict = dict(sorted(extracted.items(), key=lambda item: item[1]))

    # print out the sorted list
    for name, year in sorted_dict.items():
        print(f"{name} is a great scientist born in {year}")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)
