#include "Practica5_Funciones.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

tNoticia Crear_Noticia(){
    tNoticia noticia;

    while(getchar() != '\n');
    printf("Introduce el titulo de la noticia(maximo 50 chars): ");
    fgets(noticia.titulo, 50, stdin);
    while (strlen(noticia.titulo) == 1){
        printf("No has introducido nada, vuelve a intentarlo: ");
        fgets(noticia.titulo, 50, stdin);
    }

    printf("Introduce la fecha de la noticia:\n");
    printf("Dia: ");
    scanf("%i", &noticia.fecha.dia);
    printf("Mes: ");
    scanf("%i", &noticia.fecha.mes);
    printf("Anio: ");
    scanf("%i", &noticia.fecha.anyo);

    while(getchar() != '\n');
    printf("Introduce la fuente de la noticia(maximo 50 chars): ");
    fgets(noticia.fuente, 100, stdin);
    while (strlen(noticia.fuente) == 1
    ){
        printf("No has introducido nada, vuelve a intentarlo: ");
        fgets(noticia.fuente, 100, stdin);
    }

    printf("Introduce el numero de visitas de la noticia: ");
    scanf("%i", &noticia.visitas);

    return noticia;
}

tNodo* Crear_Nodo(tNoticia noticia){
    tNodo* nodo = (tNodo*) malloc(sizeof(tNodo));
    strncpy(nodo -> info.titulo, noticia.titulo, 50);
    nodo -> info.fecha = noticia.fecha;
    strncpy(nodo -> info.fuente, noticia.fuente, 50);
    nodo -> info.visitas = noticia.visitas;
    nodo -> sig = NULL;
    nodo -> ant == NULL;
    return nodo;
}

int Comparar_Noticias (tNoticia noticia1, tNoticia noticia2){
    if (noticia1.fecha.dia == noticia2.fecha.dia && noticia1.fecha.mes == noticia2.fecha.mes && 
    noticia1.fecha.anyo == noticia2.fecha.anyo && noticia1.fuente == noticia2.fuente &&
    noticia1.titulo == noticia2.titulo && noticia1.visitas == noticia2.visitas)
    {
        return 1;
    } else
    {
        return 0;
    }
}

void insertarAlPrincipio(tLista* lista, tNoticia noticia){
    tNodo* nodo = crearNodo(noticia);
    if (lista -> head)
    {
        lista -> head -> ant = nodo;
    } else
    {
        lista -> tail = nodo;
    }
    nodo -> sig = lista -> head;
    lista -> head = nodo;
}

void insertarAlFinal(tLista* lista, tNoticia noticia){
    tNodo* nodo = crearNodo(noticia);
    if (lista -> tail)
    {
        lista -> tail -> sig = nodo;
    } else
    {
        lista -> head = nodo;
    }
    nodo -> ant = lista -> tail;
    lista -> tail = nodo;
}

void Obtener_Primera_Noticia(tLista* lista, tNoticia* direccion){
    if (lista -> head) {
        tNoticia noticia = lista -> head -> info;
        strcpy(direccion -> titulo, noticia.titulo);
        strcpy(direccion -> fuente, noticia.fuente);
        direccion -> fecha = noticia.fecha;
        direccion -> visitas = noticia.visitas;
    } else 
    {
        return NULL;
    }
}

void Eliminar_Noticia(tLista* lista, tNoticia noticia){
    tNodo* recorrer = lista -> head;
    int encontrado = 0;
    while (!encontrado && recorrer)
    {
        if (Comparar_Noticias(recorrer -> info, noticia))
        {
            encontrado = 1;
            if (recorrer -> ant && recorrer -> sig)
            {
                recorrer -> ant -> sig = recorrer -> sig;
                recorrer -> sig -> ant = recorrer -> ant;
            } else
            {
                if (recorrer -> ant)
                {
                    recorrer -> ant -> sig = NULL;
                    lista -> tail = recorrer -> ant;
                } else
                {
                    if (recorrer -> sig)
                    {
                        recorrer -> sig -> ant = NULL;
                        lista -> head = NULL;
                    } else
                    {
                        lista -> head = NULL;
                        lista -> tail = NULL;
                    }
                }
            }
            free(recorrer);
        }
    }
}

void Imprimir_Noticia(tNoticia noticia){
    printf("Titulo: %s\n", noticia.titulo);
    printf("Fecha de publicacion: %i/%i/%i\n", noticia.fecha.dia, noticia.fecha.mes, noticia.fecha.anyo);
    printf("Fuente: %s\n", noticia.fuente);
    printf("Numero de visitas: %i\n", noticia.visitas);
    printf("\n");
}

void Imprimir_Lista(tLista* lista){
    int count = 1;
    tNodo* recorrer = lista -> head;
    while (recorrer)
    {
        printf("Noticia %i:\n", count);
        imprimirNoticia(recorrer -> info);
        recorrer = recorrer -> sig;
        count++;
    }
}

int Total_VIsitas(tLista* lista){
    tNodo* recorrer = lista -> head;
    int out = 0;
    while (recorrer)
    {
        out += recorrer -> info.visitas;
    }
    return out;
}
