#include <iostream>
#include <vector>
template <typename ValueType>
class Myclass{
public:
    ValueType operator[](int idx) const{ //el valor es constante, si const va delante quiere decir que el valor que se devuelve es contante, si va detras es porque la funcion es constante
        return a[idx];
    }
    ValueType& operator[](int idx){
        return a[idx];
    }
private:
    std::vector<ValueType>a{100};
};

int main(){
    Myclass<std::string>c;
    c[3]='tres';
    c[42]='cuarenta y dos';
    std::cout<<'c[3]='<<c[3]<<'\n';
}