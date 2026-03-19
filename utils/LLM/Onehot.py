def normal_encoded(data):
    unique_values = list(set(data))
    encoded = []

    
def Onehot_encoder(data):
    unique_values = list(set(data))
    encoded = []
    
    for item in data:
        vector = []
        for value in unique_values:
            if item == value:
                vector.append(1)
            else:
                vector.append(0)
        encoded.append(vector)
    
    return encoded, unique_values

if __name__ == "__main__":
    data = ["cat", "dog", "cat", "bird"]

    encoded, labels = Onehot_encoder(data)

    print("Labels:", labels)
    print("Encoded:")
    for row in encoded:
        print(row)