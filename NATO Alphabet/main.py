import pandas

pd_nato_phonetic_alphabet = pandas.DataFrame(pandas.read_csv("nato_phonetic_alphabet.csv"))
phonetic_dict = {row["letter"]:row["code"] for (index, row) in pd_nato_phonetic_alphabet.iterrows()}

user_word = input("Enter a word: ").upper()
list_phonetic_code_words = [phonetic_dict[letter] for letter in user_word]
print(list_phonetic_code_words)
