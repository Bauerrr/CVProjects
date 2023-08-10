//ALG02 IS1 212A LAB05
//Grzegorz Bauer
//bg49206@zut.edu.pl

#include <iostream>
#include <string>
#include <list>
#include <sstream>
#include <iterator>
#include <vector>


using namespace std;

template<typename V>
struct KaV {
public:
	string key;
	V value;

	KaV(string k, V val) {
		key = k;
		value = val;
	}
	KaV() {}
};


template<typename V>
class Tablica {
public:
	int rozmiar;
	V* tab;
	int flag;
	bool re;


	Tablica() :rozmiar(1), tab(new V[rozmiar]), flag(0), re(0) {
	}

	~Tablica() {
		delete[] tab;
	}


	//funkcja w tym zadaniu nieu¿ywana
	void add(V dane) {
		if (flag < rozmiar*0.75) {

			this->tab[flag] = dane;
			this->flag += 1;
		}
		else {

			V* tab2 = new V[rozmiar * 2];
			for (int i = 0; i < rozmiar; i++) {
				tab2[i] = this->tab[i];
			}
			this->rozmiar = this->rozmiar * 2;
			delete[] tab;
			this->tab = tab2;
			this->tab[flag] = dane;
			this->flag += 1;
			
		}
	}
	
	void add_index(V dane, int index) {
		if (flag < rozmiar * 0.75) {

			this->tab[index] = dane;
			this->flag += 1;
		}
		else {

			V* tab2 = new V[rozmiar * 2];
			for (int i = 0; i < rozmiar; i++) {
				tab2[i] = this->tab[i];
			}
			this->rozmiar = this->rozmiar * 2;
			delete[] tab;
			this->tab = tab2;
			this->tab[index] = dane;
			this->flag += 1;
			this->re = 1;
		}
	}

	
	int check() {
		if (flag > rozmiar * 0.75) {
			V* tab2 = new V[rozmiar * 2];
			for (int i = 0; i < rozmiar; i++) {
				tab2[i] = this->tab[i];
			}
			this->rozmiar = this->rozmiar * 2;
			delete[] tab;
			this->tab = tab2;
			//this->flag += 1;
			return 1;
		}
		return 0;
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

	V ret_index(int index) {
		if (index >= rozmiar) {
			cout << "indeks poza tablica" << endl;
			return 1;
		}
		return this->tab[index];
	}

	int change_index(int index, V dane) {
		if (index >= rozmiar) {
			cout << "indeks poza tablica" << endl;
			return 1;
		}
		this->tab[index] = dane;
		return 0;
	}

	void clean() {
		delete[] tab;
		this->tab = new V[rozmiar];
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



template<typename V>
struct HTable {
	
	Tablica<list<KaV<V>>> tablica;
	HTable() {};
		
	int hash(KaV<V> a) {
		int q = a.key.length();
		int n = tablica.rozmiar;
		int h = 0;
		for (int i = 0; i < q; i++) {
			h += int(a.key[i]) * pow(31, q - (i + 1));
		}
		h = abs(h) % n;
		return h;
	}
	
	void re_hash() {
		list<KaV<V>>* tab2 = new list<KaV<V>>[tablica.rozmiar];
		list<KaV<V>> temp;
		for (int i = 0; i < tablica.rozmiar; i++) {
			for (int j = tablica.tab[i].size(); j > 0; j--) {
				auto it = tablica.tab[i].begin();
				KaV<V> k1(it->key, it->value);
				temp.push_front(k1);
				tablica.tab[i].pop_front();
			}
		}
		for (int i = 0; i < tablica.rozmiar; i++) {
			list<KaV<V>> l;
			tab2[i] = l;
		}
		int x = temp.size();
		for (int i = 0; i < x; i++) {
			auto it = temp.begin();
			KaV<V> k1(it->key, it->value);
			tab2[hash(k1)].push_front(k1);
			temp.pop_front();
		}
		this->tablica.tab = tab2;
	}

	void add(KaV<V> a) {
		tablica.flag += 1;
		if (tablica.check()) {
			re_hash();
		}
		tablica.tab[hash(a)].push_front(a);
	}
	
	V search(string a) {
		KaV<V> temp(a, 1);
		int x = hash(temp);
		for (int i = 0; i < tablica.tab[x].size(); i++) {
			auto it = tablica.tab[x].begin();
			advance(it, i);
			if (it->key == a) {
				return it->value;
			}
		}
		return temp.value;
	}

	int del_key(string a) {
		KaV<V> temp(a, 1);
		int x = hash(temp);
		for (int i = 0; i < tablica.tab[x].size(); i++) {
			auto it = tablica.tab[x].begin();
			advance(it, i);
			if (it->key == a) {
				tablica.tab[x].erase(it);
				tablica.flag -= 1;
				return 0;
			}
		}
		return 1;
	}

	void clear_tab() {
		for (int i = 0; i < tablica.rozmiar; i++) {
			tablica.tab[i].clear();
		}
	}

	string to_string() {
		stringstream ss;
		string s;
		ss << "ROZMIAR: " << this->tablica.rozmiar << "\nFLAGA: " << this->tablica.flag << "\nWARTOSCI: " << endl;
		for (int i = 0; i < tablica.rozmiar; i++) {
			int x = tablica.tab[i].size();
			ss << "[" << i << "] = ";
			for (int j = 0; j < x; j++) {
				auto it = tablica.tab[i].begin();
				advance(it, j);
				ss << "(" << it->key << ", " << it->value << "), ";
			}
			ss << endl;
			
		}
		s = ss.str();
		return s;
	}
};

int main() {
	HTable<int> ht1;
	KaV<int> kv1("abc", 12344);
	KaV<int> kv2("cbd", 123746);
	KaV<int> kv3("asdgrtasd", 123544);
	ht1.add(kv1);
	ht1.add(kv2);
	ht1.add(kv3);
	ht1.del_key("abc");
	ht1.clear_tab();
	cout << ht1.to_string() << endl;
}