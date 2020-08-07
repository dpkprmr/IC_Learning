
import os
file = open("D:\FileHandling\FileRead.txt","r")
Filesize = os.path.getsize("D:\FileHandling\FileRead.txt")
if Filesize==0:
 print("File is empty")
else:
    print("File has data")
print(file.read())

import os

a=2
try:
 os.path.exists("D:\FileHandling\FileRead.txt")
 print(a/0)
 # os.remove("\FileRead.txt")
except:
    print("File Do not here")
    print("Divide by zero not allowed")
else:
    print("File is here")
finally:
    print("i will execute no matter what")


try:
     file= open("D:\FileHandling\FileRead.txt","r")
     file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
# except AssertionError as error:
#     print(2>5)
else:
    print("File is Present")


thirdset = {"Akash", "Priyanka", "Aishwarya", "False"}
print(sorted(thirdset,reverse = True))