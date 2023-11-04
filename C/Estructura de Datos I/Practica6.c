#include "Practica6_Funciones.h"
#include "Practica6_Funciones.c"
#include <stdio.h>
#include <string.h>
int main()
{
    tLista lista = Crear_Vacia();
    tElemento videojuego;
    char titulo[100], genero[100];
    float puntuacion, precio;
    int eleccion = 1;
    while (eleccion != 0)
    {
        printf("0. Salir del programa.\n1. Anyadir videojuego a la pila.\n2. Eliminar el ultimo videojuego anyadido.\n3. Mostrar la lista de los juegos gratuitos.\n");
        scanf("%i", &eleccion);
        switch (eleccion)
        {
        case 0:
            printf("Gracias por usar el programa.");
            break;
        
        case 1:
            getchar();
            printf("Titulo del videojuego: ");
            fgets(titulo, 100, stdin);
            while (strlen(titulo) == 1)
            {
                printf("No has introducido nada, vuelve a intentarlo: ");
                fgets(titulo, 100, stdin);
            }
            printf("Genero del videojuego: ");
            fgets(genero, 100, stdin);
            while (strlen(genero) == 1)
            {
                printf("No has introducido nada, vuelve a intentarlo: ");
                fgets(genero, 100, stdin);
            }
            printf("Puntuacion del videojuego: ");
            scanf("%f", &puntuacion);
            printf("Precio del videojuego: ");
            scanf("%f", &precio);
            videojuego = Crear_Videojuego(titulo, genero, puntuacion, precio);
            push(&lista, videojuego);
            break;

        case 2:
            pop(&lista);
            break;

        case 3:
            Mostrar_Gratis(lista);
            break;

        default:
            printf("La opcion seleccionada no existe, por favor intentelo de nuevo.");
            eleccion = 1;
            break;
        }
    }
}