//ALG02 IS1 212A LAB07
//Grzegorz Bauer
//bg49206@zut.edu.pl
#include <iostream>
#include <sstream>
#include <string>
#include <stdio.h>
#include <time.h>
#include <list>

using namespace std;

template<typename T>
class Tablica {
public:
	int rozmiar;
	T* tab;
	int flag;


	Tablica() :rozmiar(1), tab(new T[rozmiar]), flag(0) {
	}

	~Tablica() {
		delete[] tab;
	}


	void add(T dane) {
		if (flag < rozmiar) {

			this->tab[flag] = dane;
			this->flag += 1;
		}
		else {

			T* tab2 = new T[rozmiar * 2];
			for (int i = 0; i < rozmiar; i++) {
				tab2[i] = this->tab[i];
			}
			this->rozmiar = this->rozmiar * 2;

			this->tab = new T[rozmiar];

			for (int i = 0; i < flag; i++) {
				this->tab[i] = tab2[i];
			}
			this->tab[flag] = dane;
			this->flag += 1;
			delete[] tab2;
		}
	}

	int check() {
		if (flag > 0.75 * rozmiar) {
			T* tab2 = new T[rozmiar * 2];
			for (int i = 0; i < rozmiar; i++) {
				tab2[i] = this->tab[i];
			}
			this->rozmiar = this->rozmiar * 2;
			delete[] tab;
			this->tab = tab2;
			return 1;
		}
		return 0;
	}

	string to_string() {
		stringstream ss;
		string s;
		ss << "ROZMIAR: " << this->rozmiar << "\nFLAGA: " << this->flag << "\nWARTOSCI: " << endl;
		for (int i = 0; i < rozmiar; i++) {
			ss << "[" << i << "] = " << this->tab[i] << endl;
		}
		s = ss.str();
		return s;
	}

	T ret_index(int index) {
		if (index >= rozmiar) {
			cout << "indeks poza tablica" << endl;
			return 1;
		}
		return this->tab[index];
	}

	int change_index(int index, T dane) {
		if (index >= rozmiar) {
			cout << "indeks poza tablica" << endl;
			return 1;
		}
		this->tab[index] = dane;
		return 0;
	}

	void clean() {
		delete[] tab;
		this->tab = new T[rozmiar];
		flag = 0;
	}

	void buble_sort() {
		int x;
		for (int i = 0; i <= flag - 1; i++) {
			for (int j = 1; j <= flag - 1; j++) {

				if (this->tab[j - 1] > this->tab[j]) {
					x = this->tab[j];
					this->tab[j] = this->tab[j - 1];
					this->tab[j - 1] = x;
				}

			}
		}
	}
};

template<typename T>
struct MaxHeap {
public:
	Tablica<T> tablica;

	void add(T a) {
		if (tablica.flag == 0) {
			tablica.tab[0] = a;
			tablica.flag += 1;
			tablica.check();
			return;
		}
		tablica.tab[tablica.flag] = a;
		HeapUp(tablica.flag);
		tablica.flag += 1;
		tablica.check();
	}

	string to_string() {
		return tablica.to_string();
	}

	void HeapUp(int f) {
		bool b = true;
		while (b == true) {
			if (tablica.tab[f] > tablica.tab[(f - 1) / 2] && (f - 1) / 2 < tablica.flag) {
				T temp = tablica.tab[(f - 1) / 2];
				tablica.tab[(f - 1) / 2] = tablica.tab[f];
				tablica.tab[f] = temp;
				f = (f - 1) / 2;
			}
			else {
				return;
			}
		}
	};

	void HeapDown(int f) {
		bool b = true;
		while (b == true) {
			int f2 = f;
			while(tablica.tab[f2] < tablica.tab[2 * f2 + 1] && ((2 * f2) + 1 < tablica.flag)) {
				T temp = tablica.tab[2 * f2 + 1];
				tablica.tab[2 * f2 + 1] = tablica.tab[f2];
				tablica.tab[f2] = temp;
				f2 = 2 * f2 + 1;
			}
			while(tablica.tab[f2] < tablica.tab[2 * f2 + 2] && ((2 * f2) + 2 < tablica.flag)) {
				T temp = tablica.tab[2 * f2 + 2];
				tablica.tab[2 * f2 + 2] = tablica.tab[f2];
				tablica.tab[f2] = temp;
				f2 = 2 * f2 + 2;
			}
			if (f2 == f) {
				return;
			}
			
		}
	};

	void del_root() {
		tablica.tab[0] = tablica.tab[tablica.flag - 1];
		tablica.flag--;
		HeapDown(0);
	}

	void clean() {
		delete tablica.tab;
		tablica.tab = new T[tablica.rozmiar];
		tablica.flag = 0;
	}
};

template <typename T>
void HeapSort(T *th, int size) {
	
	MaxHeap<T> temp;
	for (int i = 0; i < size; i++) {
		temp.add(th[i]);
	}
	
	for (int i = size - 1; i >= 0; i--) {
		th[i] = temp.tablica.tab[0];
		temp.del_root();
	}
	
}


void CountingSort(int* A, int size, int NMAX) {
	int *C = new int[NMAX];
	int* B = new int[size];
	for (int i = 0; i < NMAX; i++) {
		C[i] = 0;
	}
	for (int i = 0; i < size; i++) {
		C[A[i] - 1] += 1;
	}
	for (int i = 1; i < NMAX; i++) {
		C[i] += C[i - 1];
	}
	for (int i = size - 1; i >= 0; i--) {
		B[C[A[i] - 1] - 1] = A[i];
		C[A[i] - 1] -= 1;
	}
	for (int i = 0; i < size; i++) {
		A[i] = B[i];
	}
}

template<typename T>
void BucketSort(T* tb, int size) {
	int min = tb[0];
	int max = tb[0];
	for (int i = 0; i < size; i++) {
		if (tb[i] < min) {
			min = tb[i];
		}
		if (tb[i] > max) {
			max = tb[i];
		}
	}
	list<T> *B = new list<T>[size];
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			if (j == 0) {
				if (tb[i] >= min && tb[i] <= float(max * (float(j + 1) / size))) {
					B[j].push_back(tb[i]);
				}
			}
			else {
				float rg1 = max * (float(j) / size);
				float rg2 = max * (float(j + 1) / size);
				if (tb[i] > rg1 && tb[i] <= rg2) {
					B[j].push_back(tb[i]);
				}
			}
		}
	}
	list<T> temp;
	for (int i = 0; i < size; i++) {
		B[i].sort();
		for (int j = 0; j < B[i].size(); j++) {
			if (B[i].empty() == false) {
				temp.push_back(B[i].front());
				B[i].pop_front();
			}
		}
	}
	for (int i = 0; i < size; i++) {
		if (!temp.empty()) {
			tb[i] = temp.front();
			temp.pop_front();
		}
	}
}

int main() {
	int THeap[7] = { 4,5,6,23,21,8,14 };
	int TCounting[7] = { 2,1,3,6,5,7,9 };
	int TBucket[7] = { 1,2,5,7,4,3,6 };
	HeapSort(THeap, 7);
	cout << "HeapSort: " << endl;
	for (int i = 0; i < 7; i++) {
		cout << THeap[i] << endl;
	}

	cout << "Counting Sort: " << endl;
	CountingSort(TCounting, 7, 10);
	for (int i = 0; i < 7; i++) {
		cout << TCounting[i] << endl;
	}

	cout << "Bucket Sort: " << endl;
	BucketSort(TBucket, 7);
	for (int i = 0; i < 7; i++) {
		cout << TBucket[i] << endl;
	}
}