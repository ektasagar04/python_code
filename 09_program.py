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


#tuple

marks = (95, 99, 85, 85, 85, 85)
print(marks)

print(marks.count(85))

print(marks.index(95))

#sets

marks = {95, 99 ,85, 85, 85, 85}
print(marks)

for score in marks:
    print(score)

#dictionary

marks = {"english": 95, "chemistry": 98,}

print(marks)

print(marks["chemistry"])

marks["physics"] = 97
print(marks)

marks["physics"] = 99
print(marks)


#function

import math
print(dir(math))


from math import *
print(sqrt(16))


from math import sqrt
print(sqrt(16))


def print_sum(first, second):
    print(first + second)

print_sum(1, 2)
