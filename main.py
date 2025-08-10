import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")

my_dict = {x.letter : x.code for i,x in df.iterrows()}

word = input("Enter word: ")
phonetic_list = [my_dict[letter.upper()] for letter in word]
print(phonetic_list)