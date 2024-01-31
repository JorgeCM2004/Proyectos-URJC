#include <iostream>
#include <cmath>

using namespace std;

class Punto3d
{
public:
    /*
    Punto3d(double x, double y, double z)
    {
        this -> x = x;
        this -> y = y;
        this -> z = z;
    Punto3d()
    {
        x = 0;
        y = 0;
        z = 0;
    }
    }
    */
    Punto3d(double x, double y, double z): x(x), y(y), z(z){}
    Punto3d(): x(0), y(0), z(0){}
    double modulo()
    {
        return sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2));
    }
    double getprivatex()
    {
        return getx();
    }
    double gety()
    {
        return y;
    }
    double getz()
    {
        return z;
    }
    void increasex()
    {
        x++;
    }
    void increasey()
    {
        y++;
    }
    void increasez()
    {
        z++;
    }
private:
    double getx()
    {
        return x;
    }
    double x, y, z;
};



int main()
{
    Punto3d b;
    Punto3d a{1, 2, 3};
    a.increasex();
    a.increasez();
    cout << b.getprivatex() << endl;
    cout << "El modulo del punto a es: " << a.modulo() << endl;
    return 0;
}
