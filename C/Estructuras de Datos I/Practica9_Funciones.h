#ifndef PRACTICA9_FUNCIONES_H
#define PRACTICA9_FUNCIONES_H

typedef struct competicion
{
    char nombre[20];
    int tiempo;
    int premio;
}tCompeticion;

typedef tCompeticion tElemeto;

typedef struct nodo
{
    tElemeto info;
    struct nodo* hDerecho;
    struct nodo* hIzquierdo;
}tNodo;

typedef tNodo* tKaggle;

#endif