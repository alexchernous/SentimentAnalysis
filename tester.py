import pickle, pandas
from StringProcessing import StringProcessing as SP
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def convertResults(sentimentPrediction):
    if sentimentPrediction[0] == 1:
        print('\nIt seems to me your sentiment is positive :)\n')
    elif sentimentPrediction[0] == -1:
        print('\nI think your sentiment is negative :(\n')
    else:
        print("\nHmm, either I can't tell or your sentiment is neutral\n")

# load the model from disk
sentimentModel = pickle.load(open('Models/sentimentModelFinal.sav', 'rb'))

# Load dataset
data = 'emojis'
url = f'Data/{data}Parameters.csv'
names = ['pos_neg_ratio', 'sentiment']
dataset = pandas.read_csv(url, names=names)

# Split-out validation dataset
array = dataset.values
#print(array)
X = array[:,0:1]
#print(X)
Y = array[:,1]

stop = False

while(not stop):
    parameters = []

    user_input = input("\nType in a sentence and I'll try to analyze its sentiment:\n--> ")

    try:
        pos_neg_ratio = SP.positiveEmojis(user_input)/SP.negativeEmojis(user_input)
        if pos_neg_ratio > 2:
            pos_neg_ratio = 2

    except:
        pos_neg_ratio = 2

    parameters.append([pos_neg_ratio])
    print(pos_neg_ratio)

    sentimentPrediction = sentimentModel.predict(parameters)

    # give prob for each class
    print(sentimentModel.predict_proba(parameters))

    convertResults(sentimentPrediction)


    _ = input("Would you like to keep going?\n--> ").lower()

    stop = 'no' in _ or "'t" in _


