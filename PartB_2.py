from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from clear_data import get_sentence
from symmetric_similarity import *
from preproccessing import tfidf
import csv
import io

count_questions = 20000 # setting the number of question pairs.
questions = [] # for appending the two questions
is_duplicate = [] # save it to compute accuracy later
count_duplicates = 0 # save it to compute accuracy later

# Reading - pre_proccess our dataset.
with io.open('train_original.csv', mode = 'r' , encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)

    i = 0
    for row in reader:
        i += 1
        questions.append(get_sentence(row['question1']))
        questions.append(get_sentence(row['question2']))
        is_duplicate.append(int(row['is_duplicate']))
        if (int(row['is_duplicate'])):
            count_duplicates += 1
        if i >= count_questions:
            break

# Statistic_Model
ftidf_vectorizer = TfidfVectorizer()
questions_ftidf = ftidf_vectorizer.fit_transform(questions)

ftidf_similarity = []
for i in range(0,count_questions,2):
    ftidf_similarity.append(cosine_similarity(questions_ftidf[i], questions_ftidf[i+1]))

# Semantic_Model
symmetric_similarity = []
for i in range(0,count_questions,2):
    symmetric_similarity.append(symmetric_question_similarity(questions[i], questions[i+1]))


"""
Semantic_Model + Statistic_Model Accuracy

By changing the statistic_portion and semantic_portion variables
you set how much does each model take part for the final prediction.
    In the example below we use only the Semantic_Model.

"""
index =0
correct_answers = 0

# These two must sum up to 1.0
statistic_portion = 0.0
semantic_portion = 1.0

threshold = 0.9

for i in range(int(count_questions/2)):
    similarity = (statistic_portion*ftidf_similarity[i] + semantic_portion*symmetric_similarity[i])
    if similarity > threshold:
        label = 1
    else:
        label = 0
    if label == is_duplicate[index]:
        correct_answers +=1
    index += 1

print(correct_answers/count_questions*2)
