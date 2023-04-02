import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import scipy


def plot_audio(signal, fs, time_margin=[0,0.02]):
    plt.figure()
    plt.subplot(2,1,1)
    plt.ylabel('dB')
    plt.xlabel('Time[s]')
    plt.xlim(time_margin)
    plt.plot(np.arange(0,signal.shape[0])/fs, signal)
    plt.subplot(2,1,2)
    plt.ylabel('dB')
    plt.xlabel('Hz')
    #print(signal.shape[0])
    btlen = signal.shape[0].bit_length()
    #print(btlen)
    fsize = 2**(btlen+1)
    yf = scipy.fftpack.fft(signal,fsize)
    plt.plot(np.arange(0,fs/2,fs/fsize), 20*np.log10(np.abs(yf[:fsize//2])))
    plt.show()


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


def decimate(signal, n, fs):
    new_signal = signal[::n]
    new_fs = fs/n
    return [new_signal, new_fs]


def interpolate(y, N, N1, nonlin = False):
    x = np.linspace(0,N,N)
    x1 = np.linspace(0,N,N1)
    if nonlin:
        metode_nonlin = interp1d(x,y, kind='cubic')
        y_nonlin = metode_nonlin(x1).astype(y.dtype)
        return y_nonlin, x1
    else:
        metode_lin = interp1d(x,y)
        y_lin = metode_lin(x1).astype(y.dtype)
        return y_lin, x1


test_int8 = np.round(np.linspace(0,255,255,dtype=np.uint8))
test_int32 = np.round(np.linspace(np.iinfo(np.int32).min,np.iinfo(np.int32).max,1000,dtype=np.int32))
test_float32 = np.linspace(-1,1,10000)
#print(Kwant(test_int8, 3))
# kwant_int8 = Kwant(test_int8, 3)
# plt.plot(kwant_int8, np.arange(2**8-1))
# plt.show()

# kwant_int32 = Kwant(test_int32, 2)
# print(kwant_int32)
# plt.plot(kwant_int32, np.linspace(np.iinfo(np.int32).min,np.iinfo(np.int32).max,1000,dtype=np.int32))
# plt.show()

# kwant_float32 = Kwant(test_float32, 2)
# plt.plot(kwant_float32, np.linspace(-1,1,10000, dtype=np.float32))
# plt.show()

# decimate_int8, fs_int8 = decimate(test_int8, 5, 255)
# print(decimate_int8)
# print(fs_int8)

data, fs = sf.read('SM_Lab05/sin_combined.wav', dtype=np.int32)
# kwant_data = Kwant(data, 4)
# plot_audio(data, fs)

for i in (4,8,16,24):
    kwant_data = Kwant(data, i)
    #plot_audio(data, fs, [0,0.0005])
    plot_audio(kwant_data, fs, [0,0.0005])

# for i in (4, 2, 1):
#     dec_data, dec_fs = decimate(data,i,fs)
#     plot_audio(dec_data, dec_fs)

# for i in (2000, 4000, 8000, 16000, 24000, 41000, 16950):
#     interp_data, interp_fsx = interpolate(data, fs, i)
#     plot_audio(interp_data, i, [0, 0.01])

# dec_data, dec_fs = decimate(data, 5, fs)
# plt.plot(np.arange(0,data.shape[0])/fs, data)
# plt.show()

# plt.plot(np.arange(0,dec_data.shape[0])/dec_fs, dec_data)
# plt.show()

#interp_data, interp_fsx = interpolate(data, fs, 35)
# plt.plot(interp_fsx, interp_data)
# plt.show()