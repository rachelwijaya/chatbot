from newspaper import Article
import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings

warnings.filterwarnings('ignore')
nltk.download('punkt', quiet=True)

article = Article('https://www.unicef.org/indonesia/coronavirus/stories/learning-home-during-covid-19-pandemic')
article.download()
article.parse()
article.nlp()
corpus = article.text

# Tokenization
text = corpus
sentenceList = nltk.sent_tokenize(text)  # List of sentences from the text


# Return random greeting response to user's greeting
def greetingResponse(text):
    text = text.lower()

    botGreets = ['yo', 'hey', 'hello', 'hi', 'hola', 'howdy']
    userGreets = ['hi', 'hey', 'hello', 'howdy', 'greetings']

    for word in text.split():
        if word in userGreets:
            return random.choice(botGreets)


def indexSort(listVariable):
    length = len(listVariable)
    listIndex = list(range(0, length))
    x = listVariable
    for i in range(length):
        for j in range(length):
            if x[listIndex[i]] > x[listIndex[j]]:
                # swap
                temp = listIndex[i]
                listIndex[i] = listIndex[j]
                listIndex[j] = temp
    return listIndex

# create bots response
def botResponse(userInput):
    userInput = userInput.lower()
    sentenceList.append(userInput)
    botResponse = ''
    cm = CountVectorizer().fit_transform(sentenceList)  # count matrix
    similarityScore = cosine_similarity(cm[-1], cm)  # gives similarity score to user input
    similarityScoreList = similarityScore.flatten()
    # find index in the highest in the score
    index = indexSort(similarityScoreList)
    # contains indices that is ascending for the highest values in similarity scores
    index = index[1:]
    # check if there is response to user
    responseFlag = 0
    j = 0
    for i in range(len(index)):
        if similarityScoreList[index[i]] > 0.0:  # found a sentence similar to user's input
            botResponse = botResponse + " " + sentenceList[index[i]]
            responseFlag = 1
            j += 1  # indicates how many scores there are that are above zero

        if j > 2:
            break
    if responseFlag == 0:
        # cant find sentence similar to user's input
        botResponse = botResponse + " " + "sorry idgi"
        # remove user's resposne from list
    sentenceList.remove(userInput)
    return botResponse


# start the chat
print("beep boop i am AI chatbot")
# an exit list so that the while loop stops
leaveList = ['bye', "goodbye", "leave", "exit", "quit"]
while(True):
    userInput = input()
    if userInput.lower() in leaveList:
        print("see u ltr loser")
        break
    else:
        if greetingResponse(userInput) != None:
            print(greetingResponse(userInput))
        else:
            print(botResponse(userInput))

