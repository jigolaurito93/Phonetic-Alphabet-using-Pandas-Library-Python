import pandas

alphabet_data = pandas.read_csv("phonetic_alphabet.csv")


# TODO 1: Create a dictionary in the format of Leter as key and phonetic word as value
# Use list comprehension

phonetic_dict = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}

print(phonetic_dict)


# TODO 2: Create a list of the phonetic code words from a word the user inputs


