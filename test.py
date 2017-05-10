from __future__ import division

import scipy.stats
from numpy import *

def normpdf(x, mu, sigma):
    u = (x-mu)/abs(sigma)
    y = (1/(sqrt(2*pi)*abs(sigma)))*exp(-u*u/2)
    return y


print scipy.stats.norm.pdf(1, 0, 1)
print normpdf(-1, 0, 1), '\n'

print scipy.stats.norm.pdf(1, 20, 10)
print normpdf(1, 20, 10), '\n'

print scipy.stats.norm.pdf(10, 20, 10)
print normpdf(10, 20, 10)