import numpy as np
import matplotlib.pyplot as plt


def imgToFloat(img):
    if np.issubdtype(img.dtype, np.integer) or np.issubdtype(img.dtype, np.unsignedinteger):
        img = img/255.0
    return img


def del_alpha(img):
    if img.shape[2] == 4:
        img = img[:,:,0:3]
        print(img)
    return img

def colorFit(pixel, pallet):
    return pallet[np.argmin(np.linalg.norm(pallet - pixel, axis=1))]


def kwant_colorFit(img, pallet):
    out_img = img.copy()
    for w in range(out_img.shape[0]):
        for k in range(out_img.shape[1]):
            #print(img[w,k])
            out_img[w,k] = colorFit(img[w,k], pallet)
    return out_img


def random_dithering(img):
    #do poprawki
    r = np.random.rand(img.shape[0],img.shape[1])
    random_img = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            random_img[i,j] = random_img[i,j] > r[i,j]
    # random_img = random_img > r
    random_img = random_img * 1.0
    return random_img


def organized_dithering(img, pallete):
    r = 1
    M2 = np.array([[0,8,2,10],[12,4,14,6], [3,11,1,9],[15,7,13,5]])
    new_img = img.copy()
    Mpre = (M2+1) / (2*2)**2 - 0.5
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            new_img[i,j] = colorFit(img[i,j]+r*(Mpre[np.mod(i, 2*2), np.mod(j,2*2)]), pallete)
    return new_img


def floyd_steinberg_dithering(img, pallet):
    new_img = img.copy()
    for j in range(img.shape[1]):
        for i in range(img.shape[0]):
            oldpixel = new_img[i,j].copy()
            newpixel = colorFit(oldpixel, pallet)
            new_img[i,j] = newpixel
            quant_error = oldpixel - newpixel
            if i+1 in range(img.shape[0]):
                new_img[i+1,j] = new_img[i+1,j] + quant_error * 7/16
                if j+1 in range(img.shape[1]):
                    new_img[i + 1, j + 1] = new_img[i + 1, j + 1] + quant_error * 1 / 16

            if i-1 in range(img.shape[0]) and j+1 in range(img.shape[1]):
                new_img[i-1, j+1] = new_img[i-1, j+1] + quant_error * 3/16

            if j+1 in range(img.shape[1]):
                new_img[i, j+1] = new_img[i, j+1] + quant_error * 5/16
    return new_img


paleta2 = np.linspace(0,1,2).reshape(2,1)
paleta4 = np.linspace(0,1,4).reshape(4,1)
paleta8 = np.linspace(0,1,8).reshape(8,1)
paleta16 = np.linspace(0,1,16).reshape(16,1)
print(paleta8)

pallet8 = np.array([
    [0.0, 0.0, 0.0,],
    [0.0, 0.0, 1.0,],
    [0.0, 1.0, 0.0,],
    [0.0, 1.0, 1.0,],
    [1.0, 0.0, 0.0,],
    [1.0, 0.0, 1.0,],
    [1.0, 1.0, 0.0,],
    [1.0, 1.0, 1.0,],
])

pallet16 = np.array([
    [0.0, 0.0, 0.0,],
    [0.0, 1.0, 1.0,],
    [0.0, 0.0, 1.0,],
    [1.0, 0.0, 1.0,],
    [0.0, 0.5, 0.0,],
    [0.5, 0.5, 0.5,],
    [0.0, 1.0, 0.0,],
    [0.5, 0.0, 0.0,],
    [0.0, 0.0, 0.5,],
    [0.5, 0.5, 0.0,],
    [0.5, 0.0, 0.5,],
    [1.0, 0.0, 0.0,],
    [0.75, 0.75, 0.75,],
    [0.0, 0.5, 0.5,],
    [1.0, 1.0, 1.0,],
    [1.0, 1.0, 0.0,]
])

special_pallet16 = np.array([
    [156, 155, 156],
    [88, 101, 71],
    [168, 165, 169],
    [141, 143, 145],
    [180, 178, 182],
    [69, 92, 46],
    [19, 21, 14],
    [67, 69, 62],
    [48, 70, 27],
    [36, 37, 35],
    [107, 123, 84],
    [122, 127, 131],
    [104, 110, 108],
    [199, 198, 199],
    [131, 145, 111],
    [221, 218, 216]
])
special_pallet16_float = imgToFloat(special_pallet16)
# print(paleta3)
# print(colorFit(np.array([0.43]), paleta3))
# print(colorFit(np.array([0.66]), paleta3))
# print(colorFit(np.array([0.8]), paleta3))
#
# print(colorFit(np.array([0.25,0.25,0.5]),pallet8))
# print(colorFit(np.array([0.25,0.25,0.5]),pallet16))
img = plt.imread('SM_Lab04/0013.jpg')
img = imgToFloat(img)
img = del_alpha(img)
y2= 0.2126*img[:,:,0] + 0.7152 * img[:,:,1] + 0.0722 * img[:,:,2]
print(y2.shape)
#img = y2
new_img = kwant_colorFit(img, pallet16)
new_img_random = random_dithering(img)
new_img_organized = organized_dithering(img, pallet16)
new_img_fs = floyd_steinberg_dithering(img, pallet16)

plt.subplot(1,5,1)
plt.imshow(img, cmap=plt.cm.gray)
plt.title("oryginal")

plt.subplot(1,5,2)
plt.imshow(new_img, cmap=plt.cm.gray)
plt.title("kwantyzacja")

plt.subplot(1,5,3)
plt.imshow(new_img_random, cmap=plt.cm.gray)
plt.title("losowy")

plt.subplot(1,5,4)
plt.imshow(new_img_organized, cmap=plt.cm.gray)
plt.title("zorganizowany")

plt.subplot(1,5,5)
plt.imshow(new_img_fs, cmap=plt.cm.gray)
plt.title("Floyd-Steinberg")
plt.show()
