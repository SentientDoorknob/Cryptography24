import CryptographyTools as ct

# Method: https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-IOC-Len.html

# text = input("Ciphertext: ")
ciphertext = ("DAZFI SFSPA VQLSN PXYSZ WXALC DAFGQ UISMT PHZGA MKTTF TCCFX KFCRG GLPFE TZMMM ZOZDE ADWVZ WMWKV GQSOH "
              "QSVHP WFKLS LEASE PWHMJ EGKPU RVSXJ XVBWV POSDE TEQTX OBZIK WCXLW NUOVJ MJCLL OEOFA ZENVM JILOW ZEKAZ "
              "EJAQD ILSWW ESGUG KTZGQ ZVRMN WTQSE OTKTK PBSTA MQVER MJEGL JQRTL GFJYG SPTZP GTACM OECBX SESCI YGUFP "
              "KVILL TWDKS ZODFW FWEAA PQTFS TQIRG MPMEL RYELH QSVWB AWMOS DELHM UZGPG YEKZU KWTAM ZJMLS EVJQT GLAWV "
              "OVVXH KWQIL IEUYS ZWXAH HUSZO GMUZQ CIMVZ UVWIF JJHPW VXFSE TZEDF")
ciphertext = ct.format_ciphertext(ciphertext)


def get_keyword_length(text: str, length_attempt: int):
    """Estimate keyword length. (Manual)"""
    pass

# -=-=-=-=-=-=-=-=-  Given tested keyword length.... -=-=-=-=-=-=-=-=-
# Method:

keyword_length = 5

print(ct.index_of_coincidence(ciphertext))

def decrypt_coset(coset: str) -> str:
    """Given one coset, solve like caesar cipher. (Manual?)"""
    pass


def get_keyword(text: str) -> str:
    """Returns the keyword found by coset search."""
    cosets = ct.split_cosets(text, keyword_length)
    pass




