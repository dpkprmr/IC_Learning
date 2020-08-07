# i=1
# while i < 6:
#     print(i)
#     i += 1
# Break Statement
i=1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1
# Continue Statement
# i=1
# while i < 6:
#     i += 1
#     if i ==3:
#         continue
#     print(i)
# Else
# i=1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")
# Nested While
# i=1
# j=5
# while i < 5:
#     while j > 1:
#         print(i,j)
#         i += 1
#         j -= 1
# Factorial
n=4
fact =1
for i in range(1,n+1):
    fact= fact * i
print(fact)
# Fibonacci Series
n= int(input("Enter value of n"))
a=0
b=1
c= a+b
print(a,b, end= " ")
while (c<=n):
    print(c, end= " ")
    a=b
    b=c
    c= a+b