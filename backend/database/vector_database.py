import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class VectorDB:
    def __init__(self):
        self.df = pd.DataFrame()
        self.sentences_length = 0

    def store_sentences(self, sentences):
        try:
            self.df['sentence'] = sentences
            self.sentecnes_length = len(sentences)
        except Exception as e:
            raise Exception(f'Error occured while storing sentence in database: {e}')
    
    def store_embeddings(self, embeddings):
        try:
            self.df['embedding'] = list(embeddings)
        except Exception as e:
            raise Exception(f'Error occured while storing embedding in database: {e}')
            

    def search_closest_sentence(self, user_input_em):
        try:
            cosine_similarities = cosine_similarity(user_input_em.reshape(1,-1), np.vstack(self.df['embedding'].values).reshape(self.sentecnes_length,-1))
            most_similar_idx = np.argmax(cosine_similarities)
            most_similar_sentence = self.df.iloc[most_similar_idx]["sentence"]
            return most_similar_sentence
        except Exception as e:
            raise Exception(f'Error occured while searching closest sentence in database: {e}')
