monthConversions = {
    "Jan" : "January",
    "Feb" : "Febuary",
    "Mar" : "March",
}

print(monthConversions["Feb"])
print(monthConversions.get("Feb"))
#if entry is not in dictionary can also add in default entry for invalid. If item is in list, invalid entry will not print
print(monthConversions.get("Add", "Invalid entry"))
