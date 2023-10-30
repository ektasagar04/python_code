#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ektas
#
# Created:     18/10/2023
# Copyright:   (c) ektas 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#list data type

marks = [95 , 90 , 80]
print(marks)
print(marks[0])
print(marks[1])
print(marks[-1])
print(marks[0:2])
print(marks[1:3])


marks = [95 , 90 , 80]
for score in marks :
    print(score)

#operation in list

marks = [95 , 90 , 80]

marks.append(99)

print(marks)


marks = [95 , 90 , 80]

marks.insert(0, 99)

print(marks)


marks.insert(0, 99)

print(99 in marks)

marks.insert(0, 99)

print(93 in marks)

# to know number of elements

marks = [95 , 90 , 80]

print(len (marks))


i = 0
while i < len(marks):
    print(marks[i])
    i = 1 + i

marks.clear()
print(marks)

# break and contiue

students = ("ram" , "ritu" , "mohan" , "radha" , "mona")

for students in students :
    if students == "mohan":
        break;
    print(students)


students = ("ram" , "ritu" , "mohan" , "radha" , "mona")

for students in students :
    if students == "mohan":
        continue;
    print(students)


marks = (95, 99, 85, 85, 85, 85)

print(marks.count(85))

print(marks.index(95))

#sets

marks = {95, 98, 97, 97, 97}

print(marks)

for score in marks :
    print(score)