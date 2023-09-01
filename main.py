import pandas
from logo_art import logo


alphabet_data = pandas.read_csv("phonetic_alphabet.csv")

print(logo)
# TODO 1: Create a dictionary in the format of Leter as key and phonetic word as value
# Use list comprehension

phonetic_dict = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}

# TODO 2: Create a list of the phonetic code words from a word the user inputs

name_ = input("Enter a word: ").upper()


phonetic_list = [phonetic_dict[letter] for letter in name_]
print(phonetic_list)
