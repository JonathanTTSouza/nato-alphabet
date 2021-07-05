#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas
nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_csv.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    try:
        word = input("What's the word you want to convert to NATO?: ").upper()
        nato_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters allowed")
    else:
        print(nato_word)
        break

