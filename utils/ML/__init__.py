import numpy as np
from .GredietDecent import GredietDecent
from .LinearRegression import Predict_Result, R_squared
from .FearureScale import Scale

class MachineLearning():

    def InputtwofeatureData(self, x_train ,y_train, tmp_alpha, iterations):
        self.x_train = x_train
        self.y_train = y_train

        w_init = np.zeros(len(x_train[0]))
        print(w_init)
        b_init = 0.
        gd = GredietDecent(x_train ,y_train, w_init, b_init, tmp_alpha, iterations)

        self.w_final, self.b_final, self.J_hist = gd.gradient_descent()
        print("f(x) =", self.w_final, "x + ", self.b_final)
        print("R2: ", R_squared(x_train, y_train, self.w_final, self.b_final))
    
    def OutputResult(self, x_test):
        Predict_Result(x_test, self.w_final, self.b_final)

