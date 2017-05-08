import numpy
from matplotlib import pyplot as plt
from numpy.fft import fft,ifft


def makeshift(x,n=0):
    zerocvec=0*x
    zerovec[n]=1
    vecft=fft(zerovec)
    xft=fft(x)
    return numpy.real(ifft(xft*vecft))

if __name__=='main__':
    x=numpy.arange(-30,30,0.1)
    sigma=2
    y=numpy.exp(-0.5*x**2/(sigma**2))
    yshift=makeshift(y,y.size/2) 
    
    plt.ion()
    plt.plot(x,y)
    plot.plot(x,yshift)
    plt.show()
    
    
    
    
    
    



