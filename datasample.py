import numpy as np
import targetfunctions
import math



num_samples = 2000


def sample_generator(func,filename_tosave):
    x_values = np.zeros(num_samples)
    y_values = np.zeros(num_samples)

    for i in range(num_samples):
        # Safe domain for f3
        if func == targetfunctions.f3:
            x = np.random.uniform(0, 100)
        elif(func == targetfunctions.f1 or func == targetfunctions.f2):
            x = np.random.uniform(-100, 100)

        y_clean = func(x)
        noise = np.random.uniform(-0.10, 0.10)  #noise rate is between 0 to 10 percent.
        y = y_clean * (1 + noise)

        x_values[i] = x
        y_values[i] = y
    # only used to generate random samples and save them on csv
    data = np.column_stack((x_values, y_values))
    np.savetxt(
        filename_tosave,
        data,
        delimiter=",",
        header="x,y",
        comments=""
    )

    return x_values, y_values



# x, y = sample_generator(targetfunctions.f1)

