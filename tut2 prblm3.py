import numpy
from matplotlib import pyplot as plt
from numpy.fft import fft,ifft


def makeshift(x,n=0):
    zerovec=0*x
    zerovec[1]=n
    vecft=fft(zerovec)
    xft=fft(x)
    return numpy.real(ifft(xft*vecft))

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
    mshiftcorr=corr(shift,shift)
    mshift=makeshift(m,m.size/4)
    
    mshiftcorr=mcorr(mshift,mshift)
    meaner=numpy.mean(numpy.abs(mcorr-mshiftcorr))
    
    plt.plot(n,mcorr)
    plt.plot(x,mshiftcorr)
    plt.show()
    
    