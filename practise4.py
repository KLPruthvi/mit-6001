'''def even_number(i):
#Input i a positive integer
    reminder = i % 2
    return reminder == 0 # if no return statement it gives none
print("all numbers between 1-20 even or not")
for i in range (20): # here we are checking whether the numbers of odd or even
    if even_number(i):
        print(i," is even")
    else:
        print(i,"is not even")


def func_a():
    print("inside func_a")
def func_b(y):
    print("inside func_b")
    return y
def func_c(z):
    print("inside func_c")
    return z()
print(func_a())
print( 5 + func_b(2))
print(func_c(func_a))

def g(y): #this is allowed in python even if y is not being called anywhere
    print(x)
    print(x + 1)
x = 5
g(x)
print(x)
'''

def g(x):
    def h():
        x = 'abc'
    x += 1
    print("g: x= ", x)
    h()
    return x
x = 34
z = g(x)
        
    

    