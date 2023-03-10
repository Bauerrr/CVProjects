import numpy as np

# class: HashTable
# chaining: uses built in lists


class HashTable:
    """
    A class for creating hash tables. Uses numpy module

    Attributes:
        hash_function: callable
            takes hashing function and uses it for hashing table.
            Function should take: element to hash, number of rows in hash table

        table_size: int
            designated number of rows in hash table

        dtype: type
            data type for hash table

    Methods:
        put(x):
            takes element to hash and puts it in hash table

        get(x):
            takes element that is already in hash table and finds it.
            If element is tuple or list consisting of key and value it will find value for a given key

        remove(x):
            removes element with a given key or value
    """
    def __init__(self, hash_function: callable, table_size: int, dtype: type):
        self.hf = hash_function
        self.ht_array = np.empty(table_size, dtype=object)
        self.dtype = dtype
        self.size = table_size

    def __str__(self):
        val = ""
        for i in range(len(self.ht_array)):
            val += f'[{i}]: {self.ht_array[i]} \n'
        return val

    def put(self, x):
        if type(x) in [list,tuple] and type(x) is self.dtype:
            if self.ht_array[self.hf(x[0], self.size)] is None:
                self.ht_array[self.hf(x[0], self.size)] = list()
                self.ht_array[self.hf(x[0], self.size)].append(x)
            else:
                self.ht_array[self.hf(x[0], self.size)].append(x)
        elif type(x) is self.dtype:
            if self.ht_array[self.hf(x, self.size)] is None:
                self.ht_array[self.hf(x, self.size)] = list()
                self.ht_array[self.hf(x, self.size)].append(x)
            else:
                self.ht_array[self.hf(x, self.size)].append(x)
        else:
            raise TypeError(f'{type(x)} given {self.dtype} expected.')

    def get(self, x):
        if self.dtype in [list,tuple]:
            for i in range(len(self.ht_array[self.hf(x, self.size)])):
                if self.ht_array[self.hf(x, self.size)][i][0] == x:
                    return self.ht_array[self.hf(x, self.size)][i]
        else:
            if x in self.ht_array[self.hf(x, self.size)]:
                for i in range(len(self.ht_array[self.hf(x, self.size)])):
                    if self.ht_array[self.hf(x, self.size)][i] == x:
                        return self.ht_array[self.hf(x, self.size)][i]

    def remove(self, x):
        if self.dtype in [list,tuple]:
            for i in range(len(self.ht_array[self.hf(x, self.size)])):
                if self.ht_array[self.hf(x, self.size)][i][0] == x:
                    self.ht_array[self.hf(x, self.size)].remove(self.ht_array[self.hf(x, self.size)][i])
        else:
            if x in self.ht_array[self.hf(x, self.size)]:
                for i in range(len(self.ht_array[self.hf(x, self.size)])):
                    if self.ht_array[self.hf(x, self.size)][i] == x:
                        self.ht_array[self.hf(x, self.size)].remove(self.ht_array[self.hf(x, self.size)][i])

def str_hash(x: str, n: int):
    val = np.sum([ord(c) for c in x])
    hash_val = val % n
    return hash_val





