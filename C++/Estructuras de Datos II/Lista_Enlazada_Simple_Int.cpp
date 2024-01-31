#include <iostream>

using namespace std;

struct Nodo
{
    int info;
    Nodo *siguiente;
};

class Lista
{
public:
    ~Lista()
    {
        while (cabeza)
        {
            resto();
        }
    }
    void insertar(int elem)
    {
        auto nuevonodo = new Nodo{elem, cabeza};
        cabeza = nuevonodo;
    }
    int primero()
    {
        if(cabeza)
        {
            return cabeza -> info;
        }else
        {
            return -1;
        }
    }
    void resto()
    {
        if(cabeza)
        {
            auto aux = cabeza;
            cabeza = cabeza -> siguiente;
            delete aux;
        }
    }
private:
    Nodo *cabeza = nullptr;
};

int main()
{
    return 0;
}