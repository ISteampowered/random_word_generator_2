import json

class MarkovDict:
    def __init__(self, lookback_amount=1, lookahead_amount=1):
        self.data = {}
        self.lb = lookback_amount
        self.la = lookahead_amount

    def process_file(self, file_name):
        with open(file_name) as file:
            for line in file:
                line = line.strip()
                for word in line.split(" "):
                    self.process_word(word)


    def process_word(self, word):

        word = " " * (self.lb-1) + f" {word.lower()} "

        for i in range(self.lb, len(word)-self.la+1):
            self.add(word[i-self.lb:i], word[i:i+self.la])

    def add(self, current, next_v):
        row = self.data.get(current, {})
        row[next_v] = row.get(next_v, 0) + 1
        self.data[current] = row 

    def save_to_file(self, file_out):
        with open(file_out, 'w') as output_file:
            json.dump(
                {"data":self.data, "lookahead_amount": self.la, "lookback_amount": self.lb}, 
                output_file, 
                sort_keys=True, 
                indent=4
                )

    def load_from_file(self, file_in):
        with open(file_in, 'r') as fileN:
            jsonData = json.loads(fileN)
            self.data = jsonData["data"]
            self.lb = jsonData["lookback_amount"]
            self.la = jsonData["lookahead_amount"]