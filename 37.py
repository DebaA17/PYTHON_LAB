user_input = input("Enter list elements separated by space: ")
original_list = user_input.split()

cloned_list1 = original_list[:]
cloned_list2 = list(original_list)
cloned_list3 = original_list.copy()

print("Original list:", original_list)
print("Cloned list using slicing:", cloned_list1)
print("Cloned list using list():", cloned_list2)
print("Cloned list using copy():", cloned_list3)
