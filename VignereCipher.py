import CryptographyTools as ct

# Method: https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-IOC-Len.html

# text = input("Ciphertext: ")
ciphertext = ("DAZFI SFSPA VQLSN PXYSZ WXALC DAFGQ UISMT PHZGA MKTTF TCCFX KFCRG GLPFE TZMMM ZOZDE ADWVZ WMWKV GQSOH "
              "QSVHP WFKLS LEASE PWHMJ EGKPU RVSXJ XVBWV POSDE TEQTX OBZIK WCXLW NUOVJ MJCLL OEOFA ZENVM JILOW ZEKAZ "
              "EJAQD ILSWW ESGUG KTZGQ ZVRMN WTQSE OTKTK PBSTA MQVER MJEGL JQRTL GFJYG SPTZP GTACM OECBX SESCI YGUFP "
              "KVILL TWDKS ZODFW FWEAA PQTFS TQIRG MPMEL RYELH QSVWB AWMOS DELHM UZGPG YEKZU KWTAM ZJMLS EVJQT GLAWV "
              "OVVXH KWQIL IEUYS ZWXAH HUSZO GMUZQ CIMVZ UVWIF JJHPW VXFSE TZEDF")
ciphertext = ct.format_ciphertext(ciphertext)

THRESHOLD = 0.01


def display_result(result: (int, float, float)):
    colour = ct.GREEN if result[2] < THRESHOLD else ct.RED
    print(colour)
    print(f"Keyword Length: {result[0]} \nAverage IoC: {result[1]} \nDifference from English IoC: {result[2]}")


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

# keyword_length = input("Enter estimate (see above): ")
keyword_length = 14

print(ct.shift_string_by_letter("ABCDEFGHIJKLMNOP", "D"))

def decrypt_coset(coset: str) -> str:
    """Given one coset, solve like caesar cipher. (Manual?)"""
    pass


def get_keyword(text: str) -> str:
    """Returns the keyword found by coset search."""
    cosets = ct.split_cosets(text, keyword_length)
    pass




