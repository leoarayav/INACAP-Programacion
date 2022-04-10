#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXIMA_LONGITUD_CADENA 100

struct nodoCadena
{
    char cadena[MAXIMA_LONGITUD_CADENA];
    struct nodoCadena *izquierda;
    struct nodoCadena *derecha;
};

struct nodoCadena *NuevoNodo(char cadena[MAXIMA_LONGITUD_CADENA])
{
    size_t tamNodo = sizeof(struct nodoCadena);
    struct nodoCadena *nodo = (struct nodoCadena *)malloc(tamNodo);
    strcpy(nodo -> cadena, cadena);
    nodo -> izquierda = nodo -> derecha = NULL;
    return nodo;
}

void Agregar(struct nodoCadena *nodo, char *cadena)
{
    if (strcmp(cadena, nodo -> cadena) > 0)
    {
        if (nodo -> derecha == NULL)
        {
            nodo -> derecha = NuevoNodo(cadena);
        }
        else
        {
            Agregar(nodo -> derecha, cadena);
        }
    }
    else
    {
        if (nodo -> izquierda == NULL)
        {
            nodo -> izquierda = NuevoNodo(cadena);
        }
        else
        {
            Agregar(nodo -> izquierda, cadena);
        }
    }
}

struct nodoCadena *Buscar(struct nodoCadena *nodo, char *cadena)
{
    if (nodo == NULL)
    {
        return NULL;
    }

    if (strcmp(cadena, nodo -> cadena) == 0)
    {
        return nodo;
    }
    else if (strcmp(cadena, nodo -> cadena) > 0)
    {
        return Buscar(nodo -> derecha, cadena);
    }
    else
    {
        return Buscar(nodo -> izquierda, cadena);
    }
}

void PreOrden(struct nodoCadena *nodo)
{
    if (nodo != NULL)
    {
        printf("%s,", nodo -> cadena);
        PreOrden(nodo -> izquierda);
        PreOrden(nodo -> derecha);
    }
}

void InOrden(struct nodoCadena *nodo)
{
    if (nodo != NULL)
    {
        InOrden(nodo -> izquierda);
        printf("%s,", nodo -> cadena);
        InOrden(nodo -> derecha);
    }
}

void PostOrden(struct nodoCadena *nodo)
{
    if (nodo != NULL)
    {
        PostOrden(nodo -> izquierda);
        PostOrden(nodo -> derecha);
        printf("%s,", nodo -> cadena);
    }
}

int main(int argc, char const *argv[])
{
    // Declaramos la raiz.
    struct nodoCadena *raiz = NULL;

    raiz == NULL ? raiz = NuevoNodo("Leo") : printf(raiz);

    // Mostrar busqueda.
    char busqueda[MAXIMA_LONGITUD_CADENA] = "Leo";
    struct nodoCadena *apuntador = Buscar(raiz, busqueda);
    apuntador == NULL ? printf("[ERROR] %s no existe en el arbol.", busqueda) : printf("%s si existe en el arbol.", busqueda);

    char otraBusqueda[MAXIMA_LONGITUD_CADENA] = "Nombre";
    struct nodoCadena *apuntador = Buscar(raiz, busqueda);
    apuntador == NULL ? printf("[ERROR] %s no existe en el arbol.", busqueda) : printf("%s si existe en el arbol.", busqueda);
    
    return 0;
}