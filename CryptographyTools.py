from DigramScores import digram_scores_dict
import itertools

ALPHABET = [chr(i) for i in range(65, 91)]
ALPHABET_DICT = dict(zip(ALPHABET, [0 for i in range(26)]))
DIGRAM_SCORES = digram_scores_dict

choose_2 = lambda x: x * (x - 1)

ENG_IC = 0.0667
RAND_IC = 0.0385

YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

englishFreq = {'E': 12.575645, 'T': 9.085226, 'A': 8.000395, 'O': 7.591270, 'I': 6.920007, 'N': 6.903785, 'S': 6.340880,
               'H': 6.236609, 'R': 5.959034, 'D': 4.317924, 'L': 4.057231, 'U': 2.841783, 'C': 2.575785, 'M': 2.560994,
               'F': 2.350463, 'W': 2.224893, 'G': 1.982677, 'Y': 1.900888, 'P': 1.795742, 'B': 1.535701, 'V': 0.981717,
               'K': 0.739906, 'X': 0.179556, 'J': 0.145188, 'Q': 0.117571, 'Z': 0.079130}

englishFreqDecimal = dict(E=0.12575645, T=0.09085226, A=0.08000395, O=0.07591270, I=0.06920007, N=0.06903785,
                          S=0.06340880, H=0.06236609, R=0.05959034, D=0.04317924, L=0.04057231, U=0.02841783,
                          C=0.02575785, M=0.02560994, F=0.02350463, W=0.02224893, G=0.01982677, Y=0.01900888,
                          P=0.01795742, B=0.01535701, V=0.00981717, K=0.00739906, X=0.00179556, J=0.00145188,
                          Q=0.00117571, Z=0.00079130)

root_key_dict = dict([(letter, letter) for letter in ALPHABET])


def dict_map(dictionary: dict, func) -> dict:
    return {k: func(v) for k, v in dictionary.items()}


def format_ciphertext(text) -> str:
    """Removes special characters and spaces from text."""
    text = filter(lambda x: x.isalpha(), text)
    return "".join(list(text)).upper()


def frequency(text, mode="") -> dict[str, int | float]:
    """Gives the frequency of each letter (with case) as a list."""
    length = len(text)
    output = ALPHABET_DICT.copy()
    for char in text:
        output[char] += 1

    match mode:
        case "%":
            return dict_map(output, lambda x: x / length * 100)
        case ".":
            return dict_map(output, lambda x: x / length)
        case _:
            return output


def sort_keys_by_value(dictionary, reverse=True) -> list:
    """Returns a list of keys, sorted by their values in given dictionary."""
    keys = sorted(dictionary.keys(), key=lambda key: dictionary[key], reverse=reverse)
    return keys


def shift_letter_by_value(char, amount, upper=True, positive=1) -> str:
    """Shift letter by amount in the alphabet. Cyclic."""
    caseShift = 64 if upper else 96
    index = ord(char) - caseShift
    out_alpha = (index + positive * amount) % 26
    if out_alpha == 0: out_alpha = 26
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


def interleave(*values):
    return list(itertools.chain(*zip(*values)))


def chi_squared_english(text: str) -> float:
    """Implementation of the chi^2 formula."""
    observed = frequency(text, ".")
    expected = englishFreqDecimal

    total = 0
    for letter in ALPHABET:
        term = ((observed[letter] - expected[letter]) ** 2) / expected[letter]
        total += term

    return total


def index_of_coincidence(text: str) -> float:
    """Implementation of the index of coincidence formula."""
    text_len = len(text)
    length_multiplier = 1 / choose_2(text_len)
    frequencies = frequency(text)

    sum = 0
    for letter, f in frequencies.items():
        sum += choose_2(f)
    return sum * length_multiplier


def shift_string_by_value(text, value: int, upper=True, positive=1):
    output = ""
    for letter in text:
        output += shift_letter_by_value(letter, value, upper, positive)
    return output


def shift_string_by_letter(text, char: str, upper=True, positive=1):
    caseshift = 65 if upper else 97
    return shift_string_by_value(text, ord(char) - caseshift, upper=upper, positive=positive)


def sort_tuples_by_element(iterable, index, mode="min"):
    return sorted(iterable, key=lambda x: x[index], reverse=(mode != "min"))


def substitute(text, key_dict):



class SubstitutionKey:
    def __init__(self, str_key):
        self.dict = {ALPHABET: str_key[i] for i in range(len(str_key))}
        self.str = str_key

    def update_str(self):
        self.str = "".join(self.dict.values())

    def update_dict(self):
        self.dict = {ALPHABET: self.str[i] for i in range(len(self.str))}

    def substitute(self, text):
        text = list(text)
        for i, letter in enumerate(text):
            text[i] = self.dict[letter]
        return "".join(text)
