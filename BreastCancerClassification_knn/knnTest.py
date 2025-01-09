#import library
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import  accuracy_score

import pandas as pd

#data load
cancer = load_breast_cancer()
df= pd.DataFrame(data = cancer.data, columns= cancer.feature_names)
df["Target"] = cancer.target

# feutres and target 
X = cancer.data
y = cancer.target

#train test split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size= 0.3, random_state=2) #test size %30

#standardization (training veri setine göre standarziztion yapılır, teste göre yapılmaz)

scaler =StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#KNN define and train

knn = KNeighborsClassifier(n_neighbors=3) #3 komşuya bakıcak şekilde yapılır
knn.fit(X_train, y_train)

#KNN model test and verification

y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test,y_pred) #ypred 0,1 lerden oluşur
y_pred_train = knn.predict(X_train) # overfitting işlemi

                        
print(f"Test Accuracy: {accuracy}")
print(f"Trainining Accuracy: {accuracy_score(y_train,y_pred_train)}")
