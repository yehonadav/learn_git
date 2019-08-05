from random import randint

generated_num = randint(0,10)

def check_index(num):
    return_val = ''
    printed_val = ''
    if (generated_num > num):
        printed_val = 'too low'
        return_val = 'lows'
    elif (generated_num < num):
        printed_val = 'too high'
        return_val = 'highs'
    else:
        printed_val = 'exactly :)'
        return_val = 'exacts'
    print(printed_val)
    return return_val

def game_controller():
    user_guesses = {'lows': [], 'highs': [], 'exacts': []}
    user_input = input("guess a num between 0 and 10\n")
    while (user_input != "quit"):
        
        while (not isinstance(user_input, int)):
            try:
                user_input = int(user_input)
            except ValueError:        
                user_input = input("guess a num between 0 and 10\n")
        user_guesses[check_index(user_input)].append(user_input)
        user_input = input("guess a num between 0 and 10\n")
    
    guesses = f'ok, so here are your guesses:\nyou had {len(user_guesses["lows"])} lows, {len(user_guesses["highs"])} highs and {len(user_guesses["exacts"])} exact matches'
    print(f'{guesses}\n\n')
    print(user_guesses)

if __name__ == "__main__":
    game_controller()
