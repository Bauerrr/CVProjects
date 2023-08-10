//SO IS1 212A LAB09
//Grzegorz Bauer
//bg49206@zut.edu.pl
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <process.h>
#include <Windows.h>

int main(int argc, char** argv) {

	if (argc != 2 || strlen(argv[1]) > 20 || strlen(argv[1]) < 1) {
		fprintf(stderr, "Proces zakonczyl sie niepowodzeniem \n");
		return 1;
	}
	for (int i = 0; i < strlen(argv[1]); i++) {
		if (!isdigit(argv[1][i])) {
			fprintf(stderr, "Podany argument nie jest liczba \n");
			return 1;
		}
	}

	char arg1[10] = { 0 };
	char arg2[10] = { 0 };

	if (strlen(argv[1]) == 1) {
		//printf("%s \n", argv[1]);
		return *argv[1] - '0';
	}
	else {
		for (int i = 0; i < strlen(argv[1]); i++) {
			//printf("i: %d", i);
			int half = strlen(argv[1]) / 2;
			//printf("half: %d \n", half);
			if (i < half) {
				arg1[i] = argv[1][i];
				//printf("i1: %d \n", i);
			}
			else {
				arg2[i - half] = argv[1][i];
				//printf("i2: %d \n",i);
			}
		}
	}
	STARTUPINFO si;
	PROCESS_INFORMATION pi[2];
	memset(&si, 0, sizeof(si));
	memset(&pi, 0, sizeof(pi));
	si.cb = sizeof(si);
	char argline1[40];
	char argline2[40];
	sprintf(argline1, "49206.so.lab09.exe %s", arg1);
	if (CreateProcessA(NULL, argline1, NULL, NULL, 0, 0, NULL, NULL, &si, pi+0) == 0) {
		return 2;
	};
	sprintf(argline2, "49206.so.lab09.exe %s", arg2);
	if (CreateProcessA(NULL, argline2, NULL, NULL, 0, 0, NULL, NULL, &si, pi + 1) == 0) {
		return 3;
	};

	WaitForSingleObject(pi[0].hProcess, INFINITE);
	WaitForSingleObject(pi[1].hProcess, INFINITE);
	int p0ex;
	int p1ex;
	GetExitCodeProcess(pi[0].hProcess, &p0ex);
	GetExitCodeProcess(pi[1].hProcess, &p1ex);
	//p0ex &= 0xf;
	//p1ex &= 0xf;
	printf("%5d %5d %10s %d \n", GetCurrentProcessId(), pi[0].dwProcessId, arg1, p0ex);
	printf("%5d %5d %10s %d \n", GetCurrentProcessId(), pi[1].dwProcessId, arg2, p1ex);
	int x = p0ex + p1ex;
	CloseHandle(pi[0].hProcess);
	CloseHandle(pi[0].hThread);
	CloseHandle(pi[1].hProcess);
	CloseHandle(pi[1].hThread);
	//printf("%d %d %5s %d \n", GetCurrentProcessId(), GetCurrentProcessId(), argv[1], x);
	return x;
}
