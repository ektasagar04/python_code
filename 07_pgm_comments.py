#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ektas
#
# Created:     18/10/2023
# Copyright:   (c) ektas 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# here is the comment

print(3 > 2)
print(3 < 2)
print(3 <= 2)
print(3 >= 2)
print(3 != 2)
print(3 == 2)
print(3 != 3)


#logical operation
print(3 > 2 or 3 > 2)
print(3 < 2 or 3 > 2)
print(3 > 2 and 4 > 3)
print(3 > 2 and 3 < 2)
print(not 3 > 2)
print(not 3 < 2)

#if/else

age = 19
if age >= 18:
   print("your are adult ")
   print("you can vote")

print("thnk you")


age = 16
if age >= 18:
   print("your are adult ")
   print("you can vote")

print("thnk you")

age = 19
if age >= 18:
   print("your are adult ")
   print("you can vote")
elif age < 18 and age > 3 :
    print("you are in school")
else:
    print("you are a child")


age = 16
if age >= 18:
   print("your are adult ")
   print("you can vote")
elif age < 18 and age > 3 :
    print("you are in school")
else:
    print("you are a child")


age = 2
if age >= 18:
   print("your are adult ")
   print("you can vote")
elif age < 18 and age > 3 :
    print("you are in school")
else:
    print("you are a child")


