
import pandas
df = pandas.read_csv('Intermediate days\\day26\\nato_phonetic_alphabet.csv')
df = pandas.DataFrame(df)

#TODO 1. Create a dictionary in this format:
alphabet = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("digite seu nome").upper()

phonetic_code = [alphabet[i] for i in word if i in alphabet]
print(phonetic_code)