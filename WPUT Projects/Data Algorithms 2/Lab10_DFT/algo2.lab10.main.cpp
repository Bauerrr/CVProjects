//ALG01 IS1 212A LAB10
//Grzegorz Bauer
//bg49206.zut.edu.pl

#include <complex>
#define USE MATH DEFINES
#include <math.h>
#include <iostream>

using namespace std::complex_literals;
//w ramach funkcji przyjmujemy tablicê wielkoœci N (N jest potêg¹ dwójki), i N jako rozmiar tablicy
std::complex<double> *dft(double* f, int N) {
	const double pi = std::acos(-1);
	const std::complex<double> i(0, 1);
	std::complex<double>* c = new std::complex<double>[N];
	double* creal = new double[N];
	double* cimag = new double[N];

	for (int k = 0; k < N; k++) {
		creal[k] = 0;
		cimag[k] = 0;
		for (int n = 0; n < N; n++) {
			//podzia³ na real i imaginary
			creal[k] = creal[k] + (f[n] * cos(2 * pi * k * n / N));
			cimag[k] = cimag[k] + (f[n] * sin(2 * pi * k * n / N));
			//c[k] = c[k] + (f[n] * exp(-2 * pi * k * n / N));
		}
		//std::cout << creal[k] << " + " << cimag[k] << " i" << std::endl;
		std::complex<double> temp(creal[k], cimag[k]);
		c[k] = temp;
	}
	delete[] creal;
	delete[] cimag;
	return c;
}

//std::complex<double>* fft(double* f, int N) {
//	const double pi = std::acos(-1);
//	const std::complex<double> i(0, 1);
//	double* even = new double[N / 2];
//	double* odd = new double[N / 2];
//
//
//	double varR = 0;
//	double varI = 0;
//	std::complex<double>* evenCom = new std::complex<double>[N/2];
//	std::complex<double>* oddCom = new std::complex<double>[N/2];
//	std::complex<double>* c = new std::complex<double>[N];
//	int ej = 0, oj = 0;
//
//	//if (N <= 1) return ;
//	//roz³o¿enie na indeksy parzyste i nieparzyste
//	for (int i = 0; i < N; i++) {
//		if (i % 2 == 0) {
//			even[ej] = f[i];
//			ej++;
//		}
//		else {
//			odd[oj] = f[i];
//			oj++;
//		}
//	}
//	/*for (int i = 0; i < ej; i++) {
//		std::cout << even[i] << std::endl;
//		std::cout << odd[i] << std::endl;
//	}*/
//
//	evenCom = dft(even,N/2);
//	oddCom = dft(odd,N/2);
//	for (int i = 0; i < ej; i++) {
//		std::cout << real(evenCom[i]) << " + " << imag(evenCom[i]) << std::endl;
//		std::cout << real(oddCom[i]) << " + " << imag(oddCom[i]) << std::endl;
//	}
//
//	//sklejanie
//	for (int k = 0; k < N / 2; k++) {
//		std::complex<double> exponent;
//		for (int n = 0; n < N/2; n++) {
//			exponent = exp(2 * pi * k * n / N);
//			
//		}
//		std::complex<double> temp(std::real(evenCom[k]) +  std::real(oddCom[k]), std::imag(evenCom[k])+ std::imag(oddCom[k]));
//		c[k] = temp + exp(-2*pi*k/N);
//		std::complex<double> temp2(std::real(evenCom[k]) + std::real(oddCom[k]), std::imag(evenCom[k]) +std::imag(oddCom[k]));
//		c[k+N/2] = temp2 - exp(-2 * pi * k / N);
//	}
//	delete[] odd;
//	delete[] even;
//	delete[] evenCom;
//	delete[] oddCom;
//	//delete[] cEven;
//	//delete[] cOdd;
//	return c;
//}


//std::complex<double>* fft(double* f, int N) {
//	const double pi = std::acos(-1);
//	//const std::complex<double> i(0, 1);
//	std::complex<double>* c = new std::complex<double>[N];
//	double* even = new double[N / 2];
//	double* odd = new double[N / 2];
//	int ej = 0, oj = 0;
//	
//	if (N <= 1) {
//		std::complex<double>* f2 = (f[0],0);
//		return f2;
//	};
//
//	for (int i = 0; i < N; i++) {
//		if (i % 2 == 0) {
//			even[ej] = f[i];
//			ej++;
//		}
//		else {
//			odd[oj] = f[i];
//			oj++;
//		}
//	}
//	std::complex<double> WnExp = exp((real(2i) / N + imag(2i) / N) * pi / N); // 2i * pi/N;
//
//
//	return c;
//}

int main() {
	const double pi = std::acos(-1);
	//const std::complex<double> i(0, 1);
	int N = 16;
	double* f = new double[N];
	for (int n = 0; n < N; n++) {
		f[n] = n / (double)N;
		//std::cout << f[n] << std::endl;
	}
	std::complex<double>* cDFT = dft(f, N);
	for (int i = 0; i < N; i++) {
		std::cout << std::real(cDFT[i]) << " + " << std::imag(cDFT[i]) << " i" << std::endl;
	}
	//std::complex<double>* cFFT = fft(f, N);
	/*std::cout << std::endl;
	for (int i = 0; i < N; i++) {
		std::cout << std::real(cFFT[i]) << " + " << std::imag(cFFT[i]) << " i" << std::endl;
	}*/
	delete[] f;
	delete[] cDFT;

}
