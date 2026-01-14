
'''hi = "Hello There"
ana = "Anna"
greet = hi + " " + ana
print("greet")

text = input("type")
print(5* int(text))'''

'''x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))
if x == y:
    print("x is equal to y")
    if y != 0:
        print("therefore, x/y is", x/y)
elif x > y:
    print("x is greater than y")
    print("therefore x/y is", x/y)
else:
    print("y is greater than x")
    print("therefore y/x is", y/x)
print("bye")'''

'''ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
     print("Just checking... did you mean", -x, "?")'''
    

answer = 0
negative = False
x = int(input("Enter a integer: "))
if x < 0:
    negative = True
while answer**3 < abs(x):
    answer = answer + 1
if answer**3 == abs(x):
    if negative:
        answer = - answer
    print("Cube root of", x, "is", answer)
else:
    print(x, "is not a perfect cube")
