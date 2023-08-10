//SO IS1 212A LAB08
//Grzegorz Bauer
//bg49206@zut.edu.pl
#include <unistd.h>
#include <sys/wait.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, char **argv){

if(argc != 2 || strlen(argv[1]) > 20 || strlen(argv[1]) < 1){
    //int e = errno;
    fprintf(stderr, "Proces zakonczyl sie niepowodzeniem \n");
    return 1;
}
for(int i =0; i < strlen(argv[1]); i++){
    if(!isdigit(argv[1][i])){
        fprintf(stderr,"Podany argument nie jest liczba \n");
        return 1;
    }
}

char *arg1;
char *arg2;
if(strlen(argv[1]) % 2 == 0){
    int half = strlen(argv[1]) / 2;
    arg1 = (char*)malloc(half*sizeof(char)+1);
    arg2 = (char*)malloc(half*sizeof(char)+1);
}else{
    int half = strlen(argv[1])/2;
    arg1 = (char*)malloc(half*sizeof(char)+1);
    arg2 = (char*)malloc((half+2)*sizeof(char));
}


if(strlen(argv[1]) == 1){
    //printf("%s \n", argv[1]);
    return (int)*argv[1];
}else{
    for(int i = 0; i < strlen(argv[1]); i++){
        //printf("i: %d", i);
        int half = strlen(argv[1])/2;
        //printf("half: %d \n", half);
        if(i < half){
            arg1[i] = argv[1][i];
            //printf("i1: %d \n", i);
        }else{
            arg2[i-half] = argv[1][i];
            //printf("i2: %d \n",i);
        }
    }
}
//printf("arg1: %s \n", arg1);
//printf("arg2: %s \n", arg2);

int c1;
c1 = fork();
//jesli jest dzieckiem
if(c1 ==0){
    execl(argv[0],"./lab8", arg1, NULL);
    return 147;
}
int c2;
c2 = fork();
if(c2==0){
    execl("./lab8","./lab8",arg2,NULL);
    return 148;
}
int c1ex=0;
int c2ex=0;
waitpid(c1,&c1ex,0);
waitpid(c2,&c2ex,0);
int c1exit = (WEXITSTATUS(c1ex)&0xf);
int c2exit = (WEXITSTATUS(c2ex)&0xf);
printf("%d %d %5s %d \n", getpid(),c1,arg1, c1exit);
printf("%d %d %5s %d \n", getpid(), c2,arg2, c2exit);
int x = c1exit + c2exit;
return x;
}
