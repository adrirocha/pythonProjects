with open("../Input/Letters/starting_letter.txt", "r") as file:
    letter = file.read()
with open("../Input/Names/invited_names.txt", "r") as names:
    list_of_names = names.readlines()

for name in list_of_names:
    name = name.strip()
    with open(f"ReadyToSend/letter_for_{name}.docx", "w") as new_letter:
        copy_letter = letter.replace("[name]", name)
        new_letter.write(copy_letter)
