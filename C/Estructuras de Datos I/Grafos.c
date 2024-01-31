#include <stdio.h>
#include <stdlib.h>
typedef struct superheroe {...} tSuperHeroe;
typedef struct arista
{
	tSuperHeroe info;
	int peso;
	struct arista* siguiente;
}tArista;

typedef struct nodo
{
	tSuperHeroe info;
	struct nodo* siguientenodo;
	tArista* conexiones;
}tNodo;

typedef tNodo* tGrafo;

void insertarSuperHeroe(tGrafo* grafo, char * nom, int v, int f)
{
	tNodo* Nodo = (tNodo*) malloc(sizeof(tNodo));
	crearSuperheroe(&(Nodo -> info), nom, v, f);
	crearListaVacia(&(Nodo -> conexiones));
	Nodo -> siguientenodo = *grafo;
	*grafo = Nodo;
}
void crearUnaConexion(tGrafo grafo, tSuperHeroe super1, tSuperHeroe super2, int escenas)
{
	tGrafo recorrer = grafo;
	while(iguales(&(recorrer -> info), &super1) == 0)
	{
		recorrer = recorrer -> siguientenodo;
	}
	tArista* arista = (tArista*) malloc(sizeof(tArista));
	asignarSuperHeroe(&(arista -> info), super2);
	arista -> peso = escenas;
	arista -> siguiente = recorrer -> conexiones;
	recorrer -> conexiones = arista;
}
void crearConexion(tGrafo grafo, tSuperHeroe super1, tSuperHeroe super2, int escenas)
{
	if(numeroSecuencias(grafo, obtenerNombre(&super1), obtenerNombre(&super2)) == 0)
	{
		crearUnaConexion(grafo, super1, super2, escenas);
		crearUnaConexion(grafo, super2, super1, escenas);
	}
}


/*
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

} */