import re

class BoWReview_checker():
    def __init__(self):

        self.good_words = ["amazing", "good", "loved","fantastic"]
        self.bad_words = ["awful", "bad", "hated","disgusting"]
 

    def _text_analyzer(self, text):
        self.words = re.findall(r"\b\w+\b", text.lower())
        return self.words
    
    def _counter(self):
        index = 0
        self.new_dic = {}
        for token in self.words:
            if token not in self.words:
                self.new_dic[token] = index
                index += 1
        print (self.new_dic)


processor = BoWReview_checker()
print(processor._text_analyzer("The movie was fantastic, I loved it!"),processor._counter)

