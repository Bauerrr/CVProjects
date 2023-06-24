import numpy as np
import cv2
import matplotlib.pyplot as plt

# img1 = plt.imread("SM_Lab03/0001.jpg")
# print(img1[:,0])

img= np.zeros((3,3,3),dtype=np.uint8)
img[1,1,:]=255
#print(img[1,1,:])
# print(img.shape)
# plt.imshow(img)
# plt.show()

def nearest_neighbour(img, scale: float):
    #pixels = img.shape[0]*img.shape[1]
    new_p1 = np.ceil(img.shape[0]*scale).astype(int)
    new_p2 = np.ceil(img.shape[1]*scale).astype(int)
    #p_scaled = np.ceil(img.shape[0]*scale).astype(int)
    #print(p_scaled)
    X = np.linspace(0, img.shape[0]-1, new_p1)
    Y = np.linspace(0, img.shape[1]-1, new_p2)
    print(X)
    new_img = np.zeros((new_p1, new_p2, 3), dtype=np.uint8)

    for i in range(0,new_p1):
        for j in range(0,new_p2):
            x = np.round(X[i]).astype(int)
            y = np.round(Y[j]).astype(int)
            #print(i, j, x)
            new_img[i,j] = img[x,y]
    return new_img


def bilinear_interpolation(img, scale: float):
    new_p1 = np.ceil(img.shape[0]*scale).astype(int)
    new_p2 = np.ceil(img.shape[1]*scale).astype(int)
    X = np.linspace(0, img.shape[0]-1, new_p1)
    Y = np.linspace(0, img.shape[1]-1, new_p2)
    new_img = np.zeros((new_p1, new_p2, 3), dtype=np.uint8)
    for i in range(0,new_p1):
        for j in range(0,new_p2):
            x1 = np.floor(X[i]).astype(int)
            x2 = np.ceil(X[i]).astype(int)
            y1 = np.floor(Y[j]).astype(int)
            y2 = np.ceil(Y[j]).astype(int)
            f00 = img[x1,y1]
            f11 = img[x2,y2]
            f01 = img[x1,y2]
            f10 = img[x2,y1]
            x = X[i] - x1
            y = Y[j] - y1
            new_img[i,j] = (f00 * (1-x)*(1-y)) + (f10*x*(1-y)) + (f01*(1-x)*y) + (f11*x*y)
    return new_img


def mean_downscaling(img, scale: float):
    new_p1 = np.ceil(img.shape[0]*scale).astype(int)
    new_p2 = np.ceil(img.shape[1]*scale).astype(int)
    X = np.linspace(0, img.shape[1]-1, new_p2)
    Y = np.linspace(0, img.shape[0]-1, new_p1)
    print(X.shape, Y.shape, img.shape)
    new_img = np.zeros((new_p1, new_p2, 3), dtype=np.uint8)
    print(new_img.shape)
    for i in range(0,new_p1):
        if i+1 >= Y.shape[0]:
            iy = np.round(Y[i] + np.arange(-(Y[i] - Y[i - 1]) / 2, 0)).astype(int)
        elif i == 0:
            iy = np.round(Y[i] + np.arange(0, (Y[i + 1] - Y[i]) / 2 + 1)).astype(int)
        else:
            iy = np.round(Y[i] + np.arange(-(Y[i] - Y[i - 1]) / 2, (Y[i + 1] - Y[i]) / 2 + 1)).astype(int)

        for j in range(0,new_p2):
            if j+1 >= X.shape[0]:
                ix = np.round(X[j] + np.arange(-(X[j] - X[j - 1]) / 2, 0)).astype(int)
            elif j == 0:
                ix = np.round(X[j] + np.arange(0, (X[j + 1] - X[j]) / 2 + 1)).astype(int)
            else:
                ix=np.round(X[j]+np.arange(-(X[j]-X[j-1])/2,(X[j+1]-X[j])/2+1)).astype(int)

            # mean = np.mean(np.mean(img[np.ix_(iy,ix)], axis=0),axis=0)
            mean = np.mean(img[np.ix_(iy, ix)], axis=[0, 1])

            #print(mean)
            #print(img[np.ix_(ix,iy)])
            new_img[i,j] = mean
    return new_img.astype(int)


def median_downscaling(img, scale: float):
    new_p1 = np.ceil(img.shape[0] * scale).astype(int)
    new_p2 = np.ceil(img.shape[1] * scale).astype(int)
    X = np.linspace(0, img.shape[1] - 1, new_p2)
    Y = np.linspace(0, img.shape[0] - 1, new_p1)
    #print(X.shape, Y.shape, img.shape)
    new_img = np.zeros((new_p1, new_p2, 3), dtype=np.uint8)
    for i in range(0, new_p1):
        if i + 1 >= Y.shape[0]:
            iy = np.round(Y[i] + np.arange(-(Y[i] - Y[i - 1]) / 2, 0)).astype(int)
        elif i == 0:
            iy = np.round(Y[i] + np.arange(0, (Y[i + 1] - Y[i]) / 2 + 1)).astype(int)
        else:
            iy = np.round(Y[i] + np.arange(-(Y[i] - Y[i - 1]) / 2, (Y[i + 1] - Y[i]) / 2 + 1)).astype(int)

        for j in range(0, new_p2):
            if j + 1 >= X.shape[0]:
                ix = np.round(X[j] + np.arange(-(X[j] - X[j - 1]) / 2, 0)).astype(int)
            elif j == 0:
                ix = np.round(X[j] + np.arange(0, (X[j + 1] - X[j]) / 2 + 1)).astype(int)
            else:
                ix = np.round(X[j] + np.arange(-(X[j] - X[j - 1]) / 2, (X[j + 1] - X[j]) / 2 + 1)).astype(int)

            # median = np.median(np.median(img[np.ix_(iy, ix)], axis=0), axis=0)
            median = np.median(img[np.ix_(iy, ix)], axis=[0, 1])

            #print(median)
            # print(img[np.ix_(ix,iy)])
            new_img[i, j] = median
    return new_img.astype(int)


def weighted_avg_downscaling(img , scale: float, weights: list = [1,1,1]):
    new_p1 = np.ceil(img.shape[0] * scale).astype(int)
    new_p2 = np.ceil(img.shape[1] * scale).astype(int)
    X = np.linspace(0, img.shape[1] - 1, new_p2)
    Y = np.linspace(0, img.shape[0] - 1, new_p1)
    print(X.shape, Y.shape, img.shape)
    new_img = np.zeros((new_p1, new_p2, 3), dtype=np.uint8)
    for i in range(0, new_p1):
        if i + 1 >= Y.shape[0]:
            iy = np.round(Y[i] + np.arange(-(Y[i] - Y[i - 1]) / 2, 0)).astype(int)
        elif i == 0:
            iy = np.round(Y[i] + np.arange(0, (Y[i + 1] - Y[i]) / 2 + 1)).astype(int)
        else:
            iy = np.round(Y[i] + np.arange(-(Y[i] - Y[i - 1]) / 2, (Y[i + 1] - Y[i]) / 2 + 1)).astype(int)

        for j in range(0, new_p2):
            if j + 1 >= X.shape[0]:
                ix = np.round(X[j] + np.arange(-(X[j] - X[j - 1]) / 2, 0)).astype(int)
            elif j == 0:
                ix = np.round(X[j] + np.arange(0, (X[j + 1] - X[j]) / 2 + 1)).astype(int)
            else:
                ix = np.round(X[j] + np.arange(-(X[j] - X[j - 1]) / 2, (X[j + 1] - X[j]) / 2 + 1)).astype(int)

            #w_avg = np.average(np.average(img[np.ix_(iy, ix)], axis=0),axis=1, weights=weights)
            R = img[:,:,0]
            #print(R[np.ix_(iy, ix)])
            w_avg_R = np.sum(np.sum(R[np.ix_(iy, ix)], axis=0)*weights[0] / len(R[np.ix_(iy,ix)])*weights[0])*weights[0]/len(R[np.ix_(iy,ix)])*weights[0]
            #print("--------------------")
            G = img[:,:,1]
            w_avg_G = np.sum(np.sum(G[np.ix_(iy, ix)], axis=0)*weights[1] / len(G[np.ix_(iy,ix)])*weights[1])*weights[1]/len(G[np.ix_(iy,ix)])*weights[1]
            B = img[:, :, 2]
            w_avg_B = np.sum(np.sum(B[np.ix_(iy, ix)], axis=0) * weights[2] / len(B[np.ix_(iy,ix)])*weights[2])*weights[2]/len(B[np.ix_(iy,ix)])*weights[2]
            #print(w_avg)
            # print(img[np.ix_(ix,iy)])
            new_img[i,j,0] = w_avg_R
            new_img[i, j, 1] = w_avg_G
            new_img[i, j, 2] = w_avg_B
    return new_img.astype(int)

# new_img = nearest_neighbour(img, 5)
# plt.imshow(new_img)
# plt.show()
#
# new_img = bilinear_interpolation(img, 5)
# plt.imshow(new_img)
# plt.show()
#
img2 = plt.imread('SM_Lab03/0007.jpg')
# y2= 0.2126*img2[:,:,0] + 0.7152 * img2[:,:,1] + 0.0722 * img2[:,:,2]
#
# img2 = img2[300:500, 300:500]
# plt.subplot(2,4,1)
# plt.imshow(img2)
# #print(img2.shape)
# new_img = mean_downscaling(img2, 0.4)
# #print(new_img)
# plt.subplot(1,4,2)
# plt.imshow(new_img)
# plt.title("mean")
# plt.subplot(1,4,3)
# new_img = median_downscaling(img2, 0.4)
# plt.imshow(new_img)
# plt.title("median")
# plt.subplot(1,4,4)
# new_img = weighted_avg_downscaling(img2, 0.4)
# plt.imshow(new_img)
# plt.title("weighted average")
# plt.show()

# Zadanie 2:
# Powiększanie
# img = plt.imread("SM_Lab03/0001.jpg")
# plt.subplot(1,3,1)
# plt.imshow(img)
# new_img_nn = nearest_neighbour(img, 10)
# plt.subplot(1,3,2)
# plt.imshow(new_img_nn)
# plt.title("nearest neighbour")
# new_img_bi = bilinear_interpolation(img, 10)
# plt.subplot(1,3,3)
# plt.imshow(new_img_bi)
# plt.title("bilinear interpolation")
# plt.show()

# Pomniejszanie


img = plt.imread("SM_Lab03/0007.jpg")
skala = 0.4
plt.subplot(2,4,1)
plt.imshow(img)
plt.xlim([300,600])
plt.ylim([600,300])
plt.subplot(2,4,5)
edge = cv2.Canny(img, 60, 120)
plt.imshow(edge)
plt.xlim([300,600])
plt.ylim([600,300])

plt.subplot(2,4,2)
new_img_mean = mean_downscaling(img, skala).astype(np.uint8)
plt.imshow(new_img_mean)
plt.title("mean")
plt.xlim([300*skala,600*skala])
plt.ylim([600*skala,300*skala])
plt.subplot(2,4,6)
edge_mean = cv2.Canny(new_img_mean, 60, 120)
plt.imshow(edge_mean)
plt.xlim([300*skala,600*skala])
plt.ylim([600*skala,300*skala])

new_img_median = median_downscaling(img, skala).astype(np.uint8)
plt.subplot(2,4,3)
plt.imshow(new_img_median)
plt.title("median")
plt.xlim([300*skala,600*skala])
plt.ylim([600*skala,300*skala])
plt.subplot(2,4,7)
edge_median = cv2.Canny(new_img_median, 60, 120)
plt.imshow(edge_median)
plt.xlim([300*skala,600*skala])
plt.ylim([600*skala,300*skala])

new_img_avg = weighted_avg_downscaling(img, skala).astype(np.uint8)
plt.subplot(2,4,4)
plt.imshow(new_img_avg)
plt.title("average")
plt.xlim([300*skala,600*skala])
plt.ylim([600*skala,300*skala])
plt.subplot(2,4,8)
edge_avg = cv2.Canny(new_img_avg, 60, 120)
plt.imshow(edge_avg)
plt.xlim([300*skala,600*skala])
plt.ylim([600*skala,300*skala])
plt.show()


nn_new = nearest_neighbour(img, skala)
bi_new = bilinear_interpolation(img, skala)
plt.subplot(2,3,1)
plt.imshow(img)
plt.xlim([300,600])
plt.ylim([600,300])

plt.subplot(2,3,2)
plt.imshow(nn_new)
plt.title("nearest neighbour")
plt.xlim([300*skala,600*skala])
plt.ylim([600*skala,300*skala])
plt.subplot(2,3,3)
plt.imshow(bi_new)
plt.title("bilinear interpolation")
plt.xlim([300*skala,600*skala])
plt.ylim([600*skala,300*skala])

edge_nn = cv2.Canny(nn_new, 60, 120)
edge_bi = cv2.Canny(bi_new, 60, 120)
plt.subplot(2,3,4)
plt.imshow(edge)
plt.xlim([300,600])
plt.ylim([600,300])
plt.subplot(2,3,5)
plt.imshow(edge_nn)
plt.xlim([300*skala,600*skala])
plt.ylim([600*skala,300*skala])
plt.subplot(2,3,6)
plt.imshow(edge_bi)
plt.xlim([300*skala,600*skala])
plt.ylim([600*skala,300*skala])
plt.show()