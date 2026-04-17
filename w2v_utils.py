
import numpy as np


def read_glove_vecs(glove_file):
    '''
    Reads the glove vectors from a glove file and returns:
    
    - words_to_index: a dictionary mapping words to their indices in the glove vector list
    - index_to_words: a dictionary mapping indices to their corresponding words in the glove vector list
    - word_to_vec_map: a dictionary mapping words to their glove vector representation
    '''
    words = set()
    word_to_vec_map = {}
    with open(glove_file, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip().split()
            if not line:
                continue
            curr_word = line[0]
            words.add(curr_word)
            word_to_vec_map[curr_word] = np.array(line[1:], dtype=np.float64)
    return words, word_to_vec_map
      




