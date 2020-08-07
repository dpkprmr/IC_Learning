# def myfunc(fname, lname):
#     print(fname + " " + lname)
# myfunc("Palak","Mahajan")
# myfunc("Emil","Jone")
#
# def myfunc(*kids):
#     print("the youngest kid is" +" " + kids[0])
# myfunc("Emil","Jone","Eric")
# Area of Square
# def myfunc(x):
#     area = x*x
#     print(area)
# myfunc(4)
# def myfunc(l,b):
#     area = l*b
#     print(area)
# myfunc(4,8)
# Default Parameter value
# def myfunc(country = "India"):
#     print("I am from" + " "+ country)
# myfunc()
# myfunc("Europe")
# myfunc("Brazil")
# Return Values
def myfunc(x):
    return 5 * x
print(myfunc(3))
print(myfunc(5))
# Palindrome
def pal(num):
    x= num[:: -1]
    if x== num:
        print("palindrome")
    else:
        print("not a palindrome")
print (pal('madam'))
# Fibonacci Series
n= int(input("enter the value for n"))
a= 0
b= 1
sum= 0
count= 1
print(a,b, end= " ")
while (count <=n):
    print(sum, end=" ")
    count +=1
    a=b
    b=sum
    sum= a+b




