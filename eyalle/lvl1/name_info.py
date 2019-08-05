import datetime

def calcYear(age):
    now = datetime.datetime.now()
    return (now.year - age)

NAME = input('Enter your name please: ')
AGE = int(input('Now, you\'re age: '))
birth_year = calcYear(AGE)


print (f'Hello {NAME}!\nYou were born in {birth_year} :)')

