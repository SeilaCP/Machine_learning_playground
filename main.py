import numpy as np
from utils import MachineLearning

np.random.seed(42)

num_samples = 10
num_features = 10

#  Generate Features (X_train)
x_train = np.zeros((num_samples, num_features))

x_train[:, 0] = np.random.randint(800, 2500, num_samples) 
x_train[:, 1] = np.random.randint(1, 6, num_samples)    
x_train[:, 2] = np.random.randint(1, 4, num_samples)     
x_train[:, 3] = np.random.randint(10, 81, num_samples) 

x_train[:, 4:] = np.random.randint(0, 101, (num_samples, 6))

y_train = ( x_train[:, 0] * 0.2 + 
                x_train[:, 1] * 15 - 
                x_train[:, 3] * 0.8 + 
                np.random.normal(0, 10, num_samples))

tmp_alpha = 5.0e-7
interations = 1000

# run gradient descent
model = MachineLearning()

model.InputtwofeatureData(x_train, y_train, tmp_alpha, interations)
model.OutputResult(x_train)
