#include "Practica8_Funciones.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void Crear_Arbol_Vacio(tOlimpo* a)
{
    *a = NULL;
}

void Construir(tNodo** raiz, tNodo* hDerecho, tNodo* hIzquierdo, tOlimpo* olimpo)
{
    (*raiz) -> derecho = hDerecho;
    (*raiz) -> izquierdo = hIzquierdo;
    *olimpo = *raiz;
}

void Crear_Nodo(tNodo** direccion, tElemento informacion)
{
    *direccion = (tNodo*) malloc(sizeof(tNodo));
    strcpy((*direccion) -> info.nombre, informacion.nombre);
    strcpy((*direccion) -> info.descripcion, informacion.descripcion);
    (*direccion) -> derecho = NULL;
    (*direccion) -> izquierdo = NULL;
}

void Crear_Dios(tElemento* direccion, char nombre[20], char informacion[200])
{
    strcpy(direccion -> nombre, nombre);
    strcpy(direccion -> descripcion, informacion);
}

void Kratos(tOlimpo* Arbol)
{
    if (*Arbol)
    {
        if ((*Arbol) -> derecho)
        {
            Kratos(&((*Arbol) -> derecho));
        }
        if ((*Arbol) -> izquierdo)
        {
            Kratos(&((*Arbol) -> izquierdo));
        }
        free(*Arbol);
    }
}

int Buscar_Dios(tOlimpo Arbol, tElemento Dios)
{
    if (Arbol)
    {
        if (strcmp(Arbol -> info.nombre, Dios.nombre) == 0)
        {
            return 1;
        } else
        {
            int valor = 0;
            valor = Buscar_Dios(Arbol -> derecho, Dios);
            if (valor)
            {
                return valor;
            }
            valor = Buscar_Dios(Arbol -> izquierdo, Dios);
            if (valor)
            {
                return valor;
            }
        }
    }
    return 0;
}

void Imprimir_Dios(tElemento Dios)
{
    printf("--------------------\nNombre: %s\n", Dios.nombre);
    printf("Descripcion: %s\n--------------------\n", Dios.descripcion);
}
