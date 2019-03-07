
from preprocess import tfidf
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


"""
This is an unsupervised method to check if two sentences are similar.

Find tfidf for each sentence then calculate the cosine similarity for sentences that are in the same line. If the similary
is bigger than the thresholod label the two sentence as similar otherwise there not 
"""

threshold_similarity = 0.85

df = pd.read_csv("proccessed.csv")
labels = df['is_duplicate']

#calculate tfidf for each sentence
questions = tfidf()


size = questions.shape[0]
total_questions = int(size/2)

#Label if two sentences are similar or not
correct_answers = 0
for i in range(total_questions):
    similarity = cosine_similarity(questions[i], questions[total_questions+i])
    if similarity >= threshold_similarity:
        label = 1
    else:
        label = 0
    #check if the label given from the model is correct
    if label == labels[i]:
        correct_answers += 1

#Calculate the accuracy of the model
print("Accuracy: {}".format(correct_answers/total_questions*100))

