import CryptographyTools as ct;
from statistics import mode

#text = input("Ciphertext: ")
text = "Adhz iypsspn, huk aol zspaof avclzKpk nfyl huk nptisl pu aol dhil:Hss tptzf dlyl aol ivyvnvclz,Huk aol tvtl yhaoz vbanyhil.Ildhyl aol Qhiilydvjr, tf zvu!Aol qhdz aoha ipal, aol jshdz aoha jhajo!Ildhyl aol Qbiqbi ipyk, huk zobuAol mybtpvbz Ihuklyzuhajo! "
text = ct.formatCiphertext(text);

accuracyRange = 26

cipherFreq = ct.frequency(text);
englishFreq = ct.englishFreq;

sortedKeys = ct.sortKeysByValue(cipherFreq);
engSortedKeys = ct.sortKeysByValue(englishFreq);

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
    outchar = ct.shiftLetterByValue(char, key, upper=char.isupper())
    plaintext += outchar

print(plaintext)