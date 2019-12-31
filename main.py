import json
from markov_dict import MarkovDict
from word_generator import WordGenerator

def main():
    word_generator = WordGenerator(False)

    for i in range(1, 4):
        markov_dict = MarkovDict(lookback_amount=i, lookahead_amount=1)
        markov_dict.process_file("lorem_ipsum.txt")
        markov_dict.save_to_file(f"./dicts/lorem_ipsum_{i}.markov")

        word_generator.add_dictionary(markov_dict, weight=4-i)

    sentence = ""
    for i in range(5):
        sentence += " " + word_generator.generate_word()

    print(sentence)




if __name__ == '__main__':
    main()