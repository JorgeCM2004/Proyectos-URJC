#include <unordered_map>
#include <unordered_set>
#include <iostream>

template<typename T, typename Weight = bool>
class Graph {
private:
    std::unordered_map<T, std::unordered_set<T>> adjacency_list;
    std::unordered_map<std::pair<T, T>, Weight> edge_weights;
public:
    void addNode(const T& node) {
        if (adjacency_list.find(node) == adjacency_list.end()) {
            adjacency_list[node] = std::unordered_set<T>();
        }
    }

    void setEdge(const T& from, const T& to, const Weight& weight) {
        addNode(from);
        addNode(to);
        edge_weights[std::make_pair(from, to)] = weight;
        edge_weights[std::make_pair(to, from)] = weight; // Para grafos no dirigidos
    }

    Weight getEdge(const T& from, const T& to) {
        if (edge_weights.find(std::make_pair(from, to)) != edge_weights.end()) {
            return edge_weights[std::make_pair(from, to)];
        }
        return Weight(); // Valor predeterminado (bool = false, otros tipos = 0)
    }

    std::unordered_set<T> getEdges(const T& node) {
        if (adjacency_list.find(node) != adjacency_list.end()) {
            return adjacency_list[node];
        }
        return std::unordered_set<T>(); // Si el nodo no existe, devuelve un conjunto vacío
    }

    void removeNode(const T& node) {
        if (adjacency_list.find(node) != adjacency_list.end()) {
            adjacency_list.erase(node);
            for (auto& pair : edge_weights) {
                if (pair.first.first == node || pair.first.second == node) {
                    edge_weights.erase(pair.first);
                }
            }
        }
    }

    typename std::unordered_map<T, std::unordered_set<T>>::iterator begin() {
        return adjacency_list.begin();
    }

    typename std::unordered_map<T, std::unordered_set<T>>::iterator end() {
        return adjacency_list.end();
    }
};

int main() {
    Graph<int, int> grafo;
    graph.setEdge(1, 2, 5);
    graph.setEdge(2, 3, 7);
    graph.setEdge(3, 4, 3);

    std::cout << "Edges of node 2:\n";
    for (int edge : graph.getEdges(2)) {
        std::cout << edge << std::endl;
    }

    std::cout << "Weight of edge (2, 3): " << graph.getEdge(2, 3) << std::endl;

    std::cout << "Removing node 2...\n";
    graph.removeNode(2);

    std::cout << "Remaining nodes:\n";
    for (auto it = graph.begin(); it != graph.end(); ++it) {
        std::cout << it->first << std::endl;
    }

    return 0;
}

