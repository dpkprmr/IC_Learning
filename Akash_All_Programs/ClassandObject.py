class student:

    # Class Variable
    perc_raise = 1.05
    def __init__(self,first,last,mariks):
        self.first = first
        self.last = last
        self.marks = mariks
        self.email = first+'.'+last+'@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first , self.last)

    def appy_raise(self):
        self.marks = int(self.marks*5)

stu_1 = student("Akash","Gupta","55")
stu_2 = student("Arsh","Gupta","55")
print(stu_1.first)
print(stu_1.fullname())
print(stu_2.fullname())
print(stu_1.marks)
print(stu_1.appy_raise())
print(stu_1.marks)
print(stu_2.__dict__)

# Inheritance
class Dumb(student):
 per_raise = 1.10
 

    def __init__(self,first,last,mariks,proglang):
        super().__init__(first,last,mariks)
        self.proglang = proglang

stu_1 = Dumb("Akash", "Gupta", "55","Python")
print(stu_1.proglang)


# stu_1 = student()
# stu_2 = student()

# # Instance Variable
# stu_1.firstname = "Akash"
# stu_1.lastname = "Gupta"
# stu_1.email = "agupta@integrichain.com"
# stu_1.marks = 99
#
# stu_2.firstname = "Arsh"
# stu_2.lastname = "Gupta"
# stu_2.email = "arshgupta@integrichain.com"
# stu_2.marks = 100
#
# print(stu_1.firstname)
