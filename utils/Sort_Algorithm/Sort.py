import numpy as np

class Node():
    def __init__(self, array):
        self.array = array

    def Bubble_Sort(self):
        start = 0
        end = len(self.array) - 1

        while start < end:
            last_swapped = start

            for j in range(start, end):
                if self.array[j] > self.array[j + 1]:
                    # swap
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    last_swapped = j

            end = last_swapped

        return self.array
    
    def Selection_Sort(self):
        n = len(self.array)

        for i in range(n - 1, -1, -1):
            max_index = 0

            for j in range(0, i + 1):
                if self.array[j] > self.array[max_index]:
                    max_index = j

            # swap max value with self.array[i]
            self.array[i], self.array[max_index] = self.array[max_index], self.array[i]

        return self.array
    
if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    data = Node(data)
    sorted_data = data.Selection_Sort()
    print(sorted_data)