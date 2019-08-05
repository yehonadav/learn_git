import random
import colorsys
import os
from colored import fg, bg, attr


global HANGMAN_PHOTOS
HANGMAN_PHOTOS = {
    0: """
        x-------x""",
    1: """
        x-------x
        |
        |
        |
        |
        |""",
    2: """
        x-------x
        |       |
        |       0
        |
        |
        |
    """,
    3: """
        x-------x
        |       |
        |       0
        |       |
        |
        |
    """,
    4: """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
    """,
    5: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
    """,
    6:"""
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
    """
    }
def get_secret_word():
    """
    get_secret_word() is used to obtain the SECRET_WORD
    """
    return SECRET_WORD

def pri(str):
    """
    pri(str) sets the text color to magenta, prints the given str and resets to default
    """
    TEXT_COLOR = fg(199)
    RES = attr('reset')
    print (TEXT_COLOR, str, RES)

def start_game(WORDS_FILE_PATH, WORD_INDEX):
    """
    start_game will be responsible for tha management of the game.
    It will basically interact with the user and call functions.
    :param WORDS_FILE_PATH: string representing a file with words in it
    :param WORD_INDEX: string an index to use for choosing the word to be guessed
    :type WORDS_FILE_PATH: string
    :type WORD_INDEX: string
    :return: no returned value
    :rtype:  no returned value
    """

    letters_guessed = []
    os.system('clear')
    pri_logo()

    global SECRET_WORD
    SECRET_WORD = choose_word(WORDS_FILE_PATH, int(WORD_INDEX))[1]
    ALLOWED_TRYS = 0

    while (not(check_win(letters_guessed)) and ALLOWED_TRYS < len(HANGMAN_PHOTOS)-1):
        char_guessed = input("Please guess a letter\n")
        while (not(check_valid_input(char_guessed, letters_guessed))):
            char_guessed = input("please use valid english characters only, and not letters already guessed.\n")
        ALLOWED_TRYS = print_hangman(ALLOWED_TRYS, char_guessed)
        pri (show_hidden_word(letters_guessed))

    if (ALLOWED_TRYS < len(HANGMAN_PHOTOS)-1):
        pri ("YOU WIN ! ! !")
    else:
        pri ("you lose :(")

def is_valid_input(letter_guessed):
    """
    letter_guessed checks if the argument passed is a valid English letter or not.
    :param letter_guessed: player's char
    :type letter_guessed: string
    :return: True or False, if the player's char is in English
    :rtype: boolean
    """
    is_valid = ((len(letter_guessed) == 1) and (letter_guessed.isalpha()))
    return (is_valid)

def check_valid_input(letter_guessed, old_letters_guessed):
        """
        check_valid_input checks the letter_guessed against old_letters_guessed in the following manner:
        if letter_guessed is not in old_letters_guessed, and returns True from is_valid_input(letter_guessed)
        then return True, else return False.
        :param letter_guessed: player's char
        :param old_letters_guessed: list of letters guessed
        :type letter_guessed: string
        :type old_letters_guessed: list
        :return: True or False, if the player's char is in English and not already guessed
        :rtype: boolean
        """
        valid_input = False
        if (is_valid_input(letter_guessed) and (old_letters_guessed.count(letter_guessed)) < 1):
            old_letters_guessed.append(letter_guessed)
            valid_input = True
        else:
            pri ("\n X")

        return valid_input

def show_hidden_word(old_letters_guessed):
    """
    show_hidden_word recieves a list of old letters guessed and returns a string with the right old letters guessed and _ instead of missing letters
    :param old_letters_guessed: list of letters guessed
    :type old_letters_guessed: list
    :return: generated string, of successfully guessed chars and _ instead of chars that remain unguessed
    :rtype: string
    """
    successfully_guessed = ("_ " * len(SECRET_WORD)).split()
    for char in old_letters_guessed:
        if (check_guess(char)):
            successful_indexes = get_guessed_index(char)
            for index in successful_indexes:
                successfully_guessed[index] = char
    return "".join(successfully_guessed)

def check_win(old_letters_guessed):
    """check_win recieves the list of old letters guessed and will return True if the secret word was fully guessed or False, otherwise
    :param old_letters_guessed: list of letters guessed
    :type old_letters_guessed: list
    :return: True if SECRET_WORD was guessed
    :rtype: boolean
    """
    win = all([char in old_letters_guessed for char in get_secret_word()])
    return win

def check_guess (char):
    """
    check_guess recieves a charand will return True if the char is in the SECRET_WORD, or False otherwise.
    :param char: a guessed character
    :type char: string
    :return: True if char is in SECRET_WORD
    :rtype: boolean
    """
    return (char in get_secret_word())

def print_hangman(num_of_tries, char):
    """
    print_hangman recieves the number of tries a user has and does the following:
        if the character guessed is valild, and is part of the secret word - print the current state of HangMan, return the same amount of guesses left.
        Else, print the HangMan pose after the unsuccessful guess, and return the num_of_tries + 1
    :param num_of_tries: player's number of tries
    :param char: player's guessed char
    :type num_of_tries: int
    :type char: string
    :return: the number of guesses the player has accumulated
    :rtype: int
    """

    if (not(is_valid_input(char) and check_guess(char))):
        num_of_tries += 1
    pri (HANGMAN_PHOTOS[num_of_tries] + "\n\n\n")
    return num_of_tries

def get_guessed_index(successfully_guessed):
    """
    get_guessed_index recieves a successfully guessed char in SECRET_WORD and returns all the indexes of that char in SECRET_WORD
    :param successfully_guessed: successfully guessed char
    :type successfully_guessed: string
    :return: list of indexes of successfully_guessed in SECRET_WORD
    :rtype: list
    """
    return [i for i, ch in enumerate(SECRET_WORD) if ch == successfully_guessed]

def choose_word(file_path, index):
    """
    choose_word recieves a string-based file path, and an index.
    choose_word will return a tuple that contains - (num of unique words in file, a random word based on the index)
    :param file_path: a string representing a file
    :param index: a number
    :type file_path: string
    :type index: int
    :return: tuple of 2 elements (num of unique words in file, a random word to guess)
    :rtype: tuple
    """

    f = open(file_path, 'r')
    words = f.read().rsplit()
    f.close()
    words_set = sorted(set(words), key=words.index)
    words_limit = len(words_set)
    if (index > len(words)): #in case the given index is bigger than the amount of words in the file
        index = index - (len(words) * (index // len(words)))

    words_list = list(words_set)

    pri ("")

    return (words_limit, words[index-1])

def pri_logo():
    """
    pri_logo will use pri() to print out the logo of Hangman
    """
    HANGMAN_ASCII_ART ="""
 =============================================================
|      _    _                                                 |
|     | |  | |                                                |
|     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __          |
|     |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\         |
|     | |  | | (_| | | | | (_| | | | | | | (_| | | | |        |
|     |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|        |
|                          __/ |                              |
|                         |___/                               |
 =============================================================
    """

    pri (HANGMAN_ASCII_ART)
