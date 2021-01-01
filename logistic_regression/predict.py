import numpy as np
import csv
import sys

from validate import validate



def import_data_and_weights(test_X_file_path, weights_file_path):
    test_X = np.genfromtxt(test_X_file_path, delimiter=',', dtype=np.float64, skip_header=1)
    weights = np.genfromtxt(weights_file_path, delimiter=',', dtype=np.float64)
    return test_X, weights

def sigmoid(x):
	return 1/(1+np.exp(-x))
def predict_target_values(test_X, weights):
	test_X=np.concatenate((np.ones((len(test_X),1)),test_X),axis=1)
	n=len(test_X[0])
	w1=weights[:n]
	w2=weights[n:2*n]
	w3=weights[2*n:3*n]
	w4=weights[3*n:4*n]
	a1=sigmoid(np.dot(test_X,w1))
	a2=sigmoid(np.dot(test_X,w2))
	a3=sigmoid(np.dot(test_X,w3))
	a4=sigmoid(np.dot(test_X,w4))
	ans=np.zeros((len(test_X),1))
	for i in range(len(test_X)):
		l=max(a1[i],a2[i],a3[i],a4[i])
		if a1[i]==l:
			ans[i]=0
		elif a2[i]==l:
			ans[i]=1
		elif a3[i]==l:
			ans[i]=2
		else:
			ans[i]=3
	return ans


def write_to_csv_file(pred_Y, predicted_Y_file_name):
    pred_Y = pred_Y.reshape(len(pred_Y), 1)
    with open(predicted_Y_file_name, 'w') as csv_file:
        wr = csv.writer(csv_file)
        wr.writerows(pred_Y)
        csv_file.close()


def predict(test_X_file_path):
    test_X, weights = import_data_and_weights(test_X_file_path, "WEIGHTS_FILE.csv")
    pred_Y = predict_target_values(test_X, weights)
    write_to_csv_file(pred_Y, "predicted_test_Y_lg.csv")


if __name__ == "__main__":
    test_X_file_path = sys.argv[1]
    predict(test_X_file_path)
    validate(test_X_file_path, actual_test_Y_file_path="train_Y_lg_v2.csv") 
