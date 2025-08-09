# Python program to interchange first and last elements in a list

def swap_first_last(lst):
	if len(lst) < 2:
		return lst
	lst[0], lst[-1] = lst[-1], lst[0]
	return lst


# Take user input for the list
user_input = input("Enter list elements separated by spaces: ")
my_list = user_input.split()
# Convert elements to integers if possible
try:
	my_list = [int(x) for x in my_list]
except ValueError:
	pass  # Keep as strings if not all are integers

print("Original list:", my_list)
swapped_list = swap_first_last(my_list)
print("List after swapping first and last:", swapped_list)
