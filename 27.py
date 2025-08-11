lst = input("Enter list elements (space-separated): ").split()
i, j = map(int, input("Enter two indices to swap: ").split())
lst[i], lst[j] = lst[j], lst[i]
print(lst)
