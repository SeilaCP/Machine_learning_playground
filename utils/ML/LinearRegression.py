import numpy as np
def Predict_Result(X, w, b):
    """
    Make predictions using the trained linear regression model.
    
    Args:
        X (ndarray): The input data, shape (m, n).
        w (ndarray): The weights of the model, shape (n,).
        b (scalar): The bias term of the model.
    
    Returns:
        predictions (ndarray): The predicted values, shape (m,).
    """
    X = np.atleast_2d(X)
    m = X.shape[0]

    if X.shape[1] != len(w):
        raise ValueError(
            f"Model expects {len(w)} features but got {X.shape[1]}"
        )

    for i in range(m):
        
        print(f"prediction: {np.dot(X[i], w) + b:0.2f}")

import numpy as np

def R_squared(X, Y, w, b):
    X = np.atleast_2d(X)
    m = X.shape[0]
    
    if X.shape[1] != len(w):
        raise ValueError(f"Model expects {len(w)} features but got {X.shape[1]}")

    # Vectorized prediction
    y_pred = np.dot(X, w) + b
    ss_res = np.sum((Y - y_pred) ** 2)
    y_mean = np.mean(Y)
    ss_tot = np.sum((Y - y_mean) ** 2)
    
    r2 = 1 - (ss_res / ss_tot)
    
    return r2

