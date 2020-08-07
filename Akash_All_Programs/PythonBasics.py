# Variables
a = 30
b = 'Akash'
print("Major Branch Commit")
print("merge Conflict")
print(a)
print(b)
# Integer
a = 30
print(a)
# Complex
b= 2+8j
print(b)
# Float
c = 2.35
print(c)
# Type Conversion
d= float(a)
print(d)
e = int(c)
print(e)
# Lists
Task = ['Learn Python', 'In', 15, 'Days']
Task2 = ['Use Pycharm', 'Windows10', 2.5]
Task.append("Appended")
Task.extend(Task2)
print(Task, "Extended")
Task.insert(2, 'FreshInset')
Task.reverse()
print(Task, "Task List is reversed")
# Task[2] = 30
a = id(Task)
print(a)
print(Task)
print(len(Task))
print(Task[3])
print(Task[1:])
print(Task[1:3])
print(Task*2)
print(Task+Task2)

#tuple inside a List
Games = [('Criket', 'Football', 'Basketball'), ('2011', '2010', '2008')]
print(Games[1][1])

Coordinates = [(2,3),(3,4),(4,6)]
print(Coordinates)
Coordinates.append((3,7))
print(Coordinates)

# Tuple
print("------------------------TUPLE STARTING FROM HERE------------------------")
tuple = ('Learn Python', 'In', 15, 'Days')
tuple2 = ('Learn Python', 'Learn Python', 'In', 15, 'Days')
print(tuple2)
print(tuple.index("In"))
print(tuple.__len__())
print(tuple2.count('Learn Python'))
print(tuple)
print(id(tuple))
tuple = ('Learn Java', 'In', 15, 'Days')
print(tuple)
print(id(tuple))

# STRING
print("---------------------STRING STARTS FROM HERE-------------------")
a= 'I will learn Python basics first than move forward'
print(a)
print(len(a))
print(a.count('e'))
print(a.index('l'))
print(a[0:3])
print(a[-4:-1])
print(a[-1])
print(a[:-1])
print(a[::-1])
print(a.upper())
print(a + ' ' + 'Python')

if 'P' in a or 'Z' in a:
    print("It is present")


# SET
print("----------------------SET START FROm HERE-------------")
firtsset = {0,1,9,11,2,3,4,5,6,6}
secondset = {7,6,8,9}
thirdset = {"Akash","Priyanka","Aishwarya","False"}
print(sorted(thirdset))
print(sorted(thirdset,reverse = True))
print(firtsset)

list = ['q','u','u']
x=set(list)
print(x)
a = set(['AkAssh','You','Are','Not','Good','In','Python','Yet'])
print(a)
b= set(['AkAssh','You','Are','Good','In','Python'])
union = a.union(b)
intersection = a.intersection(b)
print(union)
print(intersection)
is_disjoint = a.isdisjoint(b)
print(type(is_disjoint))
print(is_disjoint)
print("CHANGED")
print("CHANGED GREAT It")

# Dictionary
print("----------------DICTIONARY START FROM HERE-------------")
a= {'name' : 'Akash', 'age' : 27, 'list': ['He is very good', 'But not so good in Python']}
b= {'Designation' : 'SQE', 'Status' : 'Soon to be Married', 'tuple': (30, 40, 50),'set' : {'A','B','C'}}
print(b['Designation'])
print(a['list'])
print(b['tuple'])
print(b['set'])
a.pop('name')
print(a)

name = "My age is 23"
x= dict(name)
print(x)









