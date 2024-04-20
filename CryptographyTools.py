import string;

ALPHABET = [chr(i) for i in range(65, 91)]
ALPHABET_DICT = dict(zip(ALPHABET, [0 for i in range(26)]))

englishFreq = {'E': 12.575645, 'T': 9.085226, 'A': 8.000395, 'O': 7.591270, 'I': 6.920007, 'N': 6.903785, 'S': 6.340880, 'H': 6.236609, 'R': 5.959034, 'D': 4.317924, 'L': 4.057231, 'U': 2.841783, 'C': 2.575785, 'M': 2.560994, 'F': 2.350463, 'W': 2.224893, 'G': 1.982677, 'Y': 1.900888, 'P': 1.795742, 'B': 1.535701, 'V': 0.981717, 'K': 0.739906, 'X': 0.179556, 'J': 0.145188, 'Q': 0.117571, 'Z': 0.079130}

def formatCiphertext(text):
    text = filter(lambda x: x.isalpha(), text);
    return "".join(list(text)).upper();

def frequency(text, percentage = True):
    output = ALPHABET_DICT;
    for char in text:
        output[char] += 1
    if percentage:
        for key in output:
            output[key] = output[key] / len(text) * 100;
    return output

def sortKeysByValue(dictionary, reverse=True):
    keys = sorted(dictionary.keys(), key=lambda key: dictionary[key], reverse=reverse)
    return keys;

def shiftLetterByValue(c, value, upper=True, positive=-1):
    caseShift = 64 if upper else 96
    index = ord(c) - caseShift;
    outalpha = (index + positive * value) % 26;
    output = outalpha + caseShift;
    return chr(output)