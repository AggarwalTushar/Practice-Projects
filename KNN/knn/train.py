import numpy as np
import math
from collections import Counter
def import_data():
	train_X = np.genfromtxt("train_X_knn.csv", delimiter=',', dtype=np.float64, skip_header=1)
	train_Y = np.genfromtxt("train_Y_knn.csv", delimiter=',', dtype=np.float64)
	return train_X,train_Y
def compute_ln_norm_distance(vector1, vector2, n):
    ans=0
    for i in range(len(vector1)):
        ans+=(abs(vector1[i]-vector2[i]))**n
    return ans**(1/n)
def find_k_nearest_neighbors(train_X, test_example, k, n):
    temp=[]
    for i in range(len(train_X)):
        a=compute_ln_norm_distance(train_X[i],test_example,n)
        temp.append((i,a))
    temp.sort(key=lambda x:x[1])
    ans=[]
    i=0
    while i<k:
        ans.append(temp[i][0])
        i+=1
    return ans
def classify_points_using_knn(train_X, train_Y, test_X, k, n):
    ans=[]
    for i in test_X:
        temp=find_k_nearest_neighbors(train_X, i, k, n)
        for j in range(len(temp)):
            temp[j]=train_Y[temp[j]]
        b=Counter(temp)
        l=max(b.values())
        for m in b:
            if b[m]==l:
                ans.append(m)
                break
    return ans
	
def calculate_accuracy(predicted_Y, actual_Y):
    ans=0
    for i in range(len(predicted_Y)):
        if abs(predicted_Y[i]-actual_Y[i])==0:
            ans+=1
    return (ans/len(predicted_Y))
def get_best_k_using_validation_set(train_X, train_Y, validation_split_percent,n):
    X=train_X[:math.floor(((100-validation_split_percent)/100)*len(train_X))]
    valid_X=train_X[math.floor(((100-validation_split_percent)/100)*len(train_X)):]
    Y=train_Y[:math.floor(((100-validation_split_percent)/100)*len(train_X))]
    valid_Y=train_Y[math.floor(((100-validation_split_percent)/100)*len(train_X)):]
    k=list(range(1,len(X)+1))
    ans=1
    m=0
    for i in k:
        pred=classify_points_using_knn(X, Y, valid_X, i, n)
        acc=calculate_accuracy(pred, valid_Y)
        if acc>m:
            m=acc
            ans=i
    return ans
if __name__=="__main__":
	x,y=import_data()
	print("Best k value: "+str(get_best_k_using_validation_set(x, y, 50,len(x[0]))))
