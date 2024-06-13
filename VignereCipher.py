import CryptographyTools as ct

# Method: https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-IOC-Len.html

ciphertext = input("Ciphertext: ")
ciphertext = ct.format_ciphertext(ciphertext)

THRESHOLD = 0.01


def display_result(result: (int, float, float)):
    colour = ct.GREEN if result[2] < THRESHOLD else ct.RED
    print(colour)
    print(f"Keyword Length: {result[0]} \nAverage IoC: {result[1]} \nDifference from English IoC: {result[2]}")
    print(ct.RESET)


def try_length(text: str, length_attempt: int) -> (int, float, float):
    """Uses coset analysis (IoC) to determine likelihood of key length being correct."""
    columns = ct.split_cosets(text, length_attempt)

    sum = 0
    for coset in columns:
        sum += ct.index_of_coincidence(coset)
    average = sum / length_attempt
    return length_attempt, average, ct.ENG_IC - average


def get_keyword_length(text: str, max_try_length: int):
    """Estimate keyword length. (Manual)"""
    results = []
    for i in range(2, max_try_length + 1):
        results.append(try_length(text, i))

    for result in results:
        display_result(result)


get_keyword_length(ciphertext, 15)

# -=-=-=-=-=-=-=-=-  Given tested keyword length.... -=-=-=-=-=-=-=-=-
# Method:

keyword_length = int(input("Enter result (see above): "))

display_lowest = 1

# use keyword length of 1 for Caesar Cipher


def format_results(results):
    results = results[:display_lowest]

    for result in results:
        print(*result)
        print()
    print()


def decrypt_coset(coset: str):
    results = []
    for letter in ct.ALPHABET:
        shifted_coset = ct.shift_string_by_letter(coset, letter, positive=-1)
        chi_squared = ct.chi_squared_english(shifted_coset)
        results.append((letter, chi_squared, shifted_coset))
    sorted_results = ct.sort_tuples_by_element(results, 1)
    format_results(sorted_results)
    return sorted_results[0]


def get_keyword(text: str, k_length) -> str:
    """Returns the keyword found by coset search."""
    cosets = ct.split_cosets(text, k_length)
    keyword = ""
    likely_cosets = []

    for coset in cosets:
        result = decrypt_coset(coset)
        keyword += result[0]
        likely_cosets.append(list(result[2]))

    print("".join(ct.interleave(*likely_cosets)))
    print("\n")
    print(keyword)

example = ct.format_ciphertext(ciphertext)
get_keyword(example, keyword_length)


