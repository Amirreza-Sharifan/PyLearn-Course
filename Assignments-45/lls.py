import numpy as np
from numpy.linalg import inv

class LinearLeastSquare:
    def __int__(self):
        pass

    def fit(self, X_train, Y_trian):
        self.a = inv(X_train.T @ X_train) @ X_train.T @ Y_trian

    def predict(self, X_test):
        Y_pred = X_test @ self.a
        return Y_pred
    
    def evaluate(self, X_test, Y_test, metric):
        Y_pred = self.predict(X_test)

        if metric == "mae":
            loss = np.sum(np.abs(Y_test - Y_pred)) / len(Y_test)
        elif metric == "mse":
            loss = np.sum(np.abs(Y_test - Y_pred) ** 2) / len(Y_test)
        else:
            print("Please Choose the Correct Loss Function(mae or mse)")

        return loss