import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import fft,ifft

def conv_nowrap(m,n):
    assert(m.size==n.size)
    mm=np.zero(2*m.size)
    mm[0:m.size]=m
    nn=np.zero(2*n.size)
    nn[0:n.size]=n
    mmft=fft(mm)
    nnft=fft(nn)
    vec=np.real(ifft(mmft*nnft))
    return vec[0:m.size]

if __name__=='__main__':
    m=np.arange(-30,30,0.1)
    sigma=2
    n=np.exp(-0.5*m**2/sigma**2)
    n=n/n.sum()
    nconv=conv_nowrap(n,n)
    
    plt.plot(m,n)
    plt.plot(m,nconv)
    plt.show()
    
    