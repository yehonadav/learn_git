#from HM_final_funcs import pri, is_valid_input, check_valid_input, show_hidden_word, check_win, print_hangman, choose_word, pri_logo, start_game
from HM_final_funcs import  pri_logo, start_game
pri_logo()

if __name__ == "__main__":
    # os.system('pip install -r requirements.txt')
    WORDS_FILE_PATH = input("Hello!\nPlease submit the words file So I can pick a word for you, or hit Enter for default:\n\t")  or "words.txt"
    WORD_INDEX = input("Also, please enter a random number:\t") or 63
    start_game(WORDS_FILE_PATH, WORD_INDEX)

    '''
    Once player enters a file path, and an index:
    1. Present start of game with underscores
    2. input guessed char
    3. check, if valid:
      3.1 check, if char is part of SECRET_WORD:
        3.1.1 Reveal it
      3.2 else, print the appropriate HANGMAN PHOTO
    4. else, ask the player to enter valid char
    5. iterate until word is guessed or user runs out of guesses
    '''
