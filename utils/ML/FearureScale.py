import numpy as np
class Scale:
    def __init__(self, x_raw = np.array([0]), y_raw = np.array([0])):
        self.x_raw = x_raw
        self.y_raw = y_raw

    def NormalScaling(self):
        return self.x_raw / np.max(self.x_raw), self.y_raw / np.max(self.y_raw)
    
    def MeanNormalization(self):
        return (self.x_raw - np.mean(self.x_raw)) / (np.max(self.x_raw) - np.min(self.x_raw)), (self.y_raw - np.mean(self.y_raw)) / (np.max(self.y_raw) - np.min(self.y_raw))
    
    def Z_ScoreNormalization(self):
        return (self.x_raw - np.mean(self.x_raw)) / np.std(self.x_raw), (self.y_raw - np.mean(self.y_raw)) / np.std(self.y_raw)

if __name__ == "__main__":
    x_train = np.array([[1.0, 2.0], [1, 2]])   #features
    # y_train = np.array([300.0, 500.0])   #target value
    
    s = Scale(x_train)
    x_NM, y_NM = s.NormalScaling()
    x_MNM, y_MNM = s.MeanNormalization()
    x_ZS, y_ZS = s.Z_ScoreNormalization()

    print("x: ",x_NM, "y: ", y_NM)
    print("x: ",x_MNM, "y: ", y_MNM)
    print("x: ",x_ZS, "y: ", y_ZS)

