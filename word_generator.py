from markov_dict import MarkovDict
import random

class WordGenerator:
    def __init__(self, addive_chances=True):
        self.addive_chances = addive_chances # when generator words, multiple dictionaries are combined to generate the next character. When addive changces is true then changes are always added, even if the combination of chacaters does not exist in both dictionaries. When this is false the combination must exist in both.
        self.dictionaries = []
        self.highest_lookback_amount = 0

    def add_dictionary(self, dictionary, weight=1):
        self.dictionaries.append((dictionary, weight))
        self.highest_lookback_amount = max(self.highest_lookback_amount, dictionary.lb)


    def generate_word(self):
        word = " " * self.highest_lookback_amount


        while True:
            chances_dict = None
            for markov_dict, weight in self.dictionaries:
                word_part = word[-markov_dict.lb:]
                row = markov_dict.data.get(word_part, {})
                if chances_dict is None:
                    chances_dict = row
                else:
                    chances_dict = self.__add_to_dict__(chances_dict, row, weight)

            next_char = random.choices(list(chances_dict.keys()), weights=list(chances_dict.values()))[0]
            if next_char == ' ':
                break

            word += next_char

        return word.strip()


    def __add_to_dict__(self, self_dict, other_dict, weight):
        if self.addive_chances:
            for key in other_dict.keys():
                if key in self_dict:
                    self_dict[key] += other_dict[key] * weight
                else:
                    self_dict[key] = other_dict[key] * weight
            return self_dict
        else:
            return dict([(k, self_dict.get(k) + weight*other_dict.get(k)) for k in set(self_dict) & set(other_dict)])