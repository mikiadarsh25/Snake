import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phenotic_dict = {row.letter :row.code for (index, row) in data.iterrows()}

word = input("Enter a Word: ").upper()
output_list = [phenotic_dict[letter] for letter in word]
print(output_list)
