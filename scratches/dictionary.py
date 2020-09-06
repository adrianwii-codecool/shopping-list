menu = {
    "0": "EXIT",
    "1": "ADD PRODUCT",
    "2": "SHOW PRODUCT LIST",
    "3": "REMOVE PRODUCT"
}

template = "{}. {}"

def print_dictionary(dictionary):
    for key in dictionary.keys():
        print(template.format(key, menu[key]))


# {} - wszędzie tam, gdzie napotkamy taki symbol złożony 
# z dwóch nawiasów, podstaw wartość, która podana jest w argumencie funkcji format
print_dictionary(menu)

# print(menu.keys())

print("6" in menu.keys())