import numpy as np
import matplotlib.pyplot as plt
import sys
from tqdm import tqdm


def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj,np.ndarray):
        size=obj.nbytes
    elif isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


def RLE_compress(data):
    x = np.array([len(data.shape)])
    x = np.concatenate([x,data.shape])
    x1D = data.copy()
    x1D = x1D.flatten()
    out_array = np.empty(2*x1D.shape[0])
    counter = 1
    first = x1D[0]
    second = 0
    j = 0
    for i in tqdm(range(len(x1D)-1)):
        second = x1D[i+1]
        if second == first:
            counter += 1
            # if i == len(x1D)-1:
            #     out_array[j] = counter
            #     j+=1
            #     out_array[j] = first
            #     j+=1
        else:
            out_array[j] = counter
            j+=1
            out_array[j] = first
            j+=1
            first = second
            counter = 1
    out_array[j] = counter
    j+=1
    out_array[j] = first
    j+=1
    out_array = out_array[:j]
    out_array = np.concatenate([x, out_array ])
    #print(out_array[1:(out_array[0].astype(int)+1)])
    return out_array


def RLE_decompress(data):
    OG_shape = data[1:(data[0].astype(int)+1)]
    comp_data = data[(data[0].astype(int)+1):].astype(int)
    prod_og = np.prod(OG_shape)
    decomp_array = np.empty(prod_og.astype(int))
    for i in range(0,len(comp_data),2):
        count = comp_data[i]
        num = comp_data[i+1]


def BR_compress(data):
    pass


def BR_decompress(data):
    pass


# img = plt.imread('pictures/rysunek_techniczny.jpg')
img = np.array([1,1,1,1,2,1,1,1,1,2,1,1,1,1])
img = img.astype(int)
img2 = RLE_compress(img)
img3 = RLE_decompress(img2)
print(img2.astype(int))

