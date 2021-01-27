from sklearn import svm
from sklearn import  datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

print(type(iris))

print(iris.data) #sepal length, sepal widht, petal length, petal width
print(iris.feature_names)

print(iris.target)  # 0 for setosa, 1 for vercicola,2 for virginica
print(iris.target_names)

#independent variable
X = iris.data[:,2] #all rows, and last two columns

#dependent variable
y= iris.target


#split data into two subsets, training data and testing data
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=4)
model = svm.SVC(kernel='linear') #what is kernel, 

#kernel, it adds a new feature, for creating a hyperplane,

X_test_mod= X_test.reshape(-1,1)
y_test_mod = y_test.reshape(-1,1)

X_train_mod = X_train.reshape(-1,1)
y_train_mod=y_train.reshape(-1,1)

model.fit(X_train_mod,y_train_mod.ravel())
y_pred_mod = model.predict(X_test_mod) 

#predict
accuracy = model.score(X_test_mod,y_test_mod)
print(accuracy)


print(iris.data)
# print(X)
print(X_test_mod)
print(y_pred_mod)
