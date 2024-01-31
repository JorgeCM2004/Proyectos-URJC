#include <iostream>

using namespace std;

struct Persona
{
    string nombre;
    unsigned edad;
};

int main()
{
    Persona f{.nombre = "Marcos", .edad = 21};
    Persona a{{f.nombre, 4, 0}, 10};
    cout << "nombre: " << a.nombre << "\nedad: " << a.edad << endl;
    return 0;
}
