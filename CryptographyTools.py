import string;

ALPHABET = [chr(i) for i in range(65, 91)]
ALPHABET_DICT = dict(zip(ALPHABET, [0 for i in range(26)]))

data = {'e': 12.575645,'t': 9.085226,'a': 8.000395,'o': 7.591270,'i': 6.920007,'n': 6.903785,'s': 6.340880,'h': 6.236609,'r': 5.959034,'d': 4.317924,'l': 4.057231,'u': 2.841783,'c': 2.575785,'m': 2.560994,'f': 2.350463,'w': 2.224893,'g': 1.982677,'y': 1.900888,'p': 1.795742,'b': 1.535701,'v': 0.981717,'k': 0.739906,'x': 0.179556,'j': 0.145188,'q': 0.117571,'z': 0.079130}

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