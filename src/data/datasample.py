import numpy as np
import src.data.targetfunctions as targetfunctions
import math



num_samples = 2000


# datasample.py
import numpy as np

def generate_and_save_dataset(func, filename, num_samples=2000):
    x = np.zeros(num_samples)
    y = np.zeros(num_samples)

    for i in range(num_samples):
        if func.__name__ == "f3":
            xi = np.random.uniform(0, 100)
        else:
            xi = np.random.uniform(-100, 100)

        yi_clean = func(xi)
        noise = np.random.uniform(-0.10, 0.10)
        yi = yi_clean * (1 + noise)

        x[i] = xi
        y[i] = yi

    data = np.column_stack((x, y))
    np.savetxt(filename, data, delimiter=",", header="x,y", comments="")



def load_dataset(filename):
    data = np.loadtxt(filename, delimiter=",", skiprows=1)
    return data[:, 0], data[:, 1]





# x, y = sample_generator(targetfunctions.f1)

