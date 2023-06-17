import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import scipy
from scipy.stats.mstats import gmean


def Kwant(data, bit):
    d = (2**bit) - 1
    if np.issubdtype(data.dtype, np.floating):
        m = -1
        n = 1
    else:
        m = np.iinfo(data.dtype).min
        n = np.iinfo(data.dtype).max
    new_data = data.astype(float)
    Z_A = (new_data - m) / (n - m)
    Z_B = Z_A * d
    Z_B = np.round(Z_B)
    Z_A = Z_B / d
    Z_C = (Z_A * (n-m))+m
    new_data = Z_C
    return new_data.astype(data.dtype)


def A_law_compress(data):
    A = 87.6
    x1 = np.abs(data) < (1/A)
    x2 = np.logical_not(x1)
    comp_data = data.copy()
    comp_data[x1] = np.sign(comp_data[x1])*((A*np.abs(comp_data[x1]))/(1+np.log(A)))
    comp_data[x2] = np.sign(comp_data[x2])*((1+np.log(A*np.abs(comp_data[x2])))/(1+np.log(A)))
    return comp_data


def A_law_decompress(data):
    A = 87.6
    y1 = np.abs(data) < (1/(1+np.log(A)))
    y2 = np.logical_not(y1)
    decomp_data = data.copy()
    decomp_data[y1] = np.sign(decomp_data[y1])*((np.abs(decomp_data[y1])*(1+np.log(A)))/A)
    decomp_data[y2] = np.sign(decomp_data[y2])*(np.exp(np.abs(decomp_data[y2])*(1+np.log(A))-1)/A)
    return decomp_data


def mu_law_compress(data):
    mu = 255
    if np.issubdtype(data.dtype, np.integer) or np.issubdtype(data.dtype, np.unsignedinteger):
        raise Exception("zły typ danych - musi byc float")
    comp_data = np.sign(data)*((np.log(1+(mu*np.abs(data))))/(np.log(1+mu)))
    return comp_data


def mu_law_decompress(data):
    mu = 255
    if np.issubdtype(data.dtype, np.integer) or np.issubdtype(data.dtype, np.unsignedinteger):
        raise Exception("zły typ danych - musi byc float")
    decomp_data = np.sign(data)*(1/mu)*(np.power((1+mu),np.abs(data)) - 1)
    return decomp_data


def DPCM_compress(x, bit):
    y = np.zeros(x.shape)
    e = 0
    for i in range(0, x.shape[0]):
        y[i] = Kwant(x[i]-e, bit)
        e += y[i]
    return y


def DPCM_decompress(y):
    x0 = 0
    x = np.zeros(y.shape)
    for i in range(y.shape[0]):
        x0 = x0 + y[i]
        x[i] = x0
    return x


def DPCM_predict_compress(x,bit,predictor,n):
    y=np.zeros(x.shape)
    xp=np.zeros(x.shape)
    e=0
    for i in range(1,x.shape[0]):
        y[i]=Kwant(x[i]-e,bit)
        xp[i]=y[i]+e
        idx=(np.arange(i-n,i,1,dtype=int)+1)
        idx=np.delete(idx,idx<0)
        e=predictor(xp[idx])
    return y


def DPCM_predict_decompress(y, predictor, n):
    x = np.zeros(y.shape)
    x0 = 0
    for i in range(y.shape[0]):
        x[i] = y[i] + x0
        idx = (np.arange(i - n, i, 1, dtype=int) + 1)
        idx = np.delete(idx, idx < 0)
        x0 = predictor(x[idx])
    return x


x = np.linspace(-1,1,1000)
#y = 0.9*np.sin(np.pi*x*4)
data, fs = sf.read('SM_Lab05/sing_medium1.wav')
#y1 = DPCM_predict_compress(data, 8, np.mean, 3)
#y1 = Kwant(y1,8)
#y2 = DPCM_predict_decompress(y1, np.mean, 3)


# plt.subplot(2,1,1)
# plt.plot(fs,y1)
#
# plt.subplot(2,1,2)
# plt.plot(fs,y2)
# plt.show()

#testy A_law i mu_law
y1 = A_law_compress(data)
y1 = Kwant(y1,1)
y2 = A_law_decompress(y1)

# plt.subplot(2,1,1)
# plt.plot(fs,y1)
#
# plt.subplot(2,1,2)
# plt.plot(fs,y2)
# plt.show()

# sd.play(data, fs)
# stats = sd.wait()

#testy DPCM
# y1 = DPCM_compress(data, 8)
# y2 = DPCM_decompress(y1)
# y1 = DPCM_predict_compress(data, 8, np.mean, 3)
# y2 = DPCM_predict_decompress(y1, np.mean, 3)

sd.play(y2, fs)
stats = sd.wait()
