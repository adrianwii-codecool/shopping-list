def assign_more_doubled_values(c, d):
    # c = 5
    # d = 6
    return c*2, d*2


def assign_more_values(c, d):
    # c = 5
    # d = 6
    return c*2, d*2


a,b = assign_more_doubled_values(5, 10)

input = assign_more_doubled_values(5, 10)
# return tuple
print(input)
print(input[0])
print(input[1])

print(a + b)

first, second = assign_more_values("test", 6)
print(first, second)

# tuple (1, 2, 3)
# list [1,2,3]
# dictionary {"key":"value", "key1":"value1"}