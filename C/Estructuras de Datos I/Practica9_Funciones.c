#include "Practica9_Funciones.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void crear_vacio(tKaggle* p)
{
    *p = NULL;
}

void crear_competicion(tElemeto* competicion, char n[20], int t, int p)
{
    strcpy(competicion -> nombre, n);
    competicion -> tiempo = t;
    competicion -> premio = p;
}

void copiar_concurso(tElemeto* destino, tElemeto concurso)
{
    strcpy(destino -> nombre, concurso.nombre);
    destino -> tiempo = concurso.tiempo;
    destino -> premio = concurso.premio;
}

void crear_nodo(tNodo** nodo, tElemeto concurso)
{
    *nodo = (tNodo*) malloc(sizeof(tNodo));
    (*nodo) -> hIzquierdo = NULL;
    (*nodo) -> hDerecho = NULL;
    copiar_concurso(&((*nodo) -> info), concurso);
}

void construir(tKaggle* arbol, tNodo* nodo)
{
    if (*arbol)
    {
        if (nodo -> info.premio > (*arbol) -> info.premio)
        {
            construir(&((*arbol) -> hDerecho),  nodo);
        } else
        {
            construir(&((*arbol) -> hIzquierdo), nodo);
        }
    } else 
    {
        *arbol = nodo;
    }
}

int obtener_premio(tCompeticion competicion)
{
    return competicion.premio;
}

int obtener_tiempo(tCompeticion competicion)
{
    return competicion.tiempo;
}

void imprimir_concurso(tCompeticion informacion)
{
    printf("--------------------\nNombre: %s\n", informacion.nombre);
    printf("Tiempo restante: %i\n", obtener_tiempo(informacion));
    printf("Premio: %i\n--------------------\n", obtener_premio(informacion));
}

void imprimir_arbol(tKaggle arbol)
{
    if (arbol)
    {
        imprimir_arbol(arbol -> hDerecho);
        imprimir_concurso(arbol -> info);
        imprimir_arbol(arbol -> hIzquierdo);
    }
}

tElemeto obtener_minimo(tKaggle arbol)
{
    if (arbol -> hIzquierdo)
    {
        obtener_minimo(arbol -> hIzquierdo);
    } else
    {
        return arbol -> info;
    }
}
void eliminar_competicion(tKaggle* arbol, int eliminar)
{
    if (*arbol)
    {
        if (obtener_premio((*arbol) -> info) > eliminar)
        {
            eliminar_competicion(&((*arbol) -> hIzquierdo), eliminar);
        } else
        {
            if (obtener_premio((*arbol) -> info) < eliminar)
            {
                eliminar_competicion(&((*arbol) -> hDerecho), eliminar);
            } else
            {
                
            }
        }
    } else
    {
        printf("ERROR");
    }
} 