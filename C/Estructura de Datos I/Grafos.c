#include <stdio.h>
#include <stdlib.h>

typedef struct alumnos
{
    char nombre[100];
}tAlumnos;

typedef tAlumnos tElemento;

typedef struct arista
{
    tElemento info;
    struct arista* sig;
}tArista;

typedef struct nodo
{
    tElemento info;
    struct nodo* sig_nodo;
    tArista* arista;
}tNodo;

typedef tNodo* tGrafo;

void crear_grafo(tGrafo* grafo)
{
    *grafo = NULL;
}

void insertar_nodo(tGrafo* grafo, tNodo* nodo, tElemento elemento)
{
    nodo = (tNodo*) malloc(sizeof(tNodo));
    nodo -> info = elemento;
    nodo -> arista = NULL;
    nodo -> sig_nodo = *grafo;
    *grafo = nodo;
}



int main()
{
    tGrafo grafo;
    crear_grafo(&grafo);

}