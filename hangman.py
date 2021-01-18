import os
import random

def clean():
    os.system("clear")

options = { 1: "Anime", 2: "DC", 3: "Marvel" }

data = {
    "DC": ["Batman", "Shazam", "Aquaman"],
    "Marvel": ["Iron Man", "Spiderman"],
    "Anime": ["Eren Jaeger", "Saitama"]
}

def print_word(values):
    print()
    print("\t", end="")
    for x in values:
        print(x, end="")
    print() 

def check_win(values):
    for char in values:
        if char == '_':
            return False
    return True  

def play( word ):

    clean()

    displayOption = []

    rightChars = []

    incorrectGuess = 0
    
    incorretChars = []

    hangman_values = ['O','/','|','\\','|','/','\\']

    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

    for char in word:
        if char.isalpha():
            displayOption.append('_')
            rightChars.append(char.upper())
        else:
            displayOption.append(char)
    
    while True:
        print_hangman( show_hangman_values )
        print_word(displayOption)
        print("Errors:", incorrectGuess)

        val = input("Enter a character = ")
        if len(val) != 1:
            clean()
            print("Wrong choice!! Try Again")
            continue

        if not val[0].isalpha():
            clean()
            print("Wrong choice!! Try Again")
            continue

        if val.upper() in incorretChars:
            clean()
            print("Already tried!!")
            continue
        
        if  val.upper() not in rightChars:
            incorretChars.append( val.upper() )
            show_hangman_values[incorrectGuess] = hangman_values[incorrectGuess]
            incorrectGuess = incorrectGuess + 1

            if incorrectGuess == len(hangman_values):
                print()
                clean()
                print("\tGAME OVER!!!")
                print_hangman(hangman_values)
                print("The word is :", word.upper())
                break

        else:
            for i in range(len(word)):
                if word[i].upper() == val.upper():
                    displayOption[i] = val.upper()

            if check_win(displayOption):
                clean()
                print("\tCongratulations! ")
                print("The word is :", word.upper())
                break
        clean() 

def print_hangman(values):
    print()
    print("\t +--------+")
    print("\t |       | |")
    print("\t {}       | |".format(values[0]))
    print("\t{}{}{}      | |".format(values[1], values[2], values[3]))
    print("\t {}       | |".format(values[4]))
    print("\t{} {}      | |".format(values[5],values[6]))
    print("\t         | |")
    print("  _______________|_|___")
    print("  `````````````````````")
    print()

while True:
    print("---------------------")
    print("\tMENU")
    print("---------------------")

    print("Select an option")
    for index in options:
        print("Press", index , "for", options[index] )
    print("Press", len(options) + 1 , "to quit" )

    try:
        choice = int(input("Your choice is = "))
    except ValueError:
        clean()
        print("Wrong value, try again")
        continue

    if choice > len( options ) + 1:
        clean()
        print("That option doesn't exist")
        continue
    elif choice == len( options ) + 1 :
        print("Thank you for playing")
        break

    chosenOption = options[choice]

    randomWordSelected = random.choice(data[chosenOption])

    play(randomWordSelected)



