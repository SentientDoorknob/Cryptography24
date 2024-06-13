import CryptographyTools as ct

text = ct.format_ciphertext(input("Enter Ciphertext: "))

key = ct.get_key_guess(text)
print(key)
key_ord = list(map(lambda x: ord(x) - 65, key))

alphabet_ord = range(0, 26)

print(key_ord)

for i in alphabet_ord:
    print(i)

print()

for i in key_ord:
    print(i)



