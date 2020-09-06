my_list = ["orange", "milk", "potato"]
# [0,1,2]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])

print(my_list[1:3])
print(my_list)

list_length = len(my_list)
print(list_length)

# [0,1,2,3,4,5,6]
indexes = range(list_length)
print(indexes)


my_list.sort()
for i in indexes:
    print(i+1, my_list[i])
