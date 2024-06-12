import CryptographyTools as ct
import random

DIFFERENCE_THRESHOLD = 0.01

ciphertext = input("Enter Ciphertext: ")
ciphertext = ct.format_ciphertext(ciphertext)

IoC = ct.index_of_coincidence(ciphertext)
IoC_difference = ct.ENG_IC - IoC

if abs(IoC_difference) < DIFFERENCE_THRESHOLD:
    print(ct.GREEN)
    print(f"Index of Coincidence is: {IoC}; You're good to go!")
else:
    print(ct.RED)
    print(f"Warning: Index of Coincidence is: {IoC}; This is likely not a Mono-Alphabetic Substitution cipher. difference = {IoC_difference}")

    proceed = input("(Y / N) Are you sure you want to proceed? ")
    if proceed.upper() == "N":
        print("Exiting...")
        exit()

print(ct.RESET)
print()

current_key = ct.root_key_dict
current_chi_squared = ct.chi_squared_english(ciphertext)
moves = 3


def change_key(key, swaps):
    for i in range(swaps):
        a = random.choice(ct.ALPHABET)
        b = random.choice(ct.ALPHABET)

        temp = key[a]
        key[a] = key[b]
        key[b] = temp

    return key


def learn():
    prop_key = change_key(current_key, moves)
    prop_text = ct.substitute(ciphertext, prop_key)

    prop_c2 = ct.chi_squared_english(prop_text)

    if prop_c2 < current_chi_squared:
        print(prop_text)
        return prop_c2, prop_key
    else:
        print(prop_text)
        return current_chi_squared, current_key


while True:
    current_chi_squared, current_key = learn()
    input()

