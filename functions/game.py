#rock,paper,scissors
import random

options = ["rock","paper","scissors"]

computer = random.choice(options)
you = input("Enter your choice : ")

print(you)
print(computer)

if(you == computer):
    print("Its a draw !")

else:
    if(you == "rock" and computer == "paper"):
        print("computer wins ! ")

    if(you == "rock" and computer == "scissors"):
        print("you wins ! ")

    if(you == "scissors" and computer == "paper"):
        print("you wins ! ")

    if(you == "scissors" and computer == "rock"):
        print("computer wins ! ")

    if(you == "paper" and computer == "scissors"):
        print("computer wins ! ")

    if(you == "paper" and computer == "rock"):
        print("you wins ! ")

    