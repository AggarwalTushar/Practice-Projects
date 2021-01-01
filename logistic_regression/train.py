import csv
import numpy as np
def import_data():
	train_X = np.genfromtxt("train_X_lg_v2.csv", delimiter=',', dtype=np.float64, skip_header=1)
	train_Y = np.genfromtxt("train_Y_lg_v2.csv", delimiter=',', dtype=np.float64)
	return train_X,train_Y
def train_data_i(Y,i):
	return 1*(Y==i)
def sigmoid(x):
	return 1/(1+np.exp(-x))
def compute_cost(x,y,w):
	m=len(y)
	a=sigmoid(np.dot(x,w))
	a[a == 1] = 0.99999
	a[a == 0] = 0.00001
	return (-1/m)*(np.sum(y*np.log(a)+(1-y)*np.log(1-a)))
def compute_gradient_of_cost_function(X, Y, W):
	A=sigmoid(np.dot(X,W))
	A=A-Y
	dw=(1/len(X))*(np.dot(X.T,A))
	return dw
def optimize_weights(x,y,w,learning_rate,iterations):
	for i in range(iterations):
		cost=compute_cost(x,y,w)
		dw=compute_gradient_of_cost_function(x,y,w)
		w=w-learning_rate*dw
		if i%1000==0:
			print(i,cost)
	return w
def train_model(X,Y):
	X=np.concatenate((np.ones((np.shape(X)[0],1)),X),axis=1)
	Y=Y.reshape(len(X),1)
	W=np.random.rand(X.shape[1],1)
	w1=W
	w2=W
	w3=W
	w4=W
	y0=train_data_i(Y,0)
	y1=train_data_i(Y,1)
	y2=train_data_i(Y,2)
	y3=train_data_i(Y,3)
	W0=optimize_weights(X,y0,w1,iterations=10**6,learning_rate=0.008)
	W1=optimize_weights(X,y1,w2,iterations=10**6,learning_rate=0.007)
	W2=optimize_weights(X,y2,w3,iterations=10**6,learning_rate=0.007)
	W3=optimize_weights(X,y3,w4,iterations=10**6,learning_rate=0.008)
	return W0,W1,W2,W3
def save_model(weights,file):
	with open(file,'w') as file:
		w=csv.writer(file)
		for i in weights:
			w.writerows(i)
if __name__=="__main__":
	X,Y=import_data()
	W=train_model(X,Y)
	save_model(W,"WEIGHTS_FILE.csv")
