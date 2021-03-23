from translate import Translator

def punctuation_removal(data_string):
    """ 
        This function takes a string as input and returns a string without punctuations 
        (mainly comma, fullstop and question mark).
        This is implemented by the string function: .replace() 
        More punctuations can be added to the list, or a regex of punctuations can be used.
    """
    punctuations = [",", ".", "?", "!"]
    for punc in punctuations:
        data_string = data_string.replace(punc, "")
    return data_string

def stopword_removal(tokens):
    """
        This function takes a list of words, or tokens as input and returns only those words that are not stopwords. 
        It removes the commonly used words in english that are used to make a sentence grammatically correct, 
        without adding much meaning to a sentence. 
        More stopwords can be added to the list. 
    """
   
    stopwords = ['i', 'am', 'this', 'is', 'a', 'was', 'it', 'the', 'do', 'you', 'by']
    
    #implementation without list comprehension:
    # filtered_tokens = []
    # for token in tokens:
    #     if token not in stopwords:
    #         filtered_tokens.append(token)
    
    #implementation with list comprehension
    return [token for token in tokens if token not in stopwords]
    
def stemming(filtered_tokens):
    """
        This function takes a list of filtered tokens as input, and returns the base form or root word of the tokens. 
        This helps in normalising the words in our data/corpus.
    """
    root_to_token = {'come': ['came', 'coming', 'comes'], 
                    'know': ['know', 'knowing', 'knows'], 
                    'good': ['good', 'better', 'best'], 
                    'place': ['place', 'places', 'placed'], 
                    'nearby': ['nearby'],
                    'like': ['liked']
    }
    base_form_tokens = []
    for token in filtered_tokens:
        for base_form, token_list in root_to_token.items():
            if token in token_list:
                base_form_tokens.append(base_form)
            else:
                base_form_tokens.append(token)
    return base_form_tokens
    
# task 1: Read the Review Content from File and extract only reviews
fh = open('reviews.txt', 'r')
reviews = []
for line in fh.readlines():
    reviews.append(line.split('|')[1])

# task 2: Tokenize each words and create a word frequency dictionary
word_freqs = {}
tokens = []
for review in reviews:
    review_words = review.lower().split()
    for word in review_words:
        clean_word =  punctuation_removal(word)
        tokens.append(clean_word)
for token in tokens:
    word_freqs[token] = word_freqs.get(token, 0) + 1

# task 3: Remove stop words and duplicate words. Find translated word and store as tuple in new file. 
tokens = set(tokens)
filtered_tokens = stopword_removal(tokens)
base_tokens = stemming(filtered_tokens)

translate = Translator(to_lang = 'hi') 
out_fh = open('output_file.txt', 'a')
for token in base_tokens:
    translation = translate.translate(token)
    tup = (token, translation)
    out_fh.write(tup + "\n")
out_fh.close()

disp = open('output_file.txt')
for line in disp.read():
    print(line)
