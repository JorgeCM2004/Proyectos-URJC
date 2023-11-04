#include "Practica6_Funciones.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

tPila Crear_Vacia()
{
    return NULL;
}

tElemento Crear_Videojuego(char titulo[100], char genero[100], float puntuacion, float precio)
{
    tElemento out;
    strcpy(out.titulo, titulo);
    strcpy(out.genero, genero);
    out.puntuacion = puntuacion;
    out.precio = precio;
    return out;
}

tNodo* Crear_Nodo(tElemento elemento)
{
    tNodo* aux = (tNodo*) malloc(1 * sizeof(tNodo));
    aux -> info = elemento;
    aux -> ant = NULL;
    return aux;
}

void push(tPila* pila, tElemento elemento)
{
    tNodo* nodo_nuevo = Crear_Nodo(elemento);
    if ((*pila) != NULL)
    {
        nodo_nuevo -> ant = *pila;
    }
    *pila = nodo_nuevo;
}

void pop(tPila* pila)
{
    if ((*pila) != NULL)
    {
        tNodo* aux = (*pila);
        (*pila) = (*pila) -> ant;
        free(aux);
    }else 
    {
        printf("La pila esta vacia.\n");
    }
}

void Mostrar_Gratis(tPila pila)
{
    tNodo* recorrer = pila;
    int gratis = 0;
    if (pila == NULL)
    {
        printf("La pila esta vacia.\n");
        gratis = 1;
    }
    while (recorrer)
    {
        if (recorrer -> info.precio == 0.0)
        {
            printf("--------------------\nTitulo: %s\n", recorrer -> info.titulo);
            printf("Genero: %s\n", recorrer -> info.genero);
            printf("Puntuacion: %f\n--------------------\n", recorrer -> info.puntuacion);
            gratis = 1;
        }
        recorrer = recorrer -> ant;
    }
    if (gratis == 0)
    {
        printf("No existe ningun juego gratis en la pila.\n");
    }
}
