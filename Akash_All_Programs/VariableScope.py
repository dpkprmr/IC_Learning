var1 = 5


def scope_of_var():

    print("inside Scopeofvar")

    def scope_inner():
        var = 1
        print('inside Scopeinner',var)

    scope_inner()
    print("Outer Var", var1)

scope_of_var()


s= 6
def f():
    print(s)
    def f2():
     global s
     print(s)
     s = 5
     print(s)
    f2()
f()




# a= 1 if 20>0 else 0
# print(a)

