import os
from typing import List
import numpy as np
from gensim.models import KeyedVectors
from sklearn.feature_extraction.text import TfidfVectorizer



MODEL = KeyedVectors.load_word2vec_format(os.environ["MODEL_FILE"])


# main function
def compute_similarity(word1: str, word2: str) -> float:
    vec_1 = MODEL[word1]
    vec_2 = MODEL[word2]
    cosine_similarity = np.dot(vec_1, vec_2)/(np.linalg.norm(vec_1) * np.linalg.norm(vec_2))
    return cosine_similarity


# main function
def sentences_similarities(corpus: List[str]) -> List[List[float]]:
    vectorizer = TfidfVectorizer(min_df=1, stop_words="english")
    tfidf = vectorizer.fit_transform(corpus)
    pairwise_similarity = tfidf * tfidf.T
    return pairwise_similarity.toarray().tolist()


