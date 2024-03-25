#include <iostream>
#include <memory>

int main()
{
    auto pdata{std::make_shared <double> (1.0)};
    std::cout << *pdata << "\n";
    *pdata = 42.0;
    std::cout << *pdata << "\n";
    auto pinfo{pdata};
    *pinfo = 3.7;
    std::cout << *pdata << "\n";
    return 0;
}
