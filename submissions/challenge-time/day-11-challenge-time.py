with open('submissions/challenge-time/input.txt', 'r') as file:
    names = file.readlines()
    file.close()

sortedNames = sorted(names)

with open('submissions/challenge-time/input.txt', 'w') as file:
    for name in sortedNames:
        file.write(name)
    

