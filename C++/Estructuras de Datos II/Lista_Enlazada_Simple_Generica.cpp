#include <iostream>

using namespace std;

template <typename T>
struct Nodo
{
    T info;
    Nodo <T> *siguiente;
};

template <typename T>
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
    void insertar(T elem)
    {
        auto nuevonodo = new Nodo <T> {elem, cabeza};
        cabeza = nuevonodo;
    }
    T primero()
    {
        if(cabeza)
        {
            return cabeza -> info;
        }else
        {
            return T{};
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
    Nodo <T> *cabeza = nullptr;
};

int main()
{
    Lista <int> lint;
    lint.insertar(0);
    lint.insertar(1);
    lint.insertar(2);
    cout << lint.primero() << endl;
    Lista <double> ldouble;
    ldouble.insertar(0.01);
    ldouble.insertar(1.1);
    ldouble.insertar(2.2);
    cout << ldouble.primero() << endl;
    Lista <string> lstring;
    lstring.insertar("Jorge");
    lstring.insertar("Llamo");
    lstring.insertar("Me");
    cout << lstring.primero() << endl;
    return 0;
}