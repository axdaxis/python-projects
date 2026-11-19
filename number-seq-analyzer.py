import math
import sys

def fib():
    valsInput = input("How many values would you like to generate? ")
    try:
        values = int(valsInput)
    except ValueError:
        print("You must input a number.")
        return
    
    fibVals = []
    x, y = 0, 1
    for i in range(values):
        fibVals.append(x)
        x, y = y, x + y
    print(*fibVals, sep=", ") # https://stackoverflow.com/a/15769313

    return

def checkPrime():
    primeInput = input("Enter a number: ")
    try:
        value = int(primeInput)
    except ValueError:
        print("You must input a number.")
        return
    for i in range(2, value):
        if value % i == 0:
            print(f"{value} is not a prime number.")
        else:
            print(f"{value} is a prime number!")
            #THIS IS BROKEN AS HELL!!!!
        

def rangePrime():
    pass

def genMulti():
    pass

def factorial():
    pass

def collatz(): #what even is this
    pass

while True:
    print("\n") # Padding I guess?
    print("Choose an option with your keyboard:")
    print("1: Fibonacci sequence")
    print("2: Check a prime number")
    print("3: Display prime numbers in a range")
    print("4: Generate a multiplication table")
    print("5: Generate a factorial")
    print("6: Run a Collatz sequence")
    print("0: Exit")

    menuOpt = input("Select: ")
    try:
        option = int(menuOpt)
    except ValueError:
        print("You must input an option present in the menu.")
    match option:
        case 0:
            sys.exit()
        case 1: # fibonacci
            fib()
        case 2: # check prime
            checkPrime()
        case 3: # primenum range
            rangePrime()
        case 4: # multitable
            genMulti()
        case 5: # factorial
            factorial()
        case 6: # collatz
            collatz()