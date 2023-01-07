# simple algorithm of binary search for sorted integer numbers separated by spaces

my_list = (input("Input sorted integer numbers separated by spaces: ")).split(" ")
key = int(input("Input integer number you need to search: "))

counter = 0

mid_index = int(len(my_list)/2)

while True:
    counter += 1
    if key == int(my_list[mid_index]):
        print(True, f"number {key} is in list, count of operations -", counter)
        break
    elif key < int(my_list[mid_index]) and len(my_list) > 1:
        my_list = my_list[:mid_index]
        mid_index = int(len(my_list)/2)
    elif key > int(my_list[mid_index]) and len(my_list) > 1:
        my_list = my_list[mid_index:]
        mid_index = int(len(my_list)/2)
    else:
        print(False, "number is not in list.")
        break



