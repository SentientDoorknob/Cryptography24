import CryptographyTools as ct

ciphertext = input("Enter ciphertext here: ")

characters = ciphertext.split(" ")
plaintext = ""

morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '/': ' '
}


def decrypt_letter(character: str):
    try:
        character = morse_code_dict[character]
    except KeyError:
        print(f"Letter not Found: {character=}")
        character = "_"
    return character


for letter in characters:
    decrypted_letter = decrypt_letter(letter)
    plaintext += decrypted_letter

print(plaintext)
