print("Limit: 20")
print("")
for i in range(0, 21):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz!")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)
print(" ")
