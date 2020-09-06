
shopping_list = []

'''
    This function will display product from our shopping list
'''
def print_list():
    # print(shopping_list)
    print()
    print("SHOPPING LIST:")
    # print(shopping_list)
    # [0,1,2,3,4] range(5)
    # ["A", "B", "C"]

    # Print each product name in new line
    # for product in shopping_list:
    #     print(product)

    # Print each product name in new line with
    for i in range(len(shopping_list)):
        print("%2d %s" % (i+1, shopping_list[i]))


def add_product(product):
    shopping_list.append(product)
    print(product.upper(), "ADDED TO SHOPPING LIST!\n")


def remove_product():
    print_list()
    to_remove = input("Provide product name to remove: ")

    if to_remove in shopping_list:
        shopping_list.remove(to_remove)
    else:
        print("Ups, that list not contain selected product!")


def menu():
    print("MENU")
    print("1. ADD PRODUCT")
    print("2. SHOW PRODUCT LIST")
    print("3. REMOVE PRODUCT")
    print("0. EXIT")

    # choice = input("Please provide action to do: ")
    # while not is_number(choice):
    #     choice = input("Please provide action to do: ")

    # choice = int(choice)

    choice = input("Please provide action to do: ")
    while not choice in ["0", "1", "2", "3"]:
        choice = input("Please provide action to do: ")

    choice = int(choice)

    if choice == 1:
        # add product
        option = input("Do you want to add product? Y or N")

        while option.upper() == 'Y':
            product = input("Please, provide product to add: ")
            add_product(product)
            option = input("Do you want to add another product? Y or N")

    elif choice == 2:
        print_list()
        print()
    elif choice == 3:
        remove_product()
    else:
        exit()


def is_number(string):
    # https://www.w3schools.com/python/python_try_except.asp

    try:
        int(string)
        return True
    except:
        return False


def main():
    while True:
        menu()


main()
