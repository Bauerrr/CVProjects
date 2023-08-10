//ALG02 IS1 212A LAB08
//Grzegorz Bauer
//bg49206@zut.edu.pl

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <list>
#include <algorithm>

using namespace std;

struct graph {
	int p1;
	int p2;
	double k;

	void out(){
		cout << p1 << " " << p2 << " " << k << endl;
	}

};

struct UnionFind {
	int* ptab;
	graph* graf;
	int elements;
	//int k;
	double sum = 0;
	int it = 0;
	UnionFind(graph &a, int n) {
		elements = n;
		
		ptab = new int[n];
		for (int i = 0; i < n; i++) {
			ptab[i] = i;
		}
		graf = &a;
	}

	/*void unify(graph* g) {
		int rp1 = find(g->p1);
		int rp2 = find(g->p2);
		if (this->ptab[g->p1] == g->p1 && this->ptab[g->p2] != g->p1) {
			this->ptab[g->p1] = this->ptab[g->p2];
			this->sum += g->k;
			this->it += 1;
			cout << g->p1 << " " << g->p2 << " " << g->k << endl;
		}
		else if (this->ptab[g->p2] == g->p2 && this->ptab[g->p1] != g->p2) {
			this->ptab[g->p2] = this->ptab[g->p1];
			this->sum += g->k;
			this->it += 1;
			cout << g->p1 << " " << g->p2 << " " << g->k << endl;
		}
		else if (this->ptab[g->p1] != g->p1 && this->ptab[g->p2] != g->p2 && this->ptab[g->p1] != this->ptab[g->p2] && rp1 != rp2) {
			ptab[rp1] = rp2;
			this->sum += g->k;
			this->it += 1;
			cout << g->p1 << " " << g->p2 << " " << g->k << endl;
		}
		
	}*/

	void unify(graph* g) {
		int rp1 = find(g->p1);
		int rp2 = find(g->p2);
		if (rp1 != rp2) {
			ptab[rp1] = rp2;
			this->sum += g->k;
			this->it += 1;
			cout << g->p1 << " " << g->p2 << " " << g->k << endl;
		}
	}

	void unifyBR(graph* g) {
		int rp1 = find(g->p1);
		int rp2 = find(g->p2);
		if (rp1 != rp2) {
			int rp1it = 0;
			int rp2it = 0;
			for (int i = 0; i < elements; i++) {
				if (ptab[i] == rp1) {
					rp1it += 1;
				}
				else if (ptab[i] == rp2) {
					rp2it += 1;
				}
			}
			if (rp1it > rp2it) {
				ptab[rp2] = rp1;
			}
			else {
				ptab[rp1] = rp2;
			}
			this->sum += g->k;
			this->it += 1;
			cout << g->p1 << " " << g->p2 << " " << g->k << endl;
		}
	}

	int find(int i) {
		if (i == ptab[i]) return i;
		return find(ptab[i]);
	}
	
	int findPC(int i) {
		if (i == ptab[i]) return i;
		ptab[i] = find(ptab[i]);
		return find(ptab[i]);
	}

	void print() {
		for (int i = 0; i < elements; i++) {
			cout << "[" << i <<"] " << ptab[i] << endl;
		}
		cout << this->sum << endl;
		cout << this->it << endl;
	}
};


bool compareK(graph g1, graph g2) {
	return(g1.k < g2.k);
}

int main() {
	int x = 2;
	int skip;
	string filename;
	switch (x) {
	case 1:
		filename = "g1.txt";
		break;
	case 2:
		filename = "g2.txt";
		break;
	case 3:
		filename = "g3.txt";
		break;
	}
	ifstream file;
	file.open(filename);
	
	if (file.is_open()) {
		string line;
		getline(file, line);
		int n = stoi(line);
		//skipping lines
		for (int i = 0; i <= n; i++) {
			getline(file, line);
		}

		
		int e = stoi(line);
		graph* tab = new graph[e];
		for (int i = 0; i < e; i++) {
			file >> tab[i].p1 >> tab[i].p2 >> tab[i].k;
		}
		file.close();

		sort(tab, tab + e, compareK);
		/*for (int i = 0; i < e; i++) {
			tab[i].out();
		}*/
		//cout << n << "\n" << e;
		UnionFind UF(*tab, n);
		//UF.print();
		int i = 0;
		while (UF.it != n - 1) {
			UF.unify(&tab[i]);
			i++;
		}
		cout << i << endl;
		UF.print();
		//double suma = 0;
		/*for (int j = 0; j < 20; j++) {
			suma += tab[j].k;
		}*/
		//cout << suma << endl;
		//cout << UF.find(5) << endl;
	}
	else {
		cout << "Problem z plikiem";
	}
}