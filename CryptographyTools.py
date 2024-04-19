import string;

ALPHABET = [chr(i) for i in range(65, 91)]
ALPHABET_DICT = dict(zip(ALPHABET, [0 for i in range(26)]))

def formatCiphertext(text):
    text = filter(lambda x: x.isalpha(), text);
    return "".join(text).upper;