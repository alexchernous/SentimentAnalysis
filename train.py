# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import pickle
from StringProcessing import setUpTrainingSet




def loadData():


    # Load dataset
    data = 'emojis'
    url = f'Data/{data}Parameters.csv'
    names = ['pos_neg_ratio', 'sentiment']
    dataset = pandas.read_csv(url, names=names)

    #visual plot
    scatter_matrix(dataset)
    plt.show()

    # Split-out validation dataset
    array = dataset.values
    #print(array)
    X = array[:,0:1]
    #print(X)
    y = array[:,1]

    return X, y

def trainingModel(X, y):
    #print(Y)
    validation_size = 0.30
    seed = 7
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, y, test_size=validation_size, random_state=seed)


    svm = SVC(gamma='scale', probability=True)
    svm.fit(X_train, Y_train)
    predictions = svm.predict(X_test)
    print(X_test)
    print(accuracy_score(Y_test, predictions))
    print(confusion_matrix(Y_test, predictions))
    print(classification_report(Y_test, predictions))

    pickle.dump(svm, open('Models/sentimentModelTrain.sav', 'wb'))


def finalModel(X, y):
    #FINALIZING MODEL

    finalModel = SVC(gamma='scale', probability=True)
    finalModel.fit(X,y)

    pickle.dump(finalModel, open('Models/sentimentModelFinal.sav', 'wb'))


if __name__ == "__main__":
    '''
    automated processing of some sentences for training.

    this does sentiment identification automatically with a simple regex,
    which defeats the purpose of ML, but it's just a POC for myself for future
    analysis where I'll tag sentences manually and can't simply use regex.
    '''
    setUpTrainingSet()

    X, y = loadData()
    trainingModel(X, y)
    finalModel(X, y)