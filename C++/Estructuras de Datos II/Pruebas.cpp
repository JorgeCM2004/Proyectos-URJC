#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector <int> v = {8, 9, 1, 2, 3};
    v.push_back(10);
    for (const auto & e : v)
    {
        cout << e << " ";
    }
    return 0;
}