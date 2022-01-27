import requests
from random import randint
import string
from colorama import init, Fore, Back, Style

init(autoreset=True)  # for colorama to avoid having to reset the colors manually
guess_number = 1

def green(letter):
    return Style.BRIGHT + Back.GREEN + Fore.WHITE + letter


def yellow(letter):
    return Style.BRIGHT + Back.YELLOW + Fore.WHITE + letter


def gray(letter):
    return Style.BRIGHT + Back.WHITE + Fore.BLACK + letter


def generate_word():
    global wordlist
    wordlist = []
    words = requests.get(
        'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt')
    for i in (list(words.text.split("\n"))):
        if len(i) == 5:
            wordlist.append(i.upper())
    return wordlist[randint(0, len(wordlist) - 1)]


def pick_random_word(wordlist):
    return wordlist[randint(0, len(wordlist) - 1)]


def intro():
    print("Welcome to Wordle.\n\
Guess a five letter word.\n\
Letters that are in the word but in the wrong spot will be yellow.\n\
Letters in the correct spot will the green.\n\
Grey letters aren't in the word.\n")


def user_guess():
    while True:
        global guess_number
        if guess_number == 7:
            print("Out of guesses, game over.")
            quit()
        print(Style.BRIGHT + f"Guess {guess_number} of 6.")
        guess = input("Guess a five letter word or 'q' to quit. ").upper()
        if guess == "Q":
            print("bye")
            quit()
        elif str.isalpha(guess) == False:
            print("Something's not a letter, try again.")
        elif len(guess) != 5:
            print("That's not a five letter word, try again.")
        if guess not in wordlist:
            print("That's not a real word, try again.")
        else:
            guess_number += 1
            return guess


def check_guess(guess):
    color_array = ["gray", "gray", "gray", "gray", "gray"]
    for i in range(0, 5):  # check for letter in any position, make yellow
        if guess[i] in word:
            color_array[i] = "yellow"
    for i in range(0, 5):  # check for letter in correct position, make green
        if guess[i] == word[i]:
            color_array[i] = "green"
    guess_colored = []
    for i in range(0, 5):
        guess_colored.append(eval(color_array[i] + "(guess[i])"))  # eval calls color fxns to print colored letters
    print(''.join(guess_colored))  # print the guess with colored letters
    return color_array  # so that we can check for a win (all greens)


word = generate_word()

#print(word)  # DEBUG, show answer

intro()

while True:
    guess = user_guess()
    color_array = check_guess(guess)
    if color_array == ['green', 'green', 'green', 'green', 'green']:
        print("You win!")
        break
