#include <stdio.h>
#include <stdlib.h>
int subprogramaArray(int num){
    printf("%i\n", num);
    int p[1000];
    return subprogramaArray(num + 1);
}
int subprogramaPila(int num){
    printf("%i\n", num);
    return subprogramaPila(num + 1);
}
int main(){
    subprogramaArray(1);
    subprogramaPila(1);
    return 0;
}
