# # This is a test file
#
# n = int(input("Enter the element : "))
#
# arr =[]
#
# print("Enter the elements : ")
# for i in range(n):
#     arr.append(int(input()))
#
# total = sum(arr)
#
# print(f"Array : {arr}")
# print(f"The sum of array : {total}")

info = {
    "key": "value",
    "name": "Anonymous",
    "age": 69,
    "mark": 69,
    "college": "BPPIMT",
    "classmates": ["alice", "bob"]

}

student = {
    "name": "Debasis",
    "subjects": {
        "math":95,
        "science":90,
        "english":69,
    },

    "session": "2025-2026",
}
student.update({"city" : "Bengaluru"})

print(student['subjects'] ["english"])
print(student["city"])



print(info)
print(type(info))
print(info["age"])