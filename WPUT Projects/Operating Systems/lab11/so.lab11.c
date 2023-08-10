//SO IS1 212A LAB11
//Grzegorz Bauer
//bg49206@zut.edu.pl
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <time.h>
#include <malloc.h>
#include <math.h>

#define min(a,b) ((a)<(b)?(a):(b))
#define BILLION  1000000000L;

long double sum = 0;
pthread_mutex_t lock;

void *thr(void *data){
    pthread_mutex_lock(&lock);    
    
    double *a = (double *)data;
    //size_t n = sizeof(a)/sizeof(a[1]);
    //printf("%f %f %f\n",a[2],a[3],a[4]);
    long double suma = 0;
    pthread_t self = pthread_self();
    printf("Thread #%ld size=%f first=%f\n",self,a[1],a[0]);
    for(int i = 0; i<a[1]; i++){
        suma = suma + a[i+2];
    }
    sum += suma;
    printf("Thread #%ld sum=%.20Lf\n",self,suma);
    //return (void *) suma;
    pthread_mutex_unlock(&lock);
}

int main(int argc, char** argv){
    struct timespec start, stop;
    if(argc!=3){
        fprintf(stderr, "Nieprawidlowa liczba argumentow\n");
        return 1;
    }
    if(atoi(argv[1])<=1 || atoi(argv[1]) >=1000000 || atoi(argv[2])<=1 || atoi(argv[2]) >= min(100,atoi(argv[1]))){
        fprintf(stderr, "Nieprawidlowe argumenty\n");
        return 1;
    }

    int w = atoi(argv[2]);
    int n = atoi(argv[1]);
    double values[1000000]={0};
    int r = n%w;
    int d = n/w;
    pthread_t threads[w];
    
    for(int i=1; i<n+1; i++){
        values[i-1] = 1.0/((double)i*(double)i);
    }
    clock_t c1 = clock();
    for(int i = 0; i<w; i++){
        if(i+1==w && r!=0){
            double *data = (double*)calloc(d+2+r,sizeof(double));
            data[0] = i*d;
            data[1] = d+r;
            int k = 2;
            for(int j =(i*d); j<(i*d)+d+r;j++){
                data[k] = values[j];
            }
            pthread_create(threads+i,NULL,thr,data);
        }else{
            double *data = (double*)calloc(d+2,sizeof(double));
            data[0] = i*d;
            int k = 2;
            data[1] = d;
            for(int j =(i*d); j<((i*d)+d);j++){
                data[k] = values[j];
                //printf("j: %d, val: %f\n", j, values[j]);
                k++;
            }
            pthread_create(threads+i,NULL,thr,data);
        }
    }
    
    
    for(int i=0;i<w;i++){
        double retval;
        pthread_join(threads[i],(void *)&retval);
        //suma = suma + retval;
    }
    double pi;
    pi = sqrt(sum*6);
    
    
    printf("w/Threads: PI=%.20f, time=%fs\n",pi,((double)c1/CLOCKS_PER_SEC));
    
    clock_t c2 = clock();
    double sumawo = 0;
    for(int i = 0; i<n;i++){
        sumawo = sumawo + values[i];
    }
    sumawo = sqrt(sumawo*6);
    
    
    printf("wo/Threads: PI=%.20f time=%fs\n",sumawo,((double)c2/CLOCKS_PER_SEC));
    
    pthread_mutex_destroy(&lock);
    return 0;
}


