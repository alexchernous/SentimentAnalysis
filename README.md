SentimentAnalysis
=================
Description:
------------
An on going project of sentiment analysis using Machine Learning.
Current state:
* SVM ML algorithm trained on synthetic sentences containing smile and frown emojis to gauge sentiment (positive, negative, neutral)


Version and Info:
-----------------
* python version: 3.6.6/3.7.2
* imports:
```python
import pickle, re, csv, math, pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
```
* training and final models are included in the 2 *.sav* files in Models/

Running program:
----------------
1. Update python version **(IF APPLICABLE)**
2. Use *pip/conda* to install any python packages **(IF APPLICABLE)**
3. Run *tester.py*

Note: if you want to test the training of the model, run *train.py*