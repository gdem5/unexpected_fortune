""" Import modules
:typing- annotation of variable types
:random- generation of pseudo-random numbers
:colorama- editing text in the terminal
"""

import typing
import random
import colorama
from colorama import Fore, Style
colorama.init()

def load_file (file_name: str) -> str:

    with open (file_name, 'r') as file:
        return [file_lines.strip().upper() for file_lines in file]
       
    
def create_box (word: str, selected_letters: str, last_choice: str) -> str:
    """Creating boxes to guess the drawn password - number of underscores according to the number of letters in the password. 
        Coloured and normal are identical character strings, but in the case of the string 'coloured'- the letter belonging to the string
        'last choice' is displayed in blue (boldface is also added).
    """

    normal = ''
    colour = ''

    for letter in word:
        if letter in selected_letters or not letter.isalpha():
            normal += letter
            if letter == last_choice:
                colour += Fore.GREEN + letter + Style.RESET_ALL
            else:
                colour += letter 
        else:
            normal += '_'
            colour += '_'

    return normal, colour


def main_function():

    """ The main function calls the functions previously declared with the corresponding arguments. password
        words- list of all passwords read from each line of the file
        password- str- password to be guessed (drawn from the list of words)
        selected_letters- set- set of letters that have already been entered by the user
        last_choice- str- letter entered last by user
    """

    words = load_file('fortune.txt')
    password = random.choice(words)
    selected_letters = set()
    last_choice = ''

    while True:
        
        #ucreate empty box
        normal, colour = create_box (password, selected_letters, last_choice)
        print("\Guess the password: ", colour)

        #sprawdzenie czy wszystkie litery zostały odgadnięte
        if all (letter in selected_letters or not letter.isalpha() for letter in password):
            print("Guess the password: ", password)
            break
        
        #wprowadzenie danych przez użytkownika
        select_letter = input("specify the letter: ").upper()

        # sprawdzenie przynależności wprowadzonego znaku do alfabetu oraz zbadanie długości wprowadzonego znaku
        if len (select_letter) !=1 or not select_letter.isalpha():
            print("Incorrect selection! Enter one letter")
            continue

        if select_letter in selected_letters:
            print("This letter was already given")
            continue
         
        selected_letters.add(select_letter)
        last_choice = select_letter
        if select_letter in password:
            print(f"Super!, letter {select_letter} is in the password")
        else:
            print(f"Unfortunately... letter {select_letter} s not in the password, please try again!")

main_function()