import CryptographyTools as ct;
from statistics import mode

#text = input("Ciphertext: ")
text = "Adhz iypsspn, huk aol zspaof avclzKpk nfyl huk nptisl pu aol dhil:Hss tptzf dlyl aol ivyvnvclz,Huk aol tvtl yhaoz vbanyhil.Ildhyl aol Qhiilydvjr, tf zvu!Aol qhdz aoha ipal, aol jshdz aoha jhajo!Ildhyl aol Qbiqbi ipyk, huk zobuAol mybtpvbz Ihuklyzuhajo! "
text = ct.format_ciphertext(text);

accuracyRange = 26

cipherFreq = ct.frequency(text);
englishFreq = ct.ENGLISH_FREQ;

sortedKeys = ct.sort_keys_by_value(cipherFreq);
engSortedKeys = ct.sort_keys_by_value(englishFreq);

differences = []
for i in range(accuracyRange):
    diff = ord(sortedKeys[i]) - ord(engSortedKeys[i])
    if diff < 0:
        diff += 26
    differences.append(diff)

key = mode(differences)

print(key)

plaintext = ""
for char in text:
    outchar = ct.shift_letter_by_value(char, key, upper=char.isupper())
    plaintext += outchar

print(plaintext)