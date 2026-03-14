import numpy as np
from utils import GredietDecent, Predict_Result

x_train = np.array([1.0, 2.0])   #features
y_train = np.array([300.0, 500.0])   #target value

w_init = 0
b_init = 0
# some gradient descent settings
iterations = 10000
tmp_alpha = 1.0e-2



# run gradient descent
gd = GredietDecent(x_train ,y_train, w_init, b_init, tmp_alpha, iterations)
w_final, b_final, J_hist, p_hist = gd.gradient_descent()
print(f"(w,b) found by gradient descent: ({w_final:8.4f},{b_final:8.4f})")

predictions = Predict_Result(np.array([1.0]), w_final, b_final)
print(f"Predictions: {predictions}")