# svm
#import lib
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt

#load dataset

digits = load_digits()

X = digits.data
y = digits.target

# visulization
plt.figure(figsize=(10,5))
for i in range(2):
    plt.subplot(1,2, i+1)
    plt.imshow(digits.images[i], cmap="gray")
    plt.title(f"görüntü{i+1}")
    plt.axis("off")
plt.show()

# train test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size =0.2,random_state=42)


# svm
svm_model =SVC(kernel="linear", random_state=42)
svm_model.fit(X_train, y_train)

# svm training
y_pred = svm_model.predict(X_test)

# svm test: accucacy

accuracy = accuracy_score(y_test, y_pred)
print(f"accuracy: {accuracy}")
