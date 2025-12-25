import numpy as np
import math

def f1(x):
    return x**2 + 2*x + 1

def f2(x):
    return 0.2*x + np.sin(3*x)

def f3(x):
    return x**3 + np.log(x + 1)


num_samples = 2000
noise_rate = 0.05


def sample_generator(func):
    x_values = np.zeros(num_samples)
    y_values = np.zeros(num_samples)

    for i in range(num_samples):
        # Safe domain for f3
        if func == f3:
            x = np.random.uniform(0, 100)
        else:
            x = np.random.uniform(-100, 100)

        y_clean = func(x)
        noise = noise_rate * np.random.randn()
        y = y_clean * (1 + noise)

        x_values[i] = x
        y_values[i] = y

    return x_values, y_values



def save_to_csv(x, y, filename):
    data = np.column_stack((x, y))
    np.savetxt(
        filename,
        data,
        delimiter=",",
        header="x,y",
        comments=""
    )


x, y = sample_generator(f1)
save_to_csv(x, y, "data_f1.csv")

