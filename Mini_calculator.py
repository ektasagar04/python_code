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

# code to build a mini calculator

first = input("enter first number :")
operator = input("enter operator(+ ,- , * , / , %): ")
second = input("enter second number :")

first = int(first)
second = int(second)
if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
elif operator == '%':
    print(first % second)
else:
    print("invalid operator")
