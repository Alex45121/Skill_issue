import re


class BoWReview_checker():
    def __init__(self):

        self.good_words = ["amazing", "good", "loved","fantastic","nice","liked"]
        self.bad_words = ["awful", "bad", "hated","disgusting", "didn'", "shit"]
        self.words = []
        self.new_dic = {}

 

    def _text_analyzer(self, text):
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Please use words!")
        self.words = re.findall(r"\b\w+\b", text.lower())
        return self.words
    
    def _counter(self):
    
        self.new_dic = {}
        for token in self.words:
            if token in self.new_dic:
                self.new_dic[token] += 1
            else:
                self.new_dic[token] = 1
                
        return self.new_dic
    
    def __calculator(self):
        good_count = 0
        bad_count = 0
        
        for keys, values in self.new_dic.items():
            if keys in self.good_words:
                good_count += values
                
            elif keys in self.bad_words:
                bad_count += values
        if good_count > bad_count:
            return True
        elif bad_count > good_count:
            return False
        else:
            return None
           
            
    def _assumption(self):
        result = self.__calculator()
        if result is True:
            print("The review was Positive")
        elif result is False:
            print("The review was Negative")
        else:
            print("The review was Neutral")

if __name__ =="__main__" :

    
    try:
        processor = BoWReview_checker()
        review = input("Leave your review here: ")
        processor._text_analyzer(review)
        print(processor._counter())
        print(processor._assumption())
    except ValueError as e:
        print(f"Unexpected error {e}")








