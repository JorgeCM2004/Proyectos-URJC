#include <memory>
template <typename T>
class LinkedBinaryTree
{
public:
    template <typename S>
    class Node
    {
        friend class LinkedBinaryTree;
        S info;
        Node<S>* parent;
        std::shared_ptr<Node<S>> left;
        std::shared_ptr<Node<S>> right;
    };

    bool isEmpty() {return root == nullptr;}
    Node<T>* getRoot() {return root.get();}
    Node<T>* getLeftChild(Node<T>* p) {return p -> left.get();}
    Node<T>* getRightChild(Node<T>* p) {return p -> right.get();}
    Node<T>* getParent(Node<T>* p) {return p -> parent;}
    T getElement(Node<T>* p) {return p -> info;}
    bool isRoot(Node<T>* p) {return p == root.get();}
    bool isLeaf(Node<T>* p) {return (p -> left == nullptr) && (p -> right == nullptr);}
    bool isInternal(Node<T>* p) {return !isLeaf(p);}
    Node<T>* addRoot(T e) 
    {
        root = std::make_shared<Node<T>>();
        root -> info = e;
        root -> parent = nullptr;
        root -> left = nullptr;
        root -> right = nullptr;
        return root.get();
    }
    Node<T>* addLeftChild(T e, Node<T>* p) 
    {
        if (p)
        {
            p -> left = std::make_shared<Node<T>>();
            p -> left -> info = e;
            p -> left -> parent = p;
            p -> left -> left = nullptr;
            p -> left -> right = nullptr;
            return p -> left.get();
        }
        return nullptr;
    }
    Node<T>* addRightChild(T e, Node<T>* p) 
    {
        if (p)
        {
            p -> right = std::make_shared<Node<T>>();
            p -> right -> info = e;
            p -> right -> parent = p;
            p -> right -> left = nullptr;
            p -> right -> right = nullptr;
            return p -> right.get();
        }
        return nullptr;
    }
private:
    std::shared_ptr<Node<T>> root = nullptr;
};

int main()
{
    LinkedBinaryTree<int> tree;
    auto aux = tree.addRoot(1);
    aux = tree.addLeftChild(2, aux);
    aux = tree.addLeftChild(3, aux);
    aux = tree.getParent(aux);
    aux = tree.addRightChild(4, aux);
    aux = tree.getRoot();
    aux = tree.addRightChild(5, aux);
    aux = tree.addLeftChild(6, aux);
    aux = tree.getParent(aux);
    aux = tree.addRightChild(7, aux);    
    return 0;
}
