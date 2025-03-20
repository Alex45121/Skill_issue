import re
import numpy as np

class __Computations:
    def __init__(self):
        self.idf = {}
        self.vocab = set()
        self.is_fitted = False 


    def tokenizer(self,text):
        #instead of Counter function I am making my own.
        return re.findall(r"\b\w+\b", text.lower())
    
    def tf_computing(self,doc):
        #tf - Term Frequency computing using the formula: amount of times a word appears in the dictionary divided by the total length of the dictionary

        words = self.tokenizer(doc)
        word_counter = len(words)
        tf = {}

        for word in words:
            #this computes between the given words and counts how many times are they appearing

            tf[word] = tf.get(word,0) + 1


        for word in tf:
            #here it divides by the total document size to find the frequency

            tf[word] /= word_counter

        return tf
    
    def idf_computing(self, docs):
        N = len(docs)
        all_tokens = set(word for doc in docs for word in self.tokenizer(doc))
        self.vocab = all_tokens

        for word in all_tokens:
            df = sum(1 for doc in docs if word in self.tokenizer(doc))
            self.idf[word] = float (np.log((N + 1)/(1 + df)) + 1)
        
        self.is_fitted = True
        return self.idf
    
    def tfidf_computing(self, doc):

        if not self.is_fitted:
            raise KeyError("First compile document library to continue")

        tf = self.tf_computing(doc)

        tfidf = {word: tf[word] * self.idf.get(word, 1.0) for word in tf}

        return tfidf
    

    def normalizer(self, vector):
        norm = float (np.sqrt(sum(value**2 for value in vector.values())))
        return {word: value / norm for word, value in vector.items()} if norm != 0 else vector


class Document_analyzer(__Computations):

    def __init__(self, corpus):
        super().__init__()
        self.corpus = corpus
        self.positive_words = ["delicious", "excellent", "amazing", "friendly", "cozy", "recommended"]
        self.negative_words = ["worst", "bland", "terrible", "overpriced", "cold", "atrocious"]
        self.library = self.idf_computing(self.corpus)

    def analyze_statement(self,review):

        tfidf_vectors = self.tfidf_computing(review)
        tfidf_normal = self.normalizer(tfidf_vectors)

        positive_values = sum(tfidf_normal.get(word, 0) *  self.idf.get(word, 1) for word in self.positive_words)
        negative_values = sum(tfidf_normal.get(word, 0) * self.idf.get(word, 1) for word in self.negative_words)

        if positive_values > negative_values:
            return True
        elif negative_values > positive_values:
            return False
        else:
            return None










