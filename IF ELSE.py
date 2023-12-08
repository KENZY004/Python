#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kenzn
#
# Created:     14-09-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
str1=str(input("M or F: "))
age=int(input("b: "))
if((str1=="M")& (age>=65)):
    print("eligible for concession")
elif((str1=="F") &(age>=60)):
    print("eligible for concession")
else:
    print("not eligible for concession")

