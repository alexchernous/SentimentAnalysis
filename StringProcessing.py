import re, csv
import math

class StringProcessing:
    '''
    Sarcasm is not analyzed.
    '''

    def positiveEmojis(sentence):

        return len(re.findall(r':\)',sentence))

    def negativeEmojis(sentence):

        return len(re.findall(r':\(',sentence))


def setUpTrainingSet():
    data = 'emojis'

    sentences = []
    parameters = []

    with open(f'Data/{data}Sentences.txt') as file:
        sentences = file.readlines()

    sentences = [x.strip('\n') for x in sentences]
    print(sentences)


    for i in sentences:
        try:
            pos_neg_ratio = StringProcessing.positiveEmojis(i)/StringProcessing.negativeEmojis(i)
            if pos_neg_ratio > 2:
                pos_neg_ratio = 2
        except:
            pos_neg_ratio = 2

        if data == 'emojis':

            '''
            this defeats the purpose of ML, but this is just to help my POC
            so i don't have to manually tag sentences
            '''
            if pos_neg_ratio > 1: verdict = 1
            elif pos_neg_ratio == 1: verdict = 0
            else: verdict = -1

            parameters.append([pos_neg_ratio,verdict])

        else:
            parameters.append([pos_neg_ratio])


    print(parameters)

    with open(f'Data/{data}Parameters.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in parameters:
            writer.writerow(i)