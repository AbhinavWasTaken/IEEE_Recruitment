# Creating the initial list containing cutoff data
cutoff_list = [
    ("Pilani", "CS", 327),
    ("Pilani", "Chemical", 247),
    ("Pilani", "Msc. Eco", 271),
    ("Pilani", "Msc. Bio", 241),
    ("Goa", "CS", 301),
    ("Goa", "Chemical", 239),
    ("Goa", "Msc.Eco", 263),
    ("Goa", "Msc.Bio", 234),
    ("Hyderabad", "CS", 298),
    ("Hyderabad", "Chemical", 238),
    ("Hyderabad", "Msc.Eco", 261),
    ("Hyderabad", "Msc.Bio", 234)
]

# Creating empty dictionaries to be used later
Pilani = {}
Goa = {}
Hyderabad = {}

# Iteratively updating each campus dictionary with branch and cutoff (as keys and values) for every branch
for a in cutoff_list:
    if a[0] == "Pilani":
        Pilani.update({a[1]:a[2]})
    elif a[0] == "Goa":
        Goa.update({a[1]:a[2]})
    elif a[0] == "Hyderabad":
        Hyderabad.update({a[1]:a[2]})

# Combining each campus dictionary into one unified dictionary
cutoff_dictionary = {
    "Pilani" : Pilani,
    "Goa" : Goa,
    "Hyderabad": Hyderabad
}

# Priting the unified dictionary
print(cutoff_dictionary)
