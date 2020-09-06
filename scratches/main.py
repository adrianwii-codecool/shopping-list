# first line of comment
# second line of comment

'''
    Our comment 
    first line of comment
    second line of comment
'''

name = "Adrian"
lastname = "Wii"
print(name + " " + lastname)

example = "test"

quantity = 5
price = 12
print("SUM: ", quantity*price, "PLN")
print("SUM:  " + str(quantity*price) + " PLN")

a = 5
b = 6

print(a+b)
print("a + b =", a+b)

# int - integer - liczby
# str - string - tekst
# int() -> formatuje string do liczby: int("5") => 5
# str() -> formatuje int do stringa: str(5) => "5"


print(type(name))

# input - pobranie wartości od użytkownika

product = input("Provide product name: ")
print(product)


quantity = int(input("Provide quantity: "))
# print(quantity*2)
# print(quantity*3)

if quantity > 6:
    print("Don't buy so many things!")

'''
    CONDITIONS:
    >
    <
    ==
    and, or
'''

variable = "test"
variable = "whatever"

print(variable)

print(variable == "test") #False
variable == "test"  # True, False
print(variable == "whatever") #True


# len() - zwraca ilość znaków w stringu

if len(product) == 4:
    print("Your product consist with 4 letters")
    print("test")
    print(product)

# LOOPS - while, for

choice = input("Wanna add sth to your list? Y or N: ")
while choice == "Y":
    product = input("Provide product to add ")
    print(product)
    choice = input("Wanna add sth more? Y or N")

print("End of while loop")

'''
    Adrian -> 6 znaków
    name = "Adrian"
    len(name) -> 6
    index in len(name)
    0, 1, 2, 3, 4, 5
    range(5) -> [0,1,2,3,4]
    range(7) -> [0,1,2,3,4,5,6]

'''

def print_letter_index():
    for index in range(len(name)):
        print(index, name[index])



print_letter_index()
print_letter_index()

def print_letter_index_in(text):
    for index in range(len(text)):
        print("%2d %s" % (index, text[index]))


print_letter_index_in("CODECOOL")

my_text = input("Provide text message: ")
print_letter_index_in(my_text)