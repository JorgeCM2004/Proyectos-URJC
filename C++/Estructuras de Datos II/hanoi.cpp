#include <iostream>
#include <stack>

using namespace std;

class hanoi
{
private:
    stack <int> a, b, c;
    int n = 1;

    void mover(stack <int> &mov1, stack <int> &mov2)
    {
        auto aux = mov1.top();
        mov1.pop();
        mov2.push(aux);
    }
    int resolveraux(int discos, stack <int> &origen, stack <int> &destino, stack <int> &aux)
    {
        auto contador = 0;
        if (discos == 1)
        {
            this -> mover(origen, destino);
            contador++;
        } else
        {
            contador += resolveraux(discos - 1, origen, aux, destino);
            this -> mover(origen, destino);
            contador += 1;
            contador += resolveraux(discos - 1, aux, destino, origen);
        }
        return contador;
    }
public:
    hanoi(int num)
    {   if (num > 0)
        {
            n = num;
        }   
        for (auto i = num; i > 0; --i)
        {
            a.push(i);
        }
    }
    void estado_inicial()
    {
        while (!a.empty())
        {
            a.pop();
        }
        while (!b.empty())
        {
            b.pop();
        }
        while (!c.empty())
        {
            c.pop();
        }
        for (auto i = n; i > 0; --i)
        {
            a.push(i);
        }
    }
    void mostrar()
    {
        cout << "Palo A:\n";
        auto aux = a;
        int num;
        while (!aux.empty())
        {
            num = aux.top();
            aux.pop();
            cout << num << " ";
        }

        cout << "\nPalo B:\n";
        aux = b;
        while (!aux.empty())
        {
            num = aux.top();
            aux.pop();
            cout << num << " ";
        }

        cout << "\nPalo C:\n";
        aux = c;
        while (!aux.empty())
        {
            num = aux.top();
            aux.pop();
            cout << num << " ";
        }
        cout << endl;
    }
    int resolver()
    {
        if (a.empty())
        {
            cout << "El puzle ya esta resuelto." << endl;
            return 0;
        } else
        {
            return resolveraux(n, a, b, c); 
        }
    }
};

int main()
{
    hanoi h{100};
    h.mostrar();
    cout << "Numero movimientos: " << h.resolver() << "\n";
    h.mostrar();
}