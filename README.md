# Quora-Questions-Pairs

Over 100 million people visit Quora every month, so it's no surprise that many people ask similarly worded questions. Multiple questions with the same intent can cause seekers to spend more time finding the best answer to their question, and make writers feel they need to answer multiple versions of the same question. Quora values canonical questions because they provide a better experience to active seekers and writers, and offer more value to both of these groups in the long term.

Quora released on 24 January 2017, a dataset giving anyone the opportunity to train and test models of semantic equivalence, based on actual Quora data, to see how diverse approaches fare on this problem.

The dataset consists of over 400,000 lines of potential question duplicate pairs. Each line contains IDs for each question in the pair, the full text for each question, and a binary value that indicates whether the line truly contains a duplicate pair. Here are a few sample lines of the dataset:  
<br/>
![](https://qph.fs.quoracdn.net/main-qimg-ea50c7a005eb7750af0b53b07c8caa60)
<br/>

## To get the dataset just follow the link : [Quora-Questions-Pairs-Dataset](https://www.kaggle.com/quora/question-pairs-dataset)



# 3 Diffrent-Approaches:

**Part A:** Classification with Labels.

**Part B:** Classification without Labels.

**Part C:** Input: New questions - Output: Similar Questions.



# Results

### Part A

| #Question-Pairs        | Accuracy    |
|:----------------------:|:-----------:|
| 10.000                 | 50%         |
| 50.000                 | 60%         |
| 100.000                | 70%         |


### Part B

#### For 200.000 #Question-Pairs

| Model                  | Accuracy    |
|:----------------------:|:-----------:|
| Statistic(Tfidf)       | 66.5%       |
| Semantic(WordNet)      | 66.46%      |


### Combining the two models:

![](https://i.imgur.com/t0gqyxz.png)


| δ     |  Accuracy           |
| ----- | :-----------------: |
|  0.3  |  65.36%             |
|  0.5  |  65.68%             |
|  0.7  |  66.34%             |


### Part C

##### Two diffrent cases examined to rate our model:
1)When the returned question has the variable is_dublicate = 1.  
2)When the returned question is the pair of the input question.

| Case    | Recall       | Precision  |
| ------- | :----------: | :--------: |
| 1       | 42.65%       | 78.20%      |
| 2       | 78.00%       | 53.70%     |

# Built With 
* [Python](https://www.python.org/) - Programming language

# Authors - Contributors
* [Andreou Alexandros](https://www.linkedin.com/in/alexandros-andreou-39b278136/)
* [Achilleas Anastos](https://www.linkedin.com/in/achilleas-anastos-281343123/)

# Acknowledgments

* [Question Similarity Calculation for FAQ Answering](https://ieeexplore.ieee.org/document/4438554)
