//SO IS1 212A LAB10
//Grzegorz Bauer
//bg49206@zut.edu.pl
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>

int main(){
    for(;;){
        size_t glen = 0;
        char cwd[256];
        if(getcwd(cwd,sizeof(cwd))==NULL){
            printf("getcwd() error");
            break;
        };
        printf("%s%s", cwd, "> ");
        char *bufor;
        bufor = NULL;
        if(getline(&bufor,&glen,stdin)==-1){
            break;
        };
        
        extern char ** environ;
        char * token;
        token = strtok(bufor," \t\n");
        //printf("%s\n",token);
        if(strcmp(token,"exit")==0){
            break;
        }
            if(strcmp(token,"vars")==0){
                int i=0;
                while(environ[i]){
                    printf("%s \n",environ[i]);
                    i++;
                }
            

            }else if(strcmp(token,"set")==0){
               
                int it = 0;
                char* name;
                char* val;
                while(token!=NULL){
                    it++;
                    token=strtok(NULL," \t\n");
                    if(it==1){
                        name = token;
                    }else if(it==2){
                        val = token;
                        setenv(name,val,1);
                    }
                }

            }else if(strcmp(token, "del")==0){
                //printf("%s","weszlo-del");
                int it=0;
                while(token!=NULL){
                    //printf("%s","weszlo");
                    it++;
                    token=strtok(NULL," \t\n");
                    if(it==1){
                    unsetenv(token);
                    }
                }
                
                

            }else if(strcmp(token,"cd")==0){
                //printf("%s","cd uzyte");
                int it = 0;
                char* name;
                
                while(token!=NULL){
                    it++;
                    token=strtok(NULL," \t\n");
                    if(it==1){
                        name = token;
                        chdir(name);
                    }
                    
                }
            }else{
                
                char* args;
                char* name;
                name = token;
                int it=0;
                token=strtok(NULL," \t\n");
                args = token;
                //token=strtok(NULL," \t\n");
                //printf("\n%s\n%s\n", name,args);
                int c1;
                c1 = fork();
                if(c1 ==0){
                    execlp(name,name,args,NULL);
                }
                int c1ex=0;
                waitpid(c1,&c1ex,0);
            };
        
        free(bufor);
        
    };

    return 0;
};
