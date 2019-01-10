
import fastText
from itertools import chain
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

data= pd.read_csv('fastext_rubric.csv')
X = data[['short_rubric','year_text']]
X['label']=X.short_rubric.str.replace(' ', '_')
X_train,X_test=train_test_split(X,test_size=.18,random_state=42,shuffle=True)
text=list(X_test.year_text.values)


print('ddim=24,epoch=12,lr=0.9, minCount=8,wordNgrams=2')
classifier = fastText.train_supervised('data_rubric.txt', label='__',dim=32,epoch=24, minCount=8,wordNgrams=2)
print('classifier ок')
predict_label=classifier.predict(text,k=1)


y_test=X_test.label
siries_m= list(chain(*predict_label[0]))


pred=pd.Series(siries_m,index=y_test.index)
pred=pred.str.replace('__', '')
print(accuracy_score(y_test,pred))
