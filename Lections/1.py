a = 5
def f(x,y = a):
    return x*y
print (f(2))

a = 3
print (f(2))
#--------------------------------------------
def f1(a, l=[]):
    l.append(a)
    print(l)
    return l
f1(1)
f1(1)
l = f(1) #Bude zsylatys na 1 komirky pamyati
#--------------------------------------------
def f3(a = None):
    if a is None:
        print("A is None")
    else:
        print("A NOT None")
f3()
f3(1)
f3(None)
#--------------------------------------------


