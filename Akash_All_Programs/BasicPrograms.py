
i=1
while(i<=10):
    if i%2==0:
        print(i, 'is even')
    else :
        print(i, 'is odd')
    i=i+1

    print("its a basic program")


# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a-b
#
# def divide(a, b):
#     return a/b
#

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Divide")

# choice = input('Enter Choice 1/2/3:')
# if choice in ('1', '2', '3', '4'):
#     a = int(input("Enter value for first number:"))
#     b = int(input("Enter value for second number:"))
#     if choice == '1':
#         print(a, "+", b, "=", add(a, b))
#     elif choice == '2':
#         print(a, "-", b, "=", subtract(a, b))
#     elif choice == '3':
#         print(a, "/", b, "=", divide(a, b))
#
# else:
#     print('invalid input')




a=1
while(a<10):
    print(a)
    a = a+1

assert 5>4, "5 is not less than 3"

# correctNum = 13
# choice = int(input("Please enter a number"))
# if choice < correctNum:
#         print("number is too small")
# elif choice > correctNum:
#         print("number is too large")
# elif choice == correctNum:
#         print("congratulations")
#

fruits = ['Mangoes','Bananan','Apple']

for fruit in fruits:
    print("fruit in list is",fruit)

print("no fruits left in the list")
#
# num = int(input("Please enter a Number"))
# fac = 1
# if num<0:
#     print("Number should be positive")
# elif num==0:
#     print("Factorial is 1")
# else:
#     for i in range(1, num+1):
#      fac = fac*i
#     print(fac)
#


num = open("D:/FileHandling/NewDoc.txt", "r")
print(num.read())
t = num.read()
x = int(t)
print(x)

# x = print(type(t))
# print(t)
#
# if t%2==0:
#      print("Even")
# else:
#          print("odd")

