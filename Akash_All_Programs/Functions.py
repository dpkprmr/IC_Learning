def evenodd(self):
    num = int(input("Enter the number"))
    if (num%2 ==0):
        print("number is even")
    else:
        print("Number is odd")

evenodd()

def evenoffref(x):
    num =  x
    if (num%2 ==0):
        print("number is even")
    else:
        print("Number is odd")
evenoffref(4)

def myfun(*argv):
    for arg in argv:
     print(arg)
    print("CHANGED in MINOR")

myfun("My First","Python","Lecture",15)


def sqr():
    i=1
    while True:
        yield i*i
        i=i+1

for num in sqr():
    if(num>100):
        break
    print(num)

def cube(x):
    return x*x*x
print(cube(5))

g= lambda y : y*y*y
print(g(7))

print("change 2")

a= lambda x,y:x+y
print(a(3,7))
print("Change")

x= lambda a,b: (a+b)**2
print(x)
def sum(x):
    return (lambda y : x+y)
t= sum(5)
print(t(5))

def sum2(x,y):
    return x+y
print(sum2(3,4))

mylist = [1,2,3,4,5,6]
newList = list(filter(lambda a:(a/3==2),mylist))
newList2= list(filter(lambda a:(a/3!=2),mylist))
newList3= list(map(lambda a:(a/3!=2),mylist))
print(newList3)
print(newList2)
print(newList)





