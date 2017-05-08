import numpy
from matplotlib import pyplot as plt
from numpy.fft import fft,ifft

def corr(n,m):
    assert(n.size==m.size)
    nft=fft(n)
    mft=fft(m)
    mftconj=numpy.conj(mft)
    return numpy.real(ifft(nft*mftconj))

if __name__=='__main__':
    n=numpy.arange(-30,30,0.1)
    sigma=2
    m=numpy.exp(-0.5*n**2/sigma)
    mcorr=corr(m,m)
    plt.plot(n,mcorr)
    plt.show()
    


