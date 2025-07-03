import numpy as np


def preprocess(text: str):
    """preprocesser

    preprocess text to corpus

    Args:
        コーパス化する改行なしの一文: str

    Returns:
        (単語IDのndarray, 単語から単語IDへのdict, 単語IDから単語へのdict)

        For example:

        >>> text = "You say goodbye and I say hello."

        >>> corpus, word_to_id, id_to_word = preprocess(text)

        >>> corpus
        array([0, 1, 2, 3, 4, 1, 5, 6])

        >>> word_to_id
        {'you': 0, 'say': 1, 'goodbye': 2, 'and': 3,
        'i': 4, 'hello': 5, '.': 6}
        
        >>> id_to_word
        {0: 'you', 1: 'say', 2: 'goodbye', 3: 'and',
        4: 'i', 5: 'hello', 6: '.'}

    """
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
