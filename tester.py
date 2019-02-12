import pickle
from StringProcessing import StringProcessing as SP

def convertResults(sentimentPrediction):
    if sentimentPrediction[0] == 1:
        print('\nIt seems to me your sentiment is positive :)\n')
    elif sentimentPrediction[0] == -1:
        print('\nI think your sentiment is negative :(\n')
    else:
        print("\nHmm, either I can't tell or your sentiment is neutral\n")

# load the model from disk
sentimentModel = pickle.load(open('Models/sentimentModelFinal.sav', 'rb'))

stop = False

while(not stop):
    parameters = []

    user_input = input("\nType in a sentence and I'll try to analyze its sentiment:\n--> ")

    try:
        pos_neg_ratio = SP.positiveEmojis(user_input)/SP.negativeEmojis(user_input)


    except:
        pos_neg_ratio = 2

    parameters.append([pos_neg_ratio])
    print(pos_neg_ratio)

    sentimentPrediction = sentimentModel.predict(parameters)

    convertResults(sentimentPrediction)


    _ = input("Would you like to keep going?\n--> ").lower()

    stop = 'no' in _ or "'t" in _


