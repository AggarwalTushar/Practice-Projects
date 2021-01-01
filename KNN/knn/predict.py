import numpy as np
import csv
import sys
from validate import validate
from collections import Counter
import math


def import_data(test_X_file_path):
    test_X = np.genfromtxt(test_X_file_path, delimiter=',', dtype=np.float64, skip_header=1)
    train_X = np.genfromtxt("train_X_knn.csv", delimiter=',', dtype=np.float64, skip_header=1)
    train_Y = np.genfromtxt("train_Y_knn.csv", delimiter=',', dtype=np.float64)
    return test_X,train_X,train_Y

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
    ans=np.zeros((len(test_X),1))
    f=0
    for i in test_X:
        temp=find_k_nearest_neighbors(train_X, i, k, n)
        for j in range(len(temp)):
            temp[j]=train_Y[temp[j]]
        b=Counter(temp)
       	l=max(list(b.values()))
        for m in b:
            if b[m]==l:
                ans[f]=m
                f+=1
                break
    return ans
def predict_target_values(test_X,x,y):
    return classify_points_using_knn(x, y, test_X, 1, len(x[0]))
    

def write_to_csv_file(pred_Y, predicted_Y_file_name):
    pred_Y = pred_Y.reshape(len(pred_Y), 1)
    with open(predicted_Y_file_name, 'w', newline='') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerows(pred_Y)
        csv_file.close()


def predict(test_X_file_path):
    test_X,x,y = import_data(test_X_file_path)
    pred_Y = predict_target_values(test_X,x,y)
    write_to_csv_file(pred_Y, "predicted_test_Y_knn.csv")


if __name__ == "__main__":
    test_X_file_path = sys.argv[1]
    predict(test_X_file_path)
    validate(test_X_file_path, actual_test_Y_file_path="train_Y_knn.csv") 
