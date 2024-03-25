#include <array>
#include <unordered_map>
template <typename T, int N = 5>
class graph
{
private:
    std::array <std::array <int, N>, N> matriz_adyacencia;
    std::unordered_map <int, T> almacen;
public:

};
