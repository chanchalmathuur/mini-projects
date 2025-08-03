import random
'''1
1 for stone
-1 for paper
0 for scissor'''
computer = random.choice([-1,0,1])
youstr = input("enter the choice: ")
youDict = {"s":1,"p":-1,"sc":0}
reverseDict = {1:"stone", -1:"paper", 0:"scissor"}

you = youDict[youstr]

print(f"you choose {reverseDict[you]}\n computer choose {reverseDict[computer]}")

if(computer==you):
    print("Its a Draw")

else:
    if(computer == -1 and you == 1):
        print("you lose!")
    elif(computer == -1 and you ==0):
        print("you win!")
    elif(computer == 1 and you == -1):
        print("you win!")
    elif(computer == 1 and you == 0):
        print("you lose!")
    elif(computer == 0 and you == 1):
        print("you win!")
    else:
        print("Something went wrong")