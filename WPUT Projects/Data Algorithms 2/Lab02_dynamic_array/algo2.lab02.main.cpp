//ALG02 IS1 212A LAB02
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

	
	Tablica():rozmiar(1),tab(new T[rozmiar]),flag(0) {
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

	string to_string() {
		stringstream ss;
		string s;
		ss << "ROZMIAR: " << this->rozmiar << "\nFLAGA: " << this->flag << "\nWARTOSCI: ";
		for (int i = 0; i < rozmiar; i++) {
			ss << "[" << i << "] = " << this->tab[i] << ", ";
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
		for(int i = 0; i <= flag-1; i++) {
			for(int j = 1; j <= flag-1; j++) {
			
				if (this->tab[j-1] > this->tab[j]) {
					x = this->tab[j];
					this->tab[j] = this->tab[j-1];
					this->tab[j-1] = x;
				}
				
			}
		}
	}
};


int main() {
	
	Tablica<int>* t1 = new Tablica<int>();
	string wypis;
	int n = pow(10, 7);
	clock_t c1 = clock();
	for (int i = 0; i <= n; i++) {
		t1->add(i);
	}
	clock_t c2 = clock();
	cout << c2 - c1 << endl;
	delete t1;
}