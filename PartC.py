import pandas as pd
from datasketch.minhash import MinHash
from datasketch.lsh import MinHashLSH
from preprocess import tokenize_sentence


"""
To find similar questions in O(1) we are using jaccard similarity and minHash. 
Question with similar minHash are candidates to be similar. 
To compare if two candidate senteces are similar we are using jaccard similarity  
"""

df = pd.read_csv("proccessed.csv")
total_questions = df.shape[0]
threshold_jacard = 0.30
lsh = MinHashLSH(threshold=threshold_jacard)

#calculate minhash for each sentence in column question1
for index, row in df.iterrows():
    min_Hash = MinHash()
    question = tokenize_sentence(str(row['question1']))
    for word in question:
        min_Hash.update(word.encode('utf8'))
    lsh.insert(str(index), min_Hash)


total = 0
return_result = 0
correct = 0
total_correct =0
#for each sentense in column question2 find similar questions
for i in range(0, total_questions):
    question_minHash = MinHash()
    question = tokenize_sentence(str(df['question2'][i]))
    for word in question:
        question_minHash.update(word.encode('utf8'))
    candidates = lsh.query(question_minHash)
    result = []
    #check which candidates are similar with the sentence
    for j in range(len(candidates)):
        canditade = df['question1'][int(candidates[j])]
        cand = set(tokenize_sentence(str(canditade)))
        cand_minHash = MinHash()
        for word in cand:
            cand_minHash.update(word.encode('utf8'))
        if cand_minHash.jaccard(question_minHash) >= threshold_jacard:
            result.append(str(candidates[j]))

    #statistcs
    if df['is_duplicate'][i] == 1:
        total_correct += 1
    if len(result) > 0:
        return_result += 1
    if str(i) in result:
        total += 1
        if df['is_duplicate'][i]:
            correct += 1

print("Precision {}%"  .format(correct/return_result*100))
print("Recall {}%"  .format(correct/total_correct*100))