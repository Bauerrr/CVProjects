//ALG02 IS1 212A LAB06
//Grzegorz Bauer
//bg49206@zut.edu.pl
#include <iostream>
#include <sstream>
#include <string>
#include <stdio.h>
#include <time.h>


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
			if (tablica.tab[f] > tablica.tab[(f - 1) / 2] && (f-1)/2 < tablica.flag) {
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
			if (tablica.tab[f] < tablica.tab[2*f+1] && 2*f+1 < tablica.flag) {
				T temp = tablica.tab[2*f+1];
				tablica.tab[2*f+1] = tablica.tab[f];
				tablica.tab[f] = temp;
				f = 2*f+1;
			}
			else if (tablica.tab[f] < tablica.tab[2 * f + 2] && 2*f+2 < tablica.flag) {
				T temp = tablica.tab[2 * f + 2];
				tablica.tab[2 * f + 2] = tablica.tab[f];
				tablica.tab[f] = temp;
				f = 2 * f + 2;
			}
			else {
				return;
			}
		}
	};

	void del_root() {
		tablica.tab[0] = tablica.tab[tablica.flag-1];
		tablica.flag--;
		HeapDown(0);
	}

	void clean() {
		delete tablica.tab;
		tablica.tab = new T[tablica.rozmiar];
		tablica.flag = 0;
	}
};


int main() {
	MaxHeap<int> MH1;
	for (int i = 0; i <= 10; i++) {
		MH1.add(i);
	}
	//MH1.clean();
	MH1.del_root();
	cout << MH1.to_string() << endl;
}