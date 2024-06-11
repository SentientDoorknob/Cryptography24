import CryptographyTools as ct

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

key = ct.root_key_dict
current_chi_squared = ct.chi_squared_english(ciphertext)
moves = 1


def learn():
    pass


learn()

