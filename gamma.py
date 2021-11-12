import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as sts
import seaborn as sns

# build gamma distribution as population
shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)
s = np.random.gamma(shape, scale, 1000000)

# Step 1
# sample with different sample size
# list of sample mean
meansample = []
# number of sampling
numofsample = 25000
# sample size
samplesize = [1, 5, 10, 30, 100, 1000]
# for each sample size (1 to 1000)
for i in samplesize:
    # collect mean of each sample
    eachmeansample = []
    # for each sampling
    for j in range(0, numofsample):
        # sampling i sample from population
        rc = random.choices(s, k=i)
        # collect mean of each sample
        eachmeansample.append(sum(rc)/len(rc))
    # add mean of each sampling to the list
    meansample.append(eachmeansample)

# Step 2
# plot
cols = 2
rows = 3
fig, ax = plt.subplots(rows, cols, figsize=(20, 15))
fig.tight_layout(pad=10)
n = 0
variance = np.var(meansample)
fac = 1/np.sqrt(2*np.pi*variance)
mean = np.mean(meansample)
x0 = np.linspace(0, 1, 128)
dist = fac*np.exp(-(x0-mean)**2/(2*variance))
kde = sts.gaussian_kde(meansample)

for i in range(0, rows):
    for j in range(0, cols):
        ax[i, j].hist(meansample[n], 200, density=True)
        ax[i, j].set_title(label="sample size :" + str(samplesize[n]))
        n += 1
fig.suptitle("Gamma distribution with random sequence n(x; NEX, NVar(X))")
plt.show()
