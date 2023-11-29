#include "Practica8_Funciones.h"
#include "Practica8_Funciones.c"

int main()
{
    tOlimpo p;
    tNodo vacio, nodo;
    tElemento copy;
    Crear_Arbol_Vacio(&vacio);
    Crear_Dios(&copy, "Zeus", "Dios padre, mato a cronos para hacerse con el Olimpo");
    Crear_Nodo(&nodo, &copy);
    Construir( &nodo, &vacio, &vacio, &p);
    Imprimir_Dios(copy);
}