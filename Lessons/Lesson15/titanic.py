# Titanic Logistic Regression
# https://datascienceplus.com/logistic-regression-with-python-using-titanic-data/

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# load the dataset
train = pd.read_csv("train.csv")

# inspect the data a bit
train.head()

# Columns
# PassengerId type should be integer
# Survived Survived or not
# Pclass class of travel
# Name Name of Passenger
# Sex gender
# Age Age
# SibSp Number of siblings/spouse aboard
# Parch Number of parent/child aboard
# Ticket
# Fare
# Cabin
# Embarked The port which a passenger has embarked
## C Cherbourg
## S Southampton
## Q Queenstown

# how many people were on the ship
train.count()

train[train['Sex'].str.match("female")].count()

train[train['Sex'].str.match("male")].count()

# what about the movie characters
## Jack Dawson
## Molly Brown
train[train["Name"].str.contains("Dawson")]

train[train["Name"].str.contains("Brown")]

# what class were the passengers traveling
sns.countplot(x='Survived', hue='Pclass', data=train)

sns.countplot(x='Survived', hue='Sex', data=train)

# As we saw we have some null values for age.  Lets create
# a function to impute
plt.figure(figsize=(10,7))
sns.boxplot(x='Pclass',y='Age',data=train)

def add_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        return int(train[train["Pclass"] == Pclass]["Age"].mean())
    else:
        return Age

train["Age"] = train[["Age", "Pclass"]].apply(add_age,axis=1)

# we have lots of null values for cabin lets drop it
train.drop("Cabin",inplace=True,axis=1)

# lets drop any rows with nulls
train.dropna(inplace=True)

# lets convert categorical data to numeric
pd.get_dummies(train["Sex"])

sex = pd.get_dummies(train["Sex"],drop_first=True)

# lets do the same for embarked and pclass
embarked = pd.get_dummies(train["Embarked"],drop_first=True)
pclass = pd.get_dummies(train["Pclass"],drop_first=True)

# add these columns to the dataset
train = pd.concat([train,pclass,sex,embarked],axis=1)

# then remove some columns we are not going to use
train.drop(["PassengerId","Pclass","Name","Sex","Ticket","Embarked"],axis=1,inplace=True)

# create our model data set
X = train.drop("Survived",axis=1)
y = train["Survived"]

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

predictions = logmodel.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, predictions))

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, predictions)

# True positive: 107 (We predicted a positive result and it was positive)
# True negative: 60 (We predicted a negative result and it was negative)
# False positive: 21 (We predicted a positive result and it was negative)
# False negative: 26 (We predicted a negative result and it was positive)

# End of File