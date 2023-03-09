import numpy as np
import random
# from collections.abc import Callable

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
        pass


def str_hash(x: str, n: int):
    val = np.sum([ord(c) for c in x])
    hash_val = val % n
    return hash_val





#print(str_hash("hi"))
words = ['modbi', 'qupai', 'jexes', 'bagge', 'moxol', 'feziv', 'fadvu', 'jarny', 'kabiv', 'dijij', 'panuy', 'ciqul',
         'gydow', 'hejol', 'gusoj', 'juvek', 'sosow', 'sazub', 'buneg', 'sogup', 'lofah', 'rejep', 'zirux', 'jyxoq',
         'hutaf', 'fopon', 'kewuw', 'jehej', 'voxip', 'tywuc', 'qaxaw', 'rajif', 'vomog', 'quzox', 'liqin', 'lafik',
         'jociv', 'kiwux', 'nurad', 'lofiv', 'pebef', 'jajux', 'qogul', 'qamok', 'cofaz', 'vibiz', 'fubak', 'lajuk',
         'zodam', 'kexap', 'suqup', 'modic', 'gokix', 'fetuz', 'cobal', 'gimov', 'mifow', 'suxav', 'suvub', 'sukup',
         'sifow', 'jusuk', 'rahot', 'wozal', 'quful', 'gufij', 'diluz', 'hyqul', 'fokoj', 'lucuv', 'xucuf', 'wujav',
         'jizux', 'tevoj', 'zeqox', 'pufoc', 'dogex', 'fixik', 'nuxic', 'jawol', 'gafuf', 'kicun', 'fivug', 'lazud',
         'vejik', 'jevox', 'syvob', 'xojol', 'cyzaw', 'keqol', 'xoqep', 'vepox', 'tozuf', 'hifoz', 'buvar', 'molus',
         'xucih', 'xewih', 'zemek', 'qavof']

tup_words = [['556', 'modbi'], ['902', 'qupai'], ['274', 'jexes'], ['997', 'bagge'], ['561', 'moxol'], ['363', 'feziv'],
             ['167', 'fadvu'], ['422', 'jarny'], ['512', 'kabiv'], ['711', 'dijij'], ['353', 'panuy'], ['60', 'ciqul'],
             ['159', 'gydow'], ['771', 'hejol'], ['141', 'gusoj'], ['620', 'juvek'], ['768', 'sosow'], ['92', 'sazub'],
             ['802', 'buneg'], ['244', 'sogup'], ['825', 'lofah'], ['439', 'rejep'], ['780', 'zirux'], ['51', 'jyxoq'],
             ['255', 'hutaf'], ['92', 'fopon'], ['66', 'kewuw'], ['110', 'jehej'], ['289', 'voxip'], ['804', 'tywuc'],
             ['361', 'qaxaw'], ['487', 'rajif'], ['757', 'vomog'], ['194', 'quzox'], ['185', 'liqin'], ['360', 'lafik'],
             ['774', 'jociv'], ['101', 'kiwux'], ['938', 'nurad'], ['661', 'lofiv'], ['587', 'pebef'], ['100', 'jajux'],
             ['196', 'qogul'], ['920', 'qamok'], ['776', 'cofaz'], ['926', 'vibiz'], ['505', 'fubak'], ['270', 'lajuk'],
             ['963', 'zodam'], ['79', 'kexap'], ['398', 'suqup'], ['896', 'modic'], ['891', 'gokix'], ['484', 'fetuz'],
             ['465', 'cobal'], ['456', 'gimov'], ['783', 'mifow'], ['444', 'suxav'], ['696', 'suvub'], ['466', 'sukup'],
             ['277', 'sifow'], ['260', 'jusuk'], ['146', 'rahot'], ['905', 'wozal'], ['173', 'quful'], ['74', 'gufij'],
             ['106', 'diluz'], ['29', 'hyqul'], ['596', 'fokoj'], ['208', 'lucuv'], ['615', 'xucuf'], ['533', 'wujav'],
             ['352', 'jizux'], ['323', 'tevoj'], ['836', 'zeqox'], ['805', 'pufoc'], ['618', 'dogex'], ['305', 'fixik'],
             ['322', 'nuxic'], ['708', 'jawol'], ['504', 'gafuf'], ['202', 'kicun'], ['943', 'fivug'], ['623', 'lazud'],
             ['307', 'vejik'], ['406', 'jevox'], ['472', 'syvob'], ['602', 'xojol'], ['564', 'cyzaw'], ['366', 'keqol'],
             ['630', 'xoqep'], ['593', 'vepox'], ['228', 'tozuf'], ['717', 'hifoz'], ['127', 'buvar'], ['433', 'molus'],
             ['991', 'xucih'], ['590', 'xewih'], ['663', 'zemek'], ['694', 'qavof']]

# key = 0
# for i in words:
#     key = random.randint(0,1000)
#     tup_words.append([str(key), i])
# print(tup_words)
# tab = HashTable(str_hash, 50, str)
# for i in words:
#     tab.put(i)
# print(tab)
for i in tup_words[:][0]:
    print(i)

tab = HashTable(str_hash, 50, list)
for i in tup_words:
    tab.put(i)

print(tup_words[5][0])
print(tab.get('630'))
