import pytest

from core.core import compute_similarity, sentences_similarities




def test_compute_similarity():
    word1 = 'concentration'
    word2 = 'attention'

    expected  = 0.5427157878875732
    actual = compute_similarity(word1, word2)
    assert actual == expected


def test_sentences_similarities():
    corpus = ["I'd like an apple",
           "An apple a day keeps the doctor away",
           "Never compare an apple to an orange",
           "I prefer scikit-learn to Orange",
           "The scikit-learn docs are Orange and Blue"]

    expected  = [[0.9999999999999998, 0.17668795478716204, 0.27056873300683837, 0.0, 0.0], [0.17668795478716204, 0.9999999999999999, 0.1543943648960287, 0.0, 0.0], [0.27056873300683837, 0.1543943648960287, 1.0, 0.1963564882520361, 0.16815247007633355], [0.0, 0.0, 0.1963564882520361, 0.9999999999999999, 0.5449975578692606], [0.0, 0.0, 0.16815247007633355, 0.5449975578692606, 1.0]]
    actual = sentences_similarities(corpus)
    assert actual == expected