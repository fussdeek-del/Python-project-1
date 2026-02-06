import random

computer = random.choice([1,-1,0])
reversedict = {1 :"snake", -1:"water", 0:"gun"}
youstr = input("Enter your move: ")
allDict = {"s": 1, "w":-1, "g":0}
you = allDict[youstr]

print(f"you chose: {reversedict[you]}")
print(f"computer chose: {reversedict[computer]}")


if (computer == you):
    print("its a draw")

else:    
    if (computer == -1 and you ==1):
        print("you  win!")

    elif (computer == -1 and you ==0):
        print("you lose!")

    elif (computer == 1 and you ==-1):
        print("you  lose!")

    elif (computer == 1 and you ==0):
        print("you  win!")

    elif (computer == 0 and you ==-1):
        print("you  win!")

    elif (computer == 0 and you ==1):
        print("you  win!")

    else:
        print("some thing went wrong")
