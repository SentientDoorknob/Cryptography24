import CryptographyTools as ct

# Method: https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-IOC-Len.html

# text = input("Ciphertext: ")
ciphertext = ('DAZFI SFSPA VQLSN PXYSZ WXALC DAFGQ UISMT PHZGA MKTTF TCCFX KFCRG GLPFE TZMMM ZOZDE ADWVZ WMWKV GQSOH '
              'QSVHP WFKLS LEASE PWHMJ EGKPU RVSXJ XVBWV POSDE TEQTX OBZIK WCXLW NUOVJ MJCLL OEOFA ZENVM JILOW ZEKAZ '
              'EJAQD ILSWW ESGUG KTZGQ ZVRMN WTQSE OTKTK PBSTA MQVER MJEGL JQRTL GFJYG SPTZP GTACM OECBX SESCI YGUFP '
              'KVILL TWDKS ZODFW FWEAA PQTFS TQIRG MPMEL RYELH QSVWB AWMOS DELHM UZGPG YEKZU KWTAM ZJMLS EVJQT GLAWV '
              'OVVXH KWQIL IEUYS ZWXAH HUSZO GMUZQ CIMVZ UVWIF JJHPW VXFSE TZEDF')
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

# keyword_length = input("Enter result (see above): ")
keyword_length = 14

# use keyword length of 1 for Caesar Cipher


def decrypt_coset(coset: str) -> str:
    for letter in ct.ALPHABET:
        shifted_coset = ct.shift_string_by_letter(coset, letter)
        print(shifted_coset)
        chi_squared = ct.chi_squared_english(shifted_coset)
        print(letter, chi_squared)


def get_keyword(text: str) -> str:
    """Returns the keyword found by coset search."""
    cosets = ct.split_cosets(text, keyword_length)
    pass

example = "F IFSB FK X ELRPB KBXO QEB JLRKQXFKP. F EXSB QTL YOLQEBOP XKA LKB PFPQBO, XKA F TXP YLOK IXPQ. JV CXQEBO QBXZEBP JXQEBJXQFZP, XKA JV JLQEBO FP X KROPB XQ X YFD ELPMFQXI. JV YOLQEBOP XOB SBOV PJXOQ XKA TLOH EXOA FK PZELLI. JV PFPQBO FP X KBOSLRP DFOI, YRQ PEB FP SBOV HFKA. JV DOXKAJLQEBO XIPL IFSBP TFQE RP. PEB ZXJB COLJ FQXIV TEBK F TXP QTL VBXOP LIA. PEB EXP DOLTK LIA, YRQ PEB FP PQFII SBOV PQOLKD. PEB ZLLHP QEB YBPQ CLLA!"

example = ct.format_ciphertext(example)
print(example)

for letter in ct.ALPHABET:
    print(ct.shift_string_by_letter("".join(ct.ALPHABET), letter))

# decrypt_coset(example)

