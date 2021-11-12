import matplotlib.pyplot as plt
import numpy as np
f = plt.figure(figsize=(18, 10))


def plotHist(nr, N, n_, mean, var0, x0):
    ''' plots the RVs'''
    x = np.zeros((N))
    sp = f.add_subplot(3, 2, n_)

    for i in range(N):
        for j in range(nr):
            x[i] += np.random.random()
        x[i] *= 1/nr
    plt.hist(x, 100, density=True, color='#348ABD', label=" %d RVs" % (nr))
    plt.setp(sp.get_yticklabels(), visible=False)

    variance = var0/nr
    fac = 1/np.sqrt(2*np.pi*variance)
    dist = fac*np.exp(-(x0-mean)**2/(2*variance))
    plt.plot(x0, dist, color='#A60628', linewidth=3, label='CLT', alpha=0.8)
    plt.xlabel('r')
    plt.xlim([0, 1])
    leg = plt.legend(loc="upper left")
    leg.get_frame().set_alpha(0.1)


N = 10000   # number of samples taken
nr = ([1, 2, 4, 8, 16, 32])

mean, var0 = 0.5, 1.0/12  # mean and variance of uniform distribution in range 0, 1
x0 = np.linspace(0, 1, 128)

for i in range(np.size(nr)):
    plotHist(nr[i], N, i+1, mean, var0, x0)

plt.suptitle(
    "random variables (RVs) converge to a Gaussian distribution (CLT)", fontsize=10)
plt.show()
