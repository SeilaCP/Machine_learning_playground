
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
    
    return X * w + b