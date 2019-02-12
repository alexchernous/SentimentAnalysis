import pandas
import pickle

# load the model from disk
loaded_model = pickle.load(open('Models/sentimentModelFinal.sav', 'rb'))

data = 'new'

url = f'Data/{data}Parameters.csv'
names = ['pos_neg_ratio']
dataset = pandas.read_csv(url, names=names)
Xnew = dataset.values

prediction = loaded_model.predict(Xnew)

for i in range(len(Xnew)):
    print("X=%s, Predicted=%s" % (Xnew[i], prediction[i]))


