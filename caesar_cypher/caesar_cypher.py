alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    if encode_or_decode == "decode":
        shift_amount *= -1 

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            # If the shifted position is less than the length of the alphabet it remains the same.
            # But if the shifted position is greater than the length of the alphabet it gets the rest of the module.
            # Ex1: shifted_position = 21, the length of the alphabet is 26, so the shifted_position stays as 21.
            # Ex2: shifted_position = 28, the length of the alphabet is 26, so the shifted_position is 28-26 = 2.
            shifted_position %= len(alphabet)  # Garante que o índice fique dentro da lista
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == 'no':
        should_continue = False
        print('End.')

