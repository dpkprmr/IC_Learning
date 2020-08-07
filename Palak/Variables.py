# #Global Keyword
# def myfunc():
#     global x
#     x= "Automation"
# myfunc()
# print("Learning python for" + " " + x)
# # Using Global Keyword to change a global variable inside a function
# x="Hello"
# def myfunc():
#     global x
#     x="Automation"
# myfunc()
# print("Learning python for" + " " + x)
# #Getting Data Types
# x=5
# print(type(x))
#
# x="Hello,World!"
# print(x)
# print(type(x))
#
# x=20.5
# print(x)
# print(type(x))
# x= -87.7e100
# print(x)
# print(type(x))
# #List
# x= ["apple", "banana", "cherry"]
# print(x)
# print(type(x))
# #tuple
# x= ("a","b","c")
# print(x)
# print(type(x))
#
# #Strings As Arrays
# a="Hello,World"
# print(a[3])
# #Slicing
# a="Hello,World"
# print(a[2:5])
# #Negative Indexing
# a="Hello,world!"
# print(a[-7:-4])
# print(a[-3])
# #String Length
# a="Hello,world!"
# print(len(a))
# #String Methods
# #strip
# a="  hello,world! "
# print(a.strip())
# #lower
# a="hello,world!"
# print(a.lower())
# #upper
# a="hello,world!"
# print(a.upper())
# #replace
# a="hello,world!"
# print(a.replace("hello","goodbye"))
# #split
# a = "Hello, World!"
# print(a.split(","))
# #check string
# a= 20,30,40
# x=30 in a
# print(x)
# a= 20,30,40
# x=30 not in a
# print(x)
#
# a= "hello,world1"
# x= "llo" in a
# print(x)
# #String Concatination#
# fname= "Palak"
# lname= "Mahajan"
# x= fname + " " + lname
# print(x)
# a=30
# b=40
# c= b - a
# print(c)
# #String Format
# age= 27
# text= "My name is Palak, and I am {}"
# print(text.format(age))
# a= {1,2,3,4,5,6,6,6,1,0,8,8,9,0,1}
# print(a)
#a= fr{"Amit","palak","Aishwarya"}
#print(a)

# b= tuple(("palak","Amit","Akash","Deepak"))
# print(b)
#
# #Changing Tuple values
# thistuple= ("palak","Amit","Akash","Deepak")
# y= list(thistuple)
# y[1]= "Aishwarya"
# thistuple= tuple(y)
# print(thistuple)
# # Checking If Item Exists in List Through Loop
# thistuple= ("palak","Amit","Akash","Deepak")
# if "palak" in thistuple:
#     print("Yes, name is present in the list")
# # Tuple Length
# thistuple= ("palak","Amit","Akash","Deepak")
# print(len(thistuple))
# #SETS
# #Adding new values in Set
# thisset= {"palak","Amit","Akash","Deepak"}
# thisset.add("Aishwarya")
# print(thisset)
# #adding Multiple values In Set
# thisset= {"palak","Amit","Akash","Deepak"}
# thisset.update(["Aishwarya","Ankit"])
# print(thisset)
# #Remove Item from SET
# thisset= {"palak","Amit","Akash","Deepak","Aishwarya","Ankit"}
# thisset.remove("Aishwarya")
# print(thisset)
# #Dictionary
# thisdict= {'name': "Palak","age": 27, "Work": "Software Engineer"}
# print(thisdict)
# #Accessing Values By It's Key In Dictionary
# thisdict= {'name': "Palak","age": 27, "Work": "Software Engineer"}
# x= thisdict["Work"]
# print(x)
# # Changing Values By Referring It's Key
# thisdict= {'name': "Palak","age": 27, "Work": "Software Engineer"}
# thisdict["Work"] = "Tester"
# print(thisdict)
# # Check if Key Exists:
# thisdict= {'name': "Palak","age": 27, "Work": "Software Engineer"}
# if "Work" in thisdict:
#     print("Software Engineer")
# #Adding Items
# thisdict= {'name': "Palak","age": 27, "Work": "Software Engineer"}
# thisdict["Company"]= "IntegriChain"
# print(thisdict)
# #Removing Itmes
# thisdict= {'name': "Palak","age": 27, "Work": "Software Engineer","Company":"IntegriChain"}
# thisdict.pop("Company")
# print(thisdict)
#
# thisdict= {'name': "Palak","age": 27, "Work": "Software Engineer","Company":"IntegriChain"}
# thisdict.popitem()
# print(thisdict)
#
# b= list(("palak","Amit","Akash","Deepak"))
# print(b)

x = frozenset({"apple", "banana", "cherry"})
print(x)

 



