//ALG02 IS1 212A LAB01
//Grzegorz Bauer
//bg49206@zut.edu.pl

#include <iostream>
#include <string>
#include <conio.h>
#include <string>
#include <sstream>


using namespace std;
template <typename T>
struct dane {
public:
	dane<int>* next;
	dane<int>* prev;
	T body;

	
};


template <typename T>
class Lista {
public:
	dane<int>* first;
	dane<int>* last;
	int len;

	Lista() {
		first = NULL;
		last = NULL;
		len = 0;
	}
	~Lista() {
		delete first;
		delete last;
	}


	void add_last(T d) {
		
		if (first == NULL && last == NULL) {
			first = &d;
			last = &d;
			d.prev = NULL;
			d.next = NULL;
			len += 1;
		}
		else if (last != NULL) {
			d.prev = last;
			d.prev->next = &d;
			last = &d;
			len += 1;
			d.next = NULL;
		}
	}
	/*
	void rescale_first() {
		dane<int>* x = last;
		for (int i = len - 1; i >= 0; i--) {
			x = last->prev;
		}
		first = x;
	}
	*/
	void add_first(T d) {
		if (first == NULL && last == NULL) {
			first = &d;
			last = &d;
			d.prev = NULL;
			d.next = NULL;
			len += 1;
		}
		else if (first != NULL) {
			d.next = first;
			first->prev = &d;
			first = &d;
			d.prev = NULL;
			len += 1;
		}
	}

	void del_last() {
		if (last == NULL) {
			cout << "nie mozna usuwac z pustej listy" << endl;
		}
		else {
			last = last->prev;
			last->next = NULL;
			len = len - 1;

		}
	}

	void del_first() {
		if (first == NULL) {
			cout << "nie mozna usuwac z pustej listy" << endl;
		}
		else {
			first = first->next;
			first->prev = NULL;
			len = len - 1;

		}
	}

	
	void show_data(int index) {
		dane<int>* x = new dane<int>();
		if (index >= len) {
			cout << "nie istnieje taki indeks" << endl;
		}
		else if (index == len-1) {
			x = last;
			cout << "dane pod indeksem " << index << ": " << x->body << endl;
		}
		else{
			int i = 0;
			for (i = 0; i <= index; i++) {
				if (i != 0) {
					x = x->next;
				}
				else{
					x = first;
					
				}
			}
			cout << "dane pod indeksem " << index << ": " << x->body << endl;
		}
		//delete x;
	}

	template <typename T>
	void swap_data(int index, T new_data) {
		dane<int>* x = new dane<int>();
		
		if (index >= len) {
			cout << "nie istnieje taki indeks" << endl;
		}
		else if (index == len - 1) {
			last->body =new_data;
		}
		else {
			int i = 0;
			for (i = 0; i <= index; i++) {
				if (i != 0) {
					x = x->next;
				}
				else {
					x = first;

				}
			}
			x->body = new_data;
		}
	}

	template <typename T>
	void search(T s_data) {
		dane<int>* x = new dane<int>();
		int i = 0;
		int y = 0;
		for (i = 0; i <= len-1; i++) {
			if (i != 0) {
				x = x->next;
				y = x->body;
			}
			else {
				x = first;
				y = x->body;

			}

			if ( x->body == s_data) {
				cout << "wynik wyszukiwania: " << x << endl;
				y = 1;
				
			}
		}
		if (y == 0) {
			cout << "nie znaleziono wynikow dla: " << s_data << endl;
		}
	}

	template <typename T>
	void search_del(T s_data) {
		dane<int>* x = new dane<int>();
		int i = 0;
		int y = 0;
		for (i = 0; i <= len - 1; i++) {
			if (i != 0) {
				x = x->next;
				y = x->body;
			}
			else {
				x = first;
				y = x->body;

			}

			if (x->body == s_data) {
				cout << "Usuwanie powiodlo sie "<< endl;
				x->prev->next = x->next;
				x->prev = NULL;
				x->next = NULL;
				len = len - 1;
				y = 1;
				
			}
		}
		if (y == 0) {
			cout << "nie znaleziono wynikow dla: " << s_data << endl;
		}
	}

	void add_index(int index, T d) {
		dane<int>* x = new dane<int>();
		if (index == len - 1) {
			add_last(d);
		}
		else if (index == 0) {
			add_first(d);
		}
		else {
			int i = 0;
			for (i = 0; i <= index; i++) {
				if (i != 0) {
					x = x->next;
				}
				else {
					x = first;

				}
			}
			d.next = x->next;
			x->next->prev = &d;
			x->next = &d;
			d.prev = x;
			len += 1;
			
		}
	}

	void clear_all() {
		first->next->prev = NULL;
		first = NULL;
		last->prev->next = NULL;
		last = NULL;
		len = 0;
	}

	string to_string() {
		string func;
		stringstream ss;
		cout << "len: " << len << endl;
		ss << "len: " << len << endl;
		dane<int>* x = new dane<int>();
		
		int i = 0;
		for (i = 0; i <= len-1; i++) {
			if (i != 0) {
				x = x->next;
				cout << "(" << x << "," << x->body << ") <--> ";
				ss << "(" << x << "," << x->body << ") <--> ";
				if (i == len-1) {
					cout << "(" << x << "," << x->body << ")" << endl;
					ss << "(" << x << "," << x->body << ")" << endl;
				}
			}
			else {
				x = first;
				cout << "(" << x << "," << x->body << ") <--> ";
				ss << "(" << x << "," << x->body << ") <--> ";
			}
			
		}
		func = ss.str();
		return func;
	}

	void show_len() {
		cout << "len: " << len << endl;
		cout << "first: " << first << endl;
		cout << "last: " << last << endl;
	}
};



int main() {
	
	Lista<dane<int>>* l1 = new Lista<dane<int>>();
	dane<int> d1;
	dane<int> d2;
	dane<int> d3;
	dane<int> d4;
	dane<int> d5;
	string listwa;
	d1.body = 23124;
	d2.body = 213425;
	d3.body = 123551;
	d4.body = 223849;
	d5.body = 56712873;
	l1->add_last(d1);
	l1->add_last(d2);
	l1->add_last(d3);
	l1->add_last(d4);
	l1->show_data(0);
	l1->show_data(1);
	l1->show_data(2);
	l1->show_data(3);
	l1->show_data(4);
	l1->show_len();
	l1->swap_data(2, 3758);
	l1->show_len();
	l1->add_last(d5);
	listwa = l1->to_string();
	
	l1->search(23124);
	l1->show_len();
	l1->add_index(3, d2);
	l1->search_del(213425);
	l1->show_data(0);
	l1->show_data(1);
	l1->show_data(2);
	l1->show_data(3);
	l1->show_data(4);
	l1->clear_all();
	l1->show_data(3);
	l1->show_len();

	cout << "\n" << listwa;

	/*
	cout << "d1: "<< &d1 << endl;
	cout << "next: " << &d1.next << endl;
	cout << "prev: " << &d1.prev << endl;
	cout << "body: " << &d1.body << endl;
	*/
	
	getchar();
	getchar();
}