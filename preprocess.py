import pandas as pd


"""
These methods are used to clear the sentences from the input file and do preproccesing for the parts.
"""


"""
Convert the sentence in lowercase

@ param string sentence     sentence

@ returns the sentence in lower case
"""
def lowercase(sentence):
    return str(sentence).lower()


"""
Remove the numbers from the sentence

@ param string sentence     sentence

@ return the sentence without numbers
"""
def remove_numbers(sentence):
    import re
    return re.sub(r'\d +', "", sentence)


"""

@ param string sentence     sentence

@ return the sentence without punctuation
"""
def remove_punctuation(sentence):
    from string import punctuation
    return ''.join(c for c in sentence if c not in punctuation)



"""
@ param string sentence sentence

@ return the sentence without stopwords. Stopwords are the words with symantic meaning
"""
def stop_words_removal(tokens):
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    return [w for w in tokens if not w in stop_words]



"""
@ param string sentence sentence

@ return the sentence in list a list format

"""
def tokenize_sentence(sentence):
    from nltk.tokenize import word_tokenize
    return word_tokenize(sentence)



"""
Converts the list to string

@ param list tokens     list of wards

@ return the a string of words
"""
def tokens_to_sentence(tokens):
    return ' '.join(token for token in tokens)


"""
Remove from the sentence 
@ param string sentence sentence

@ return the sentence without numbers
"""
def decontracted(sentence):
    import re
    phrase = re.sub(r"n\'t", " not", sentence)
    phrase = re.sub(r"\'re", " are", sentence)
    phrase = re.sub(r"\'s", " is", sentence)
    phrase = re.sub(r"\'d", " would", sentence)
    phrase = re.sub(r"\'ll", " will", sentence)
    phrase = re.sub(r"\'t", " not", sentence)
    phrase = re.sub(r"\'ve", " have", sentence)
    phrase = re.sub(r"\'m", " am", sentence)
    return phrase


"""
Convert the sentence to lowercase, remove numbers, punctiation

@ param string sentence     sentence

@ return the sentence without numbers
"""
def get_tokens(sentence):
    sentence = lowercase(sentence)
    sentence = remove_numbers(sentence)
    sentence = decontracted(sentence)
    sentence = remove_punctuation(sentence)
    tokens = tokenize_sentence(sentence)
    tokens = stop_words_removal(tokens)
    return tokens


"""
Keep from the sentence only the words that have symantic meaning

@ param string sentence     sentence
@ return the sentence in string
"""
def get_sentence(sentence):
    tokens = get_tokens(sentence)
    return tokens_to_sentence(tokens)


"""
Reads the sentences from the columns 'question1' and 'question2' and keep the words that have symantic meaning then saves
pandas dataframe in the file 'proccessed.csv'  
"""

def pre_proccess():
    df = pd.read_csv("train_original.csv")
    for index, row in df.iterrows():
        df.set_value(index,'question1', get_sentence(row['question1']))
        df.set_value(index, 'question2', get_sentence(row['question2']))
    df.to_csv('processed.csv')

    #average sentence length 22

"""
For each word in column question1 and question2 in the file 'processed.csv finds the occurence. 
Then sort the words in descending order. 
For each word in word in 'processed.csv' change it with a number, the number is the possition of the word in the sorted list.
Finally return the first 70% of the dataset as training set and the last 30% as testing set

@return pandas train_x, train_y, test_x,test_y
"""
def word_embending():

    def word_to_number(sentence,word_list):
        sentence = tokenize_sentence(sentence)
        new_word = []
        for i in range(len(sentence)):
            new_word.append(word_list.index(sentence[i])+1)
        return new_word

    from nltk.tokenize import word_tokenize
    import operator
    df = pd.read_csv("processed.csv")
    word_voc = {}
    for index, row in df.iterrows():
        question1 = word_tokenize(str(row['question1']))
        question2 = word_tokenize(str(row['question2']))

        "calculate the occurence of each word in column question1"
        for word in question1:
            if word in word_voc:
                word_voc[word] += 1
            else:
                word_voc[word] = 1
        "calculate the occurence of each word in column questiono2"
        for word in question2:
            if word in word_voc:
                word_voc[word] += 1
            else:
                word_voc[word] = 1

    sorted_words = sorted(word_voc.items(), key=operator.itemgetter(1), reverse=True)
    "list of the words in descending occurerence order"
    word_list=[]
    for i in range(len(sorted_words)):
        word_list.append(sorted_words[i][0])

    for index, row in df.iterrows():
        # if index == 3:
        #     break
        df.at[index, 'question1'] = word_to_number(str(row['question1']), word_list)
        df.at[index, 'question2'] = word_to_number(str(row['question2']), word_list)

    "return the dataset 70% train 30% test"
    size = df.shape[0]
    train_data = df[0:int(0.7 * size)]
    test_data = df[int(0.7 * size):size]
    y_train = train_data['is_duplicate']
    y_test = test_data['is_duplicate']
    x_train = train_data['question1'] + train_data['question2']
    x_test = test_data['question1'] + test_data['question2']

    return x_train, y_train, x_test,y_test

"For sentence find the tfidf"
def tfidf():
    from sklearn.feature_extraction.text import TfidfVectorizer
    df = pd.read_csv("proccessed.csv")
    q1 = df['question1']
    q2 = df['question2']
    questions = [q1, q2]
    "calculate tfidf for each question"
    questions = pd.concat(questions).values.astype('U')
    ftidf_vectorizer = TfidfVectorizer()
    questions = ftidf_vectorizer.fit_transform(questions)
    return questions
