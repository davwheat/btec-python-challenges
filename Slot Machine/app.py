from random import choice
from time import sleep
import sys

current_money = 100.00
spin_cost = 1
all_symbols=["☻", "♥", "♦", "♣", "♠", "☼"]

def spinRandom(count = 1):
    global all_symbols

    spins = []
    for i in range(count):
        spins.append(choice(all_symbols))

    return spins

def processSpin(spin):
    if spin[0] == spin[1] == spin[2]:
        return 10
    if spin[0] == spin[1] or spin[0] == spin[2] or spin[1] == spin[2]:
        return 2
    else:
        return 0

def startSpin():
    global current_money
    global spin_cost

    print(f"You have £{current_money} remaining.")
    print(f"One spin costs £{spin_cost}.\n")
    print(f"Press ENTER to spin the slot machine...\n")
    input()
    current_money -= spin_cost
    spins = spinRandom(3)

    print(f"{spins[0]}     ", end="\r", flush="True")
    sleep(0.5)

    print(f"{spins[0]} {spins[1]}   ", end="\r", flush="True")
    sleep(0.5)

    print(f"{spins[0]} {spins[1]} {spins[2]} ", flush="True")
    sleep(0.5)

    winningMultiplier = processSpin(spins)
    winnings = spin_cost * winningMultiplier

    current_money += winnings

    print(f"You won £{winnings}")
    

def main():
    while current_money > 0:
        startSpin()
    
    print("You've run out of money!")

main()