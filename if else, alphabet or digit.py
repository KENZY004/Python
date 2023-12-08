#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kenzn
#
# Created:     21-09-2023
# Copyright:   (c) kenzn 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
ch=input("ch: ")
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print("alphabet")
elif(ch>='0' and ch<='9'):
    print("digit")
else:
    print("neither alphabet nor digit")