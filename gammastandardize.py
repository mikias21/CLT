import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as stats

# Step 1
# build gamma distribution as population
shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)
s = np.random.gamma(shape, scale, 1000000)

# Step 2
# sample from population with different number of sampling
# a list of sample mean
meansample = []
# number of sample
numofsample = [1000, 2500, 5000, 10000, 25000, 50000]
# sample size
samplesize = 500
# for each number of sampling (1000 to 50000)
for i in numofsample:
    # collect mean of each sample
    eachmeansample = []
    # for each sampling
    for j in range(0, i):
        # sampling 500 sample from population
        rc = random.choices(s, k=samplesize)
        # collect mean of each sample
        eachmeansample.append(sum(rc)/len(rc))
    # add mean of each sampling to the list
    meansample.append(eachmeansample)

# Step 3
# I will import the list above, so I make the code after this line run only when I call this file directly
if __name__ == "__main__":
    # plot
    cols = 2
    rows = 3
    fig, ax = plt.subplots(rows, cols, figsize=(20, 15))
    fig.tight_layout(pad=10)
    n = 0
    for i in range(0, rows):
        for j in range(0, cols):
            ax[i, j].hist(meansample[n], 200, density=True)
            ax[i, j].set_title(
                label="number of sampling :" + str(numofsample[n]))
            n += 1
    fig.suptitle("Gamma distribution with random sequence Xn and Yn")
    plt.show()
