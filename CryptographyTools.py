from DigramScores import digram_scores_dict

ALPHABET = [chr(i) for i in range(65, 91)]
ALPHABET_DICT = dict(zip(ALPHABET, [0 for i in range(26)]))
DIGRAM_SCORES = digram_scores_dict

englishFreq = {'E': 12.575645, 'T': 9.085226, 'A': 8.000395, 'O': 7.591270, 'I': 6.920007, 'N': 6.903785, 'S': 6.340880,
               'H': 6.236609, 'R': 5.959034, 'D': 4.317924, 'L': 4.057231, 'U': 2.841783, 'C': 2.575785, 'M': 2.560994,
               'F': 2.350463, 'W': 2.224893, 'G': 1.982677, 'Y': 1.900888, 'P': 1.795742, 'B': 1.535701, 'V': 0.981717,
               'K': 0.739906, 'X': 0.179556, 'J': 0.145188, 'Q': 0.117571, 'Z': 0.079130}


def format_ciphertext(text) -> str:
    """Removes special characters and spaces from text."""
    text = filter(lambda x: x.isalpha(), text)
    return "".join(list(text)).upper()


def frequency(text, percentage=True) -> dict[str, int]:
    """Gives the frequency of each letter (with case) as a list. Percentage by default."""
    output = ALPHABET_DICT
    for char in text:
        output[char] += 1
    if percentage:
        for key in output:
            output[key] = output[key] / len(text) * 100
    return output


def sort_keys_by_value(dictionary, reverse=True) -> list:
    """Returns a list of keys, sorted by their values in given dictionary."""
    keys = sorted(dictionary.keys(), key=lambda key: dictionary[key], reverse=reverse)
    return keys


def shift_letter_by_value(char, amount, upper=True, positive=-1) -> str:
    """Shift letter by amount in the alphabet. Cyclic."""
    caseShift = 64 if upper else 96
    index = ord(char) - caseShift
    out_alpha = (index + positive * amount) % 26
    output = out_alpha + caseShift
    return chr(output)


def split_cosets(text, key_length) -> list[str | list]:
    """Splits a string into cosets mod key_length."""
    output = [[] for i in range(0, key_length)]

    pos = 0
    for char in text:
        output[pos % key_length].append(char)
        pos += 1

    for i in range(0, len(output)):
        output[i] = "".join(output[i])

    return output


def trim_to_shared_size(str1: str, str2: str) -> (str, str, int):
    """Returns 2 strings trimmed to the maximum size they share."""
    size = min(len(str1), len(str2))
    return str1[:size], str2[:size], size


def average_list(iterable: list) -> float:
    print(iterable)
    int_list = [i for i in iterable if isinstance(i, float)]
    print(int_list)
    return sum(int_list) / len(int_list)


def unpack_list_list(nested_list: list[list]) -> list:
    return [item for sublist in nested_list for item in sublist]








