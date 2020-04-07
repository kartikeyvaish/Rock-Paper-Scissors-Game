import os
import time
import random

def CpuChoseThis(a):
    if a==1:
        return "Rock"
    elif a==2:
        return "Paper"
    else:
        return "Scissors"

def UserChoseThis(a):
    if a == 'R' or a == 'r':
        return "Rock"
    elif a == 'P' or a == 'p':
        return "Paper"
    else:
        return "Scissors"

def GameCode():
    print("\t\tWELCOME TO STONE....PAPER....SCISSORS GAME")
    PlayerScore = 0
    CPUScore = 0
    PlayerOne = input("Enter Player Name - ")
    PlayerTwo = "CPU"
    BestOf = int(input("Enter Best Of HOW Much?? - "))
    for i in range(BestOf):
        os.system("CLS")
        print(f"\t\t{PlayerOne} VS {PlayerTwo}")
        print(f"\t\t{PlayerOne} = {PlayerScore} and {PlayerTwo} = {CPUScore}")
        print(f"\t\tGame Number {i+1}")
        Cpu = CpuChoseThis(RandomGenerator())
        time.sleep(1)
        print("\tRock....",end="", flush=True)
        time.sleep(1)
        print("Paper....", end="", flush=True)
        time.sleep(1)
        print("Scissors", end="", flush=True)
        print("\r")
        ch = input("Enter Choice - R or P or S - ")
        ch = UserChoseThis(ch)
        print(f"CPU Chose {Cpu}")
        print(f"\t{ch} VS {Cpu}")
        time.sleep(2)
        result = CheckWhoWon(ch,Cpu,PlayerOne)
        if result == 1:
            PlayerScore = PlayerScore + 1
        elif result == 2:
            CPUScore = CPUScore + 1
        else:
            PlayerScore = PlayerScore + 0.5
            CPUScore = CPUScore + 0.5

    os.system("CLS")
    print("\t\tFINAL SCORES ARE AS FOLLOWS")
    print(f"{PlayerOne} = {PlayerScore} and {PlayerTwo} = {CPUScore}")
    print("\r")
    if PlayerScore > CPUScore:
        print(f"\t{PlayerOne} Wins")
    elif PlayerScore < CPUScore:
        print(f"\t{PlayerTwo} Wins")
    else:
        print(f"\tThe Game was a DRAW")

def CheckWhoWon(ch, Cpu, PlayerOne):
    if ch == Cpu:
        print("\tDraw")
        time.sleep(1.8)
        return -1
    elif ch == 'Rock' and Cpu == 'Paper':
        print("\tCPU Won")
        time.sleep(1.8)
        return 2
    elif ch == 'Rock' and Cpu == 'Scissors':
        print(f"\t{PlayerOne} Won")
        time.sleep(1.8)
        return 1
    elif ch == 'Paper' and Cpu == 'Rock':
        print(f"\t{PlayerOne} Won")
        time.sleep(1.8)
        return 1
    elif ch == 'Paper' and Cpu == 'Scissors':
        print("\tCPU Won")
        time.sleep(1.8)
        return 2
    elif ch == 'Scissors' and Cpu == 'Rock':
        print("\tCPU Won")
        time.sleep(1.8)
        return 2
    elif ch == 'Scissors' and Cpu == 'Paper':
        print(f"\t{PlayerOne} Won")
        time.sleep(1.8)
        return 1

def RandomGenerator():
    N = random.randint(1, 3)
    return N

WantTo = 1
while WantTo == 1:
    GameCode()
    print("\r")
    WantTo = int(input("You Want TO Play More....PRESS 1....Otherwise any key to exit"))