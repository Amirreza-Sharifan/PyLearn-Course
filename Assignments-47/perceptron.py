import numpy as np
from tqdm import tqdm
class Perceptron:
    def __init__(self, learning_rate, input_length):
        self.learning_rate = learning_rate
        self.weights = np.random.rand(input_length)
        self.bias = np.random.rand(1)

    def activation(self, x, function):
        if function == "sigmoid":
            return 1 / (1 + np.exp(-x))
        elif function == "relu":
            return np.maximum(0, x)
        elif function == "tanh":
            return np.tanh(x)
        elif function == "linear":
            return x
        else:
            raise Exception("Unknown activation function")

    def fit(self, X_train, Y_train, epochs):
        for epoch in tqdm(range(epochs)):
            for x, y in zip(X_train, Y_train):
                #Forwarding
                y_pred = x @ self.weights + self.bias
                y_pred = self.activation(y_pred, "sigmoid")

                #Backward
                error = y - y_pred

                #Updating
                self.weights += self.learning_rate * error * x
                self.bias += self.learning_rate * error
    
    def predict(self, X_test):
        Y_pred = []
        for x_test in X_test:
            y_pred = x_test @ self.weights + self.bias
            y_pred = self.activation(y_pred, "sigmoid")
            Y_pred.append(y_pred)
        return np.array(Y_pred)
    
    def calculate_loss(self, X_test, Y_test, metric):
        Y_pred = self.predict(X_test)
        if metric == "mse":
            return np.mean(np.square(Y_test - Y_pred))
        elif metric == "mae":
            return np.mean(np.abs(Y_test - Y_pred))
        elif metric == "rmse":
            return np.sqrt(np.mean(np.square(Y_test, Y_pred)))
        else:
            raise Exception("Unknown metric")
        
    def calculate_accuracy(self, X_test, Y_test):
        Y_pred = self.predict(X_test)
        Y_pred = Y_pred.reshape(-1)
        Y_pred = np.where(Y_pred > 0.5 ,1, 0)
        accuracy = np.sum(Y_pred == Y_test) / len(Y_test)
        return accuracy
    
    def evaluate(self, X_test, Y_test):
        loss = self.calculate_loss(X_test, Y_test, "mse")
        accuracy = self.calculate_accuracy(X_test, Y_test)
        return loss, accuracy
        