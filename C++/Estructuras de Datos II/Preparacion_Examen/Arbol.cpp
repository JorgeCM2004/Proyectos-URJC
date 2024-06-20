#include <iostream>
#include <memory>
#include <stack>

template <typename T>
class BTree
{
public:
    template <typename S>
    class Node
    {
    private:
        S info;
        Node<S>* padre;
        std::shared_ptr<Node<S>> h_izquierdo;
        std::shared_ptr<Node<S>> h_derecho;        
    public:
        Node(const S& value) : info(value), padre(nullptr), h_izquierdo(nullptr), h_derecho(nullptr) {}
        friend class BTree;
    };

    void addNode(const T& info)
    {
        Node<T> nodo(info);
        addNode(nodo);
    }

    void addNode(const Node<T>& nodo) {
        if (root == nullptr) {
            addRoot(nodo);
        } else {
            addNodePrivate(root, nodo);
        }
    }
    T getInfo(Node<T>* nodo)
    {
        return nodo -> info;
    }
    auto getRoot()
    {
        return root.get();
    }
    auto getPadre(Node<T>* nodo)
    {
        return nodo -> padre;
    }
    auto getHIzquierdo(Node<T>* nodo)
    {
        return nodo -> h_izquierdo;
    }
    auto getHDerecho(Node<T>* nodo)
    {
        return nodo -> h_derecho;
    }
private:
    std::shared_ptr<Node<T>> root = nullptr;
    void addRoot(Node<T> nodo)
    {
        auto n_inteligente = std::make_shared<Node<T>>(nodo);
        root = n_inteligente;
    }
    void addRoot(T info)
    {
        Node<T> nodo(info);
        addRoot(nodo);
    }
    void addNodePrivate(std::shared_ptr<Node<T>> r, const Node<T>& nodo) {
        if (nodo.info < r->info) {
            if (r->h_izquierdo == nullptr) {
                r->h_izquierdo = std::make_shared<Node<T>>(nodo);
                r->h_izquierdo->padre = r.get();
            } else {
                addNodePrivate(r->h_izquierdo, nodo);
            }
        } else {
            if (r->h_derecho == nullptr) {
                r->h_derecho = std::make_shared<Node<T>>(nodo);
                r->h_derecho->padre = r.get();
            } else {
                addNodePrivate(r->h_derecho, nodo);
            }
        }
    }
};

template <typename T>
class IteradorPreorden
{
public:
    IteradorPreorden(): t(), pila() {}
    IteradorPreorden(T tree): t(tree), pila() {pila.push(t.getRoot());}
    IteradorPreorden& operator++()
    {
        auto e = pila.top();
        pila.pop();
        auto d = t.getHDerecho(e);
        if (d)
        {
            pila.push(d);
        }
        auto i = t.getHIzquierdo(e);
        if (i)
        {
            pila.push(i);
        }
        return *this;        
    }
    IteradorPreorden& operator++(int)
    {
        auto tmp(*this);
        operator++();
        return tmp;
    }
    auto operator*()
    {
        return t.getInfo(pila.top());
    }
    bool operator!=(const IteradorPreorden& other)
    {
        auto d = (pila.empty() != other.pila.empty());
        return d;
    }
private:
    T t;
    std::stack<typename T::Node<typename T::type>*> pila;;
};

template <typename T, typename I>
class Iterable
{
public:
    Iterable(T begin): inicio(I(begin)), fin(I()) {};
    auto begin() {return inicio;};
    auto end() {return fin;};

private:
    I inicio;
    I fin;
};

int main() {
    BTree<int> t;
    t.addNode(10);
    t.addNode(5);
    t.addNode(20);
    t.addNode(3);
    t.addNode(7);
    Iterable<BTree<int>, IteradorPreorden<BTree<int>>> iterador(t);
    for (auto i : iterador)
    {
        std::cout << i << ", ";
    }
    
    return 0;
}