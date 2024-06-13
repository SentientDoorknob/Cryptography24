import CryptographyTools as Ct
from CryptographyTools import SubstitutionKey


class SubstitutionDecoder:
    def __init__(self, moves=1):
        self.text = Ct.format_ciphertext(input("Enter Ciphertext: "))
        length = len(self.text)
        self.expected = Ct.dict_map(Ct.ENGLISH_FREQ_DECIMAL, lambda x: x * length)
        self.current_text = ""

        starting_key = Ct.get_key_guess(self.text)

        self.highest_c2 = Ct.chi_squared_english(self.text, self.expected)
        self.key = SubstitutionKey(starting_key)

        self.learn()

        self.moves = moves

    def __str__(self):
        return f"Key: {str(self.key)}\nChi^2: {self.highest_c2}\nText: {self.current_text}"

    def learn_iteration(self):
        proposed_key = self.key.__copy__()
        proposed_key.swap_random()

        proposed_text = proposed_key.substitute(self.text)
        proposed_c2 = Ct.chi_squared_english(proposed_text, self.expected)

        if self.highest_c2 > proposed_c2:
            self.highest_c2 = proposed_c2
            self.key = proposed_key
            self.current_text = proposed_text
            print("here")

            print(self)
            return input()
        return ""

    def learn(self):

        while True:
            response = self.learn_iteration()
            if response == "exit":
                break


decoder = SubstitutionDecoder(6)


