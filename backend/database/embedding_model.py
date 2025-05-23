from vector_database import VectorDB

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd


class EmbeddingModel:
    def __init__(self, model_tag = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_tag  = model_tag
        self.model = SentenceTransformer(model_tag)
        self.vectorDb = VectorDB()
        

    def encode(self, sentences):
        try:
            embeddings = []
            self.vectorDb.store_sentences(sentences)
            for sentence in sentences:
                embeddings.append(self.model.encode(sentence))
            embeddings = np.array(embeddings)
            self.vectorDb.store_embeddings(embeddings)
            # print(f"Encoded {len(sentences)} sentences. Shape: {self.embeddings.shape}, single embedding shape: {self.embeddings[0].shape}")
        except Exception as e:
            print(f'Error occured while encoding: {e}')
    
    def search_sentence(self, user_input):
        try:
            user_input_em = np.array(self.model.encode(user_input))
            # print(f'User embedding shape:{user_input_em.shape}')

            result = self.vectorDb.search_closest_sentence(user_input_em)
            print(f'Your Search Result: {result}')
        except Exception as e:
            print(f'Error occured while searching result: {e}')



# # Test code
# model = EmbeddingModel()
# sentenceList = [
#     "The quick brown fox jumps over the lazy dog.",
#     "Python is an amazing language for data science.",
#     "Learning new languages opens doors to different cultures.",
#     "Artificial intelligence is revolutionizing many industries.",
#     "Space exploration continues to inspire scientific discovery.",
#     "Reading books broadens one's knowledge and perspective.",
#     "The sun rises in the east and sets in the west.",
#     "In the digital age, technology is ever-changing.",
#     "Mathematics is the language of the universe.",
#     "Good health is the foundation of a fulfilling life.",
#     "Music has the power to evoke emotions and memories.",
#     "Coding is both challenging and rewarding.",
#     "The internet connects people from all corners of the globe.",
#     "The ocean covers more than 70% of the Earth's surface.",
#     "Success is the result of persistence and hard work.",
#     "Sustainable energy solutions are crucial for the future.",
#     "The beauty of nature is a constant source of inspiration.",
#     "Education is a powerful tool for personal and societal growth.",
#     "Innovation drives progress and shapes the future.",
#     "The more you learn, the more you realize how much you don't know."
# ]
# model.encode(sentenceList)
# user_input = "What is COding intelligence?"
# model.search_sentence(user_input)