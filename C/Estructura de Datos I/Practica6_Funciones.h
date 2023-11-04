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

typedef tNodo* tPila;

tPila Crear_Vacia();
tElemento Crear_Videojuego(char titulo[100], char genero[100], float puntuacion, float precio);
tNodo* Crear_Nodo(tElemento elemento);
void push(tPila* pila, tElemento elemento);
void pop(tPila* pila);
void Mostrar_Gratis(tPila pila);
#endif