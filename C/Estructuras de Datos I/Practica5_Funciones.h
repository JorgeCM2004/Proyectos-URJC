#ifndef PRACTICA5_FUNCIONES_H
#define PRACTICA5_FUNCIONES_H

typedef struct Fecha{
    int dia;
    int mes;
    int anyo;
} tFecha;

typedef struct Noticia{
    char titulo[50];
    tFecha fecha;
    char fuente[50];
    int visitas;
} tNoticia;

typedef struct nodo{
    tNoticia info;
    struct nodo* sig;
    struct nodo* ant;
} tNodo;

typedef struct Lista{
    tNodo* head;
    tNodo* tail;
} tLista;

tNoticia Crear_Noticia();
tNodo* Crear_Nodo(tNoticia noticia);
int Comparar_Noticias (tNoticia noticia1, tNoticia noticia2);
void insertarAlPrincipio(tLista* lista, tNoticia noticia);
void insertarAlFinal(tLista* lista, tNoticia noticia);
void Obtener_Primera_Noticia(tLista* lista, tNoticia* direccion);
void Eliminar_Noticia(tLista* lista, tNoticia noticia);
void Imprimir_Noticia(tNoticia noticia);
void Imprimir_Lista(tLista* lista);
int Total_VIsitas(tLista* lista);

#endif