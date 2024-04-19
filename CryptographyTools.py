import string;

def formatCiphertext(text):
    text = filter(lambda x: x.isalpha(), text);
    return "".join(text);