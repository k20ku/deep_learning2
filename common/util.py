import numpy as np


def preprocess(text: str):
    words = text.lower().replace('.', ' .').split(' ')

    word_to_id: dict[str, int] = {}
    id_to_word: dict[int, str] = {}
    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)  # インデックス
            word_to_id[word] = new_id
            id_to_word[new_id] = word

    corpus = np.array([word_to_id[w] for w in words])

    return corpus, word_to_id, id_to_word
