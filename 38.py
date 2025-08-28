user_input = input("Enter list elements separated by spaces: ")


my_list = [int(x) for x in user_input.split()]

element_to_count = int(input("Enter the element to count: "))


count = my_list.count(element_to_count)

print(f"The element {element_to_count} appears {count} times in the list.")

