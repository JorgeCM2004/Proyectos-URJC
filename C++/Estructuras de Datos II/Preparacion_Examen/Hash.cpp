#include <iostream>
#include <unordered_map>
#include <list>
/* Ejercicio 2 Enunciado Enero 2022*/
using STR = std::string;

template <typename W>
struct Airport
{
    STR nombre;
    std::unordered_map<STR, W> aristas;

    Airport(STR n): nombre(n), aristas() {}

    auto getID()
    {
        return nombre;
    }

    auto addFlight(W vuelo)
    {
        aristas[vuelo.getID()] = vuelo;
    }
};

template <typename W>
struct std::hash <Airport <W>>
{
    auto operator() (const Airport<W>& Aeropuerto) const
    {
        return (std::hash <STR>()(Aeropuerto.nombre));
    }
};

struct Flight
{
    STR id;
    int time;
    int cost;
    Airport<Flight>* destino;
    Flight(STR i, int t, int c, Airport<Flight>* d): id(i), time(t), cost(c), destino(d) {};
    auto getID()
    {
        return id;
    }
    auto operator<=>(const Flight& otro) const = default;
};

template <>
struct std::hash <Flight>
{
    auto operator()(const Flight& vuelo) const
    {
        return (std::hash <STR>()(vuelo.id));
    }
};

template <typename T, typename W>
class URJCFlights
{
    private:
    std::unordered_map<STR, T> nodes;
    std::unordered_map<T, std::unordered_map <T, int>> aeropuertos_conectados;
    public:

    URJCFlights(): nodes(), aeropuertos_conectados() {};

    auto newAirport(Airport<W> aeropuerto)
    {
        nodes[aeropuerto.getID()] = aeropuerto;
    }

    auto newAirport(STR info)
    {
        Airport<W> aeropuerto(info);
        nodes[aeropuerto.getID()] = aeropuerto;

    }

    auto newConnection(T aeropuerto, std::list<std::pair<T, int>> lista_aeropuertos)
    {
        for (auto pares : lista_aeropuertos)
        {
            auto t_elem = pares.first;
            auto distancia_entera = pares.second;
            aeropuertos_conectados[aeropuerto.getID()][t_elem.getID()] = distancia_entera;
            aeropuertos_conectados[t_elem.getID()][aeropuerto.getID()] = distancia_entera;
        };
    }

    auto newFlight(T aeropuerto, W vuelo)
    {
        if (aeropuertos_conectados[aeropuerto.getID()][vuelo.destino -> getID()])
        {
            aeropuerto.addFlight(vuelo);
            std::cout << "Vuelo añadido" << "\n";
        } else
        {
            std::cout << "Los aeropuertos no estan conectados" << "\n";
        }
    }

    auto availableAirportsConnections(T aeropuerto)
    {
        return aeropuertos_conectados[aeropuerto.getID()];
    }

    auto availableFlights(T aeropuerto)
    {
        return nodes[aeropuerto.getID()];
    }
};
int main() {
    URJCFlights<Airport<Flight>, Flight> gestor_vuelos;

    // Crear aeropuertos
    Airport<Flight> madrid("Madrid");
    Airport<Flight> barcelona("Barcelona");
    Airport<Flight> paris("Paris");

    // Agregar aeropuertos al gestor de vuelos
    gestor_vuelos.newAirport(madrid);
    gestor_vuelos.newAirport(barcelona);
    gestor_vuelos.newAirport(paris);

    // Establecer conexiones entre los aeropuertos
    gestor_vuelos.newConnection(madrid, {{barcelona, 600}, {paris, 1000}});
    gestor_vuelos.newConnection(barcelona, {{paris, 800}});

    // Crear algunos vuelos
    Flight vuelo1("1", 120, 200, &madrid);
    Flight vuelo2("2", 90, 150, &madrid);

    // Añadir vuelos al aeropuerto de Madrid
    gestor_vuelos.newFlight(madrid, vuelo1);
    gestor_vuelos.newFlight(madrid, vuelo2);

    // Mostrar vuelos disponibles desde Madrid
    std::cout << "Vuelos disponibles desde Madrid:" << std::endl;
    for (const auto& flight_pair : gestor_vuelos.availableFlights(madrid)) {
        std::cout << "ID: " << flight_pair.first << ", Time: " << flight_pair.second.time << ", Cost: " << flight_pair.second.cost << std::endl;
    }

    return 0;
}

