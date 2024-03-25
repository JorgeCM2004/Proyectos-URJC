#include <iostream>
#include <vector>
struct Persona {
    std::string nombre;
    std::string apellidos;
    unsigned long long num_DNI;
    char letra_DNI;
    bool valido = false;
};

auto hash(Persona e)
    {
        return e.num_DNI;
    }

template <typename T, int N = 100>
class efficentStorage
{
public:
    void insertar(const T& e)
    {
        if (storage[e.hash() % N].valido == false)
        {
            storage.insert(storage.begin() + (e.hash() % N), e);
        } else
        {
            colisiones++;
        }
    }
    void remove(const T& e)
    {
        storage.remove(storage.begin() + (e.hash() % N));
    }
    bool contains(const T& e)
    {
        return storage[e.hash() % N] == e;
    }
private:
    std::vector <T> storage{N};
    int colisiones = 0;
};
