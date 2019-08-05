from typing import NewType

def getAge(age):
    right_age = age
    while (type(right_age) != int):
        try:
            int(right_age)
            break
        except:
            right_age=input(f'oops, looks like you didn\'t enter a valid age.\nPlease enter a number\n')
    return right_age

def hobbies(name, age: int, hobby, *optional_hobbies, **other):
    output = f'my name is {name}, my age is {age}.\nI like {hobby} {optional_hobbies}.'
    for k, v in other.items():
        output += f'\n{k} - {v}'

    return output



if __name__ == "__main__":
    print(hobbies('eyal', int(input('please enter you age\n')), 'playing', 'basketball', 'guitar', 'computer sience', 8, other=["other1", "other2"], ball_sports=['basktball', 'football'], distler='nmotzez zain'))
    
            
