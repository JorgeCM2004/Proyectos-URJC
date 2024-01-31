#include "Practica9_Funciones.h"
#include "Practica9_Funciones.c"
int main()
{
    tKaggle p;
    tNodo* nodo;
    tElemeto copy;
    crear_vacio(&p);
    crear_competicion(&copy, "Roberto", 99, 1);
    crear_nodo(&nodo, copy);
    construir(&p, nodo);
    crear_competicion(&copy, "Alfonso", 10, 10);
    crear_nodo(&nodo, copy);
    construir(&p, nodo);
    imprimir_arbol(p);
}