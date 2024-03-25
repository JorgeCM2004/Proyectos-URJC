#include <iostream>
#include <vector>
#include <list>

template <typename KeyType, typename ValueType, int N = 100>
class HashMap
{
private:
    std::vector <std::list<std::pair<KeyType, ValueType>>> contenedor{N};
    size_t compress(KeyType k) {return k % N;}
public:
    int operator[](KeyType k) const
    {
        auto idx = compress(k);
        auto encontrado = false;
        auto it = contenedor[idx].begin();
        while ((!encontrado) and (it != contenedor[idx].end()))
        {
            encontrado = (*it).first == k; 
            if (!encontrado) ++it;
        }

        if (encontrado)
        {
            return (*it).second;
        } else
        {
            return ValueType{};
        }
    }
    int& operator[](KeyType k)
    {
        auto idx = compress(k);
        auto encontrado = false;
        auto it = contenedor[idx].begin();
        while ((!encontrado) and (it != contenedor[idx].end()))
        {
            encontrado = (*it).first == k; 
            if (!encontrado) ++it;
        }

        if (encontrado)
        {
            return (*it).second;
        } else
        {
            contenedor[idx].push_front(std::make_pair(k, ValueType{}));
            return contenedor[idx].front().second;
        }
    }
    bool contains(KeyType k)
    {
        auto idx = compress(k);
        for (auto& p: contenedor[idx])
        {
            if (p.first == k)
            {
                return true;
            }
        }
        return false;
    }
};

int main(){
    HashMap <int, int, 100> c;
    c[30102] = 20;
    std::cout << "c[30102] = " << c[30102] << '\n';
}