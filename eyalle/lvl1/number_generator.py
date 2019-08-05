
from random import randint

def numbers(range):
    while (range > 0):
        yield randint(0, 10000)
        range -= 1
    pass

def main():
    for n in numbers(20): 
        print(n)

if __name__ == "__main__":
    main()