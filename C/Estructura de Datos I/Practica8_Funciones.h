#ifndef PRACTICA8_FUNCIONES_H
#define PRACTICA8_FUNCIONES_H

typedef struct dioses
{
    char nombre[20];
    char descripcion[200];
}tDioses;

typedef tDioses tElemento;

typedef struct nodo
{
    tElemento info;
    struct nodo* derecho;
    struct nodo* izquierdo;
}tNodo;

typedef tNodo* tOlimpo;

void Crear_Arbol_Vacio(tOlimpo* a);
void Construir(tNodo* raiz, tNodo* hDerecho, tNodo* hIzquierdo, tOlimpo* olimpo);
void Crear_Nodo(tNodo* direccion, tElemento* informacion);
void Crear_Dios(tElemento* direccion, char nombre[20], char informacion[200]);
void Copiar_Info(tNodo** direccion, tElemento* informacion);
void Kratos(tOlimpo* Arbol);
int Buscar_Dios(tOlimpo Arbol, tElemento Dios);
void Imprimir_Dios(tElemento Dios);

#endif