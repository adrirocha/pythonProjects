import pandas

pd_nato_phonetic_alphabet = pandas.DataFrame(pandas.read_csv("nato_phonetic_alphabet.csv"))
phonetic_dict = {row["letter"]:row["code"] for (index, row) in pd_nato_phonetic_alphabet.iterrows()}

def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        list_phonetic_code_words = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(list_phonetic_code_words)

generate_phonetic()
