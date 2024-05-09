import CryptographyTools as ct

# Method: https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-IOC-Len.html

# text = input("Ciphertext: ")
ciphertext = ("")
ciphertext = ct.format_ciphertext(ciphertext)


def get_keyword_length(text: str, length_attempt: int):
    """Estimate keyword length. (Manual)"""
    pass

# -=-=-=-=-=-=-=-=-  Given tested keyword length.... -=-=-=-=-=-=-=-=-
# Method:

keyword_length = 5


def decrypt_coset(coset: str) -> str:
    """Given one coset, solve like caesar cipher. (Manual?)"""
    pass


def get_keyword(text: str) -> str:
    """Returns the keyword found by coset search."""
    cosets = ct.split_cosets(text, keyword_length)
    pass




