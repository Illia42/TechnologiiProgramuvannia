my_list = [1, 5, 3]
print("Start:", my_list)

my_list.append(10)
print("append(10):", my_list)

my_list.extend([20, 30])
print("extend([20, 30]):", my_list)

my_list.insert(1, 99)
print("insert(1, 99):", my_list)

my_list.remove(99)
print("remove(99):", my_list)

my_list.sort()
print("sort():", my_list)

my_list.reverse()
print("reverse():", my_list)

copy_list = my_list.copy()
print("copy():", copy_list)

my_list.clear()
print("clear():", my_list)