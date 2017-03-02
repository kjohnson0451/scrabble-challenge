import argparse
import logging
from itertools import permutations
import bisect
import operator

def get_available_words(rack, dictionary_file):

  dictionary_list = [line.rstrip('\n') for line in dictionary_file]
  
  list_of_perms = [''.join(p) for p in permutations(rack)]
  list_of_available_words = []

  for perm in list_of_perms:
    indices_to_remove_temp = []
    indices_to_remove = []
    for index, word in enumerate(dictionary_list):
      if word in perm:
        list_of_available_words.append(word)
        indices_to_remove_temp.append(index)
    indices_to_remove = sorted(list(set(indices_to_remove_temp)), reverse=True)
    for index_to_remove in indices_to_remove:
      dictionary_list.pop(index_to_remove)

  return list_of_available_words

def get_words_vs_scores(list_of_available_words):

  scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
                        "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
                        "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
                        "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
                        "X": 8, "Z": 10}

  word_vs_score = {}

  for word in list_of_available_words:
    for c in word:
      if word not in word_vs_score:
        word_vs_score[word] = scores[c]
      else:
        word_vs_score[word] += scores[c]

  sorted_word_vs_score = sorted(word_vs_score.items(), key=operator.itemgetter(1), reverse=True)

  return sorted_word_vs_score

def main():
  
  try:
    DICTIONARY_FILE_PATH = "sowpods.txt"
    DICTIONARY_FILE = open(DICTIONARY_FILE_PATH)

    parser = argparse.ArgumentParser(description='Get scrabble rack.')
    parser.add_argument('rack', help='Letters on the scrabble rack')

    rack = parser.parse_args().rack.upper()
    if not rack.isalpha():
      raise ValueError('Rack does not exclusively contain letters');
    if len(rack) > 7:
      raise ValueError('Rack contains more than 7 letters');

    list_of_available_words = get_available_words(rack, DICTIONARY_FILE)    

    word_vs_score = get_words_vs_scores(list_of_available_words)
    
    print(word_vs_score)
    
  except IOError as e:
    logging.error(e)
  except ValueError as e:
    logging.error(e)
    
main()
