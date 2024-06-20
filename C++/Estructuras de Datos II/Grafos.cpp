#include <iostream>
#include <unordered_map>
#include <vector>

template <typename T, typename W>
class BasicGraph {
public:
    void addNode(T node) {
        nodes[node] = {};
    }

    void setEdge(T sourceNode, T targetNode, W weight) {
        nodes[sourceNode][targetNode] = weight;
        nodes[targetNode][sourceNode] = weight; // Grafo no dirigido
    }

    const std::unordered_map<T, W>& getEdges(T node) const {
        return nodes.at(node);
    }
    
    // No puede ser const porque puede crear la arista vacia si no existe
    W getEdge(T sourceNode, T targetNode) {
        return nodes.at(sourceNode).at(targetNode);
    }
    
    void removeNode(T node) {
        auto& edges = nodes[node];
        for (const auto& [targetNode, weight] : edges) {
            nodes[targetNode].erase(node);
        }
        nodes.erase(node);
    }

    auto begin() {return nodes.begin();}
    auto end() {return nodes.end();}

private:
    std::unordered_map<T, std::unordered_map<T, W>> nodes;
};

struct city {
    std::string name;
    int population;
    int surface;
    auto operator<=>(const city& other) const {
        return surface <=> other.surface;
    }
    bool operator==(const city& other) const {
        return name == other.name; 
    }
};

namespace std {
    template <>
    struct hash<city> {
        size_t operator()(const city& c) const {
            return hash<int>{}(c.surface);
        }
    };
}

int main() {
    BasicGraph<city, int> graph;

    // Agregar nodos
    city c1{"City1", 10000, 50};
    city c2{"City2", 5000, 30};
    city c3{"City3", 20000, 70};
    city c4{"City4", 15000, 60};
    city c5{"City5", 30000, 80};

    graph.addNode(c1);
    graph.addNode(c2);
    graph.addNode(c3);
    graph.addNode(c4);
    graph.addNode(c5);

    // Agregar aristas
    graph.setEdge(c1, c2, 42);
    graph.setEdge(c1, c3, 43);
    graph.setEdge(c1, c4, 44);
    graph.setEdge(c1, c5, 44);
    graph.setEdge(c2, c3, 37);
    graph.setEdge(c3, c4, 34);
    graph.setEdge(c4, c5, 54);

    // Mostrar grafo completo
    for (const auto& [node, edges] : graph) {
        std::cout << "Aristas del nodo " << node.name << ":" << "\n";
        for (const auto& [targetNode, weight] : edges) {
            std::cout << "  - Nodo " << targetNode.name << ": " << ((weight != 0) ? "Conectado" : "No conectado") << "\n";
        }
    }

    graph.removeNode(c3);    

    std::cout << "***********************\n";

    // Mostrar grafo sin nodo 3
    for (const auto& [node, edges] : graph) {
        std::cout << "Aristas del nodo " << node.name << ":" << "\n";
        for (const auto& [targetNode, weight] : edges) {
            std::cout << "  - Nodo " << targetNode.name << ": " << ((weight != 0) ? "Conectado" : "No conectado") << "\n";
        }
    }
    
    std::cout << "***********************\n";
    
    // GetEdges muestra la arista si existe y sino la crea "vacia"
    std::cout << "Node 1 - Node 2: " << graph.getEdge(c1, c2) << "\n";
    std::cout << "Node 2 - Node 5: " << graph.getEdge(c2, c5) << "\n";

    return 0;
}