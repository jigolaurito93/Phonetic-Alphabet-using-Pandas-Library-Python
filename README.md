# Phonetic-Alphabet-using-Pandas-Library-Python

I developed a program that asks for a user input and subsequently presents the associated NATO phonetic word for each letter in the provided word, storing the results in an array.

To implement this, I utilized the pandas library and employed the technique of list comprehension for my code.

The phonetic alphabet was originally stored in a csv file with the alphabet letter and the corresponding NATO phonetic value

I transformed the CSV file into a DataFrame using the Pandas Library and applied list comprehension to convert the DataFrame into a dictionary.

To access the values in each row, I utilized the iterrows() function.

The program begins by requesting a word for conversion. I iterated through each letter in the word, converting it into its corresponding phonetic word, and stored it within an array.

In addition, I incorporated ASCII art from www.patorjk.com, which displays the phrase "NATO PHONETIC ALPHABET." I saved this art in a separate Python file and imported it into my main.py file.

Although this is a simple and straightforward program, I aimed to demonstrate the significance of my skills in list comprehension and the Panda Library, which I honed during my bootcamp experience.
