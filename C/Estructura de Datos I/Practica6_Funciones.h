#ifndef PRACTICA6_FUNCIONES_H
#define PRACTICA6_FUNCIONES_H
typedef struct Videojuego
{
    char titulo[100];
    char genero[100];
    float puntuacion;
    float precio;
}tVideojuego;

typedef tVideojuego tElemento;

typedef struct nodo
{
    tElemento info;
    struct nodo* ant;    
}tNodo;

typedef tNodo* tLista;

tLista Crear_Vacia();
tElemento Crear_Videojuego(char titulo[100], char genero[100], float puntuacion, float precio);
tNodo* Crear_Nodo(tElemento elemento);
void push(tLista* lista, tElemento elemento);
void pop(tLista* lista);
void Mostrar_Gratis(tLista lista);
#endif