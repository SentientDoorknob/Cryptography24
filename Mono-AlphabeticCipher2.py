import CryptographyTools as Ct
from CryptographyTools import SubstitutionKey


class SubstitutionDecoder:
    def __init__(self, moves = 1):
        self.text = Ct.format_ciphertext(input("Enter Ciphertext: "))
        self.current_text = ""

        starting_key = Ct.get_key_guess(self.text)

        self.highest_c2 = Ct.chi_squared_english(self.text)
        self.key = SubstitutionKey(Ct.ALPHABET_STR)

        self.learn()

        self.moves = moves

    def __str__(self):
        return f"Key: {str(self.key)}\nChi^2: {self.highest_c2}\nText: {self.current_text}"

    def learn(self):
        proposed_key = self.key
        proposed_key.swap_random()

        proposed_text = proposed_key.substitute(self.text)
        proposed_c2 = Ct.chi_squared_english(proposed_text)

        if self.highest_c2 > proposed_c2:
            self.highest_c2 = proposed_c2
            self.key = proposed_key
            self.current_text = proposed_text

            print(self)
            input()
        self.learn()


decoder = SubstitutionDecoder(2)


