### Mini Challenge ###
def mini_challenge():
    num = int(input("Enter a number: "))

    if num > 0:
        print(f"{num} is a Positive number!")
    elif num < 0:
        print(f"{num} is a Negative number!")
    else:
        print("That number is a Zero!")

# mini_challenge()

####################################################################################################
### Challenge Time ###
# You're in the middle of examination, your classmate asked you for help.
    
def examination():
    print("The examination has started!")
    print("/*Proctor goes in the bathroom*/")
    print("Your classmate asked you for help.")
    response = input("Hey can I see your answers? (Y/N): ")
    if response == "Y" or response == "y":
        yes()
    elif response == "N" or response == "n":
        no()

def yes():
    print("Your classmate started to copy your answers.")
    print("Your classmate is doesnt want to give back your paper because he not done copying all of it.")
    action = int(input("What do you want to do? (1 = Force him, 2 = Let him Finish): "))
    if action == 1:
        print("You force him to give back your paper.")
        print("Close call, the proctor almost caught you.")
        print("Your classmate is a little bit frustrated but thanks you anyway.")
    elif action == 2:
        print("You let him finish copying your answers.")
        print("The proctor caught you both red handed.")
        print("You and your classmate are now facing the consequences of your actions. Game Over!")

def no():
    print("You refused to give your answers.")
    print("Your classmate is mad at you!, but copies anyway")
    action = int(input("What do you want to do? (1 = Tell the proctor, 2 = Let him copy): "))
    if action == 1:
        print("You told the proctor that your classmate is copying your answers.")
        print("Your classmate is now facing the consequences of his actions.")
        print("Friendship over. Game Over")
    elif action == 2:
        print("You let him finish copying your answers.")
        print("The proctor caught you both red handed.")
        print("You and your classmate are now facing the consequences of your actions. Game Over!")



#xamination()
