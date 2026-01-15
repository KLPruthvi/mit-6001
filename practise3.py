'''name = "pruthvi" '''

'''print(len(name))

print(name[3])
print(name[-5])
print(name[3:7:2])
print(name[::])
print(name[::-1])
print(name[4:1:-2])

name = 's'+ name[1:7]
name = 's'+ name[1:5]
print(name)

X = input("please enter a name ")
if 'u' in X or 'i' in X:
    print("there is an I or U in name")
else:
    print("there is no U or I in name")

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
i = 0
while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    i += 1
print("What does that spell?")
for i in range(times):
    print(word, "!!!")


s1 = "mit u rock"
s2 = "i rule mit"
if len(s1) == len(s2):
    for char1 in s1:
        if char1 in s2:
            print("Common letter")


cube = 64
for guess in range(cube+1):
    if guess**3 == cube:
        print("cube root of", cube ,"is", guess)'''
        
cube = float(input("Enter a number"))
was_negative = False
if cube < 0:
    was_negative = True
    cube = abs(cube)
high = max(1, cube) ##to set
epsilon = 0.01
num_guesses = 0
low = 0
guess = (high + low)/2.0

while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
if was_negative:
    guess = -guess
    cube = -cube
print ('num_guesses =', num_guesses)
print (guess, 'is close to the cube root of', cube)

