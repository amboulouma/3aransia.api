BASE_DIR = './api'
DATA_DIR = '/data'

CONTROLLED_DICTIONARY = '/controlled_dictionary.csv'
OPEN_DICTIONARY = '/open_dictionary.csv'
DICTIONARY_SAMPLE = '/dictionary_sample.csv'
MOROCCAN_ALPHABET = '/moroccan_alphabet.csv'

UPPER_ENGLISH_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
LOWER_ENGLISH_ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

UPPER_ENGLISH_VOWELS = ['A', 'E', 'I', 'O', 'U', 'Y']
UPPER_ENGLISH_CONSONS = list(set(UPPER_ENGLISH_ALPHABET) - set(UPPER_ENGLISH_VOWELS))

LOWER_ENGLISH_VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
LOWER_ENGLISH_CONSONS = list(set(LOWER_ENGLISH_ALPHABET) - set(LOWER_ENGLISH_VOWELS))

NUMBERS = '0123456789'

DOUBLE_MOROCCAN_LETTERS = ['la', 'kh', 'sh', 'ou', 'gh']
MOROCCAN_ENDING_LETTERS = ['d', 'a', 'o', 'w', 'r', 'z', 'u']

DUPLICATE_MOROCCAN_LETTERS = ['aa', 'bb', 'cc','dd','ee','ff','gg','hh','ii','iy','jj', 
    'kk', 'll', 'mm','nn','oo','pp', 'qq', '77', '22', '55', '99', 'rr', 'ss', 'tt','uu','ww','xx', 'yi', 'yy','zz']

WORD_NOT_FOUND_ERROR = { 'error_message': {
                            'message': 'Word not found', 
                            }
                        }