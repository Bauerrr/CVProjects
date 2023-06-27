import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import skimage
import scipy.ndimage

#Dyskretyzacja
def dyskretyzacja(f,fs):
    t = np.arange(0,1,1/fs)
    s = np.sin(2*np.pi*f*t)
    plt.figure()
    plt.plot(t,s)
    plt.title(f'{fs} Hz')
    plt.show()
    return s, t

# dyskretyzacja(10,20)
# dyskretyzacja(10,21)
# dyskretyzacja(10,30)
# dyskretyzacja(10,45)
# dyskretyzacja(10,50)
# dyskretyzacja(10,100)
# dyskretyzacja(10,150)
# dyskretyzacja(10,200)
# dyskretyzacja(10,250)
# dyskretyzacja(10,1000)
#4: Czy istnieje twierdzenie, które określa z jaką częstotliwością należy próbkować, aby móc wiernie odtworzyć sygnał? Jak się nazywa?
# Jest to twierdzenie Nyquista–Shannona
#5: Jak nazywa się zjawisko, które z powodu błędnie dobranej częstotliwości próbkowania powoduje błędną interpretację sygnału?
# Aliasing

#Kwantyzacja
img = mpimg.imread('aliasing.png')


#2:
print(img.ndim)

#3:
print(img.shape[2])

#4:
#Wyznaczenie jasności piksela
wjp = (np.max(img,axis=-1, keepdims=1) + np.min(img,axis=-1, keepdims=1))/2


#Uśrednienie wartości piksela
uwp = img.mean(axis=-1,keepdims=1)


#Wyznaczenie luminacji piskela
wlp = img[:,:,0]*0.21 + img[:,:,1]*0.72 + img[:,:,2]*0.07


#5: Wygeneruj histogram dla każdego z otrzymanych „szarych” obrazów (funkcja histogram z pakietu numpy)
hwjp = np.histogram(wjp)
huwp = np.histogram(uwp)
hwlp = np.histogram(wlp)

#6: Dla dowolnego z wygenerowanych obrazów, za pomocą parametru bins zredukuj liczbę kolorów na histogramie do 16 i wyświetl zakresy nowych kolorów
hwjp16 = np.histogram(wjp,bins=16)
print(hwjp16)

#7: Stwórz kolejną macierz (obrazek) ze zredukowaną liczbą kolorów (jako nową wartość piksela przyjmnij środek przedziału zwróconego przez funkcję histogramu)
md=np.median(np.histogram(wlp)[0])
hwlpmd = np.histogram(wlp,bins=int(md))

#8: Wyświetl wszystkie obrazy i ich histogramy
plt.figure()
plt.imshow(img)
plt.title("Oryginalny obraz")
plt.show()

plt.figure()
plt.imshow(wjp)
plt.title("Wyznaczenie jasności piksela")
plt.show()

plt.figure()
plt.imshow(uwp)
plt.title("Uśrednienie wartości piksela")
plt.show()

plt.figure()
plt.imshow(wlp)
plt.title("Wyznaczenie luminacji piksela")
plt.show()

plt.figure()
plt.hist(hwjp)
plt.title("Histogram dla wyznaczenie jasności piksela")
plt.show()

plt.figure()
plt.hist(huwp)
plt.title("Histogram dla uśrednienie wartości piksela")
plt.show()

plt.figure()
plt.hist(hwlp)
plt.title("Histogram dla wyznaczenie luminacji piksela")
plt.show()

plt.figure()
plt.hist(hwjp16)
plt.title("Histogram dla wyznaczenie jasności piksela dla 16 kolorów")
plt.show()

plt.figure()
plt.hist(hwlpmd)
plt.title("Histogram dla wyznaczenie luminacji piksela do zadania 7")
plt.show()

#Binaryzacja
img4 = mpimg.imread('ad_lab4_4.png')

#2: Wczytaj obraz, zamień go na skalę szarości za pomocą jednej z wcześniej stosowanych metod i wygeneruj histogram
img4g = img4.mean(axis=-1, keepdims=1)
img4ghist = np.histogram(img4g)

#3: Napisz funkcję, która na podstawie histogramu określi punkt progo-wania (zazwyczaj lokalne minimum między dwoma
# ‘klasami‘ kolorów, tak jak na poniższym obrazku’
def f43(h : np.histogram):
    return np.min(h[1])

#4: Zbinaryzuj (ustaw wartości na 0 lub 1) wartości pikseli obrazka zgodnie z otrzymanym progiem
img44 = np.where(img4g>f43(img4ghist),1,0)

#5: Wyświetl obraz z wysegmentowanym obiektem (segmentacja, czyli usunięcie niepotrzebnych elementów,
# jak np. tła i uwypukleniu tych ważniejszych)
mf = scipy.ndimage.median_filter(img4, size=3)
th = skimage.filters.threshold_otsu(mf)
img45 = np.uint8(mf>th)*255
plt.figure()
plt.imshow(img45)
plt.show()
