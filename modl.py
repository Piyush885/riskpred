import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import xgboost as xgb
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
def calculat_score(arr):
    df = pd.read_csv('Maternal Health Risk Data Set.csv')
    X = df.drop(['RiskLevel'],axis=1)
    y = df.RiskLevel
    X.BodyTemp = (X.BodyTemp - 32)*5/9
    le = LabelEncoder()
    y = le.fit_transform(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
    #sc = StandardScaler()
    # X_train = sc.fit_transform(X_train)
    # X_test = sc.transform(X_test)
    gama = np.arange(0.05, 15, 0.05)
    c_vals = np.arange(0.5, 15, 0.5)
    max_acc = 0
    max_gama = 2.45
    max_c = 5.0

    
    
    
    svm = SVC(kernel='rbf', random_state=7, gamma=max_gama, C=max_c)
    svm.fit(X_train, y_train)
    
    return svm.predict(arr)[0]
print(calculat_score([[25,130,80,15.0,98.0,86]]))
# {
#   "age":1.85955195,
#   "systolicBP":1.45721471,
#   "diastolicBP":1.35024476,  
#   "bs":3.13209818,  
#   "bodytemp":-0.4871202,  
#   "heartrate":0.3495532 
# }    
   
