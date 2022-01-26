# STUDENT NAME: SHRUTI PAGHADAL
# STUDENT ID: 20CE065
# AIM: Find Captain's Room Number

print("\n------------------------------------PRACTICAL 3------------------------------------------------------------\n")
# The first line consists of an integer, K , the size of each group.
k = int(input("Enter the size of each group:\n")) 
# The second line contains the unordered elements of the room number list.
print("\nThe list of room number is:")
rooms = (int(x) for x in input().split(' '))
dictionary = {}

for i in rooms:
    if not i in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1

for key, val in dictionary.items():
    if val != k:
        print("\nCaptain's room number is:",key)
print("\n------------------------------------------END OF PRACTICAL 3--------------------------------------------------------\n")