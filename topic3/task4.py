def find_insert_position(lst, target):
    for index, item in enumerate(lst):
        if item >= target:
            return index
    return len(lst)

arr = [5, 15, 25, 35, 45]
number = 20

index_to_insert = find_insert_position(arr, number)

print("Original array:", arr)
print("Insert index:", index_to_insert)

arr.insert(index_to_insert, number)
print("Result array:", arr)