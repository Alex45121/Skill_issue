import re
import numpy as np

class __Computations:
    def __init__(self):
        
        pass


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
        idf = {}
        all_tokens = set(word for doc in docs for word in self.tokenizer(doc))

        for word in all_tokens:
            df = sum(1 for doc in docs if word in self.tokenizer(doc))
            idf[word] = float (np.log((N + 1)/(1 + df)) + 1)
        
        return idf
    
    def tfidf_computing(self, doc, docs):

        tf = self.tf_computing(doc)
        idf = self.idf_computing(docs)

        tfidf = {word: tf[word] * idf[word] for word in tf}

        return tfidf
    

    def normalizer(self, vector):
        norm = float (np.sqrt(sum(value**2 for value in vector.values())))
        return {word: value / norm for word, value in vector.items()} if norm != 0 else vector


class Personal_tfidf(__Computations):

    def __init__(self):
        pass

    def fit(self,doc):
        return self.tf_computing(doc)


    def transform(self,docs):
        return self.idf_computing(docs)

    def fit_transform(self,doc,docs):
        return self.tfidf_computing(doc,docs)
    
    def normalize(self,vector):
        return self.normalizer(vector)


docs = [
    "The movie was fantastic, I loved it!",
    "I hated the movie, it was awful!",
    "The movie was okay, not the best but not bad."
] 
doc1 = "The movie was fantastic, I loved it!"

opa = Personal_tfidf()
demo = opa.fit_transform(doc1,docs)
treno = opa.normalize(demo)

print(treno)





