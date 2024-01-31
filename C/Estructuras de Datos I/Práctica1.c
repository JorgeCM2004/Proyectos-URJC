#include <stdio.h>
#include <stdlib.h>
int subprogramaArray(int** contenedor, int num){
    printf("%i\n", num);
    contenedor = (int*) malloc(sizeof(int) * 10000);
    return subprogramaArray(contenedor, num + 1);
}
int main(){
    int *p[10];
    subprogramaArray(p, 1);
}
