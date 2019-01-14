import numpy as np

def change(data):
    data[0] = 1000

if __name__ == '__main__':
    list = [1,2,3,4,5]
    list = np.array(list)
    change(list)
    print(list)