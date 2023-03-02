import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import warnings
warnings.filterwarnings(action='ignore')
import pickle


df=pd.read_csv(r'D:\users\Praveen kumar\pycharmprojects\market price\Vegetable_market.csv')
print(df)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

x= np.array(df.iloc[:, 0:5])
y= np.array(df.iloc[:,6:])


x=le.fit_transform(x)
y=le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, shuffle=True, random_state=1)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

from sklearn.svm import SVC


from sklearn import linear_model
sv=linear_model(kernel='linear').fit(X_train,y_train)
pickle.dump(sv,open('Market.pkl','wb'))


