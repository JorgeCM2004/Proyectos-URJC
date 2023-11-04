#include "Practica6_Funciones.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

tLista Crear_Vacia()
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

void push(tLista* lista, tElemento elemento)
{
    tNodo* nodo_nuevo = Crear_Nodo(elemento);
    if ((*lista) != NULL)
    {
        nodo_nuevo -> ant = *lista;
    }
    *lista = nodo_nuevo;
}

void pop(tLista* lista)
{
    if ((*lista) != NULL)
    {
        tNodo* aux = (*lista);
        (*lista) = (*lista) -> ant;
        free(aux);
    }else 
    {
        printf("La lista esta vacia.\n");
    }
}

void Mostrar_Gratis(tLista lista)
{
    tNodo* recorrer = lista;
    int gratis = 0;
    if (lista == NULL)
    {
        printf("La lista esta vacia.\n");
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
        printf("No existe ningun juego gratis en la lista.\n");
    }
}
