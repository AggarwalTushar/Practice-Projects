import csv
import numpy as np
def import_data():
	train_X = np.genfromtxt("train_X_lr.csv", delimiter=',', dtype=np.float64, skip_header=1)
	train_Y = np.genfromtxt("train_Y_lr.csv", delimiter=',', dtype=np.float64)
	train_X=np.concatenate((np.ones((np.shape(train_X)[0],1)),train_X),axis=1)
	return train_X,train_Y
def compute_gradient_descent(X,Y,W):
	Y_pred=np.dot(X,W)
	diff=Y_pred-Y
	dw=(1/len(X))*(np.dot(diff.T,X))
	return dw.T
def compute_cost(X,Y,W):
	Y_pred=np.dot(X,W)
	cost=(Y_pred-Y)**2
	return (1/(2*len(X)))*np.sum(cost)
def optimize_weights(X,Y,W,num_iterations,learning_rate):
	prev_cost=0
	for i in range(num_iterations):
		W=W-(learning_rate*compute_gradient_descent(X,Y,W))
		cost=compute_cost(X,Y,W)
		if (i+1)%10000==0:
			print(i+1,cost)
		if abs(cost-prev_cost)<0.000001:
			print(i+1,cost)
			break
		prev_cost=cost
	return W
def train_model(X,Y):
	Y=Y.reshape(len(X),1)
	W=np.random.rand(X.shape[1],1)
	W=optimize_weights(X,Y,W,num_iterations=10**9,learning_rate=0.0002)
	return W
def save_model(weights,file):
	with open(file,'w') as file:
		w=csv.writer(file)
		w.writerows(weights)
if __name__=="__main__":
	X,Y=import_data()
	W=train_model(X,Y)
	save_model(W,"WEIGHTS_FILE.csv")
