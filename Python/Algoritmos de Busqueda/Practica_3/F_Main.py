from F_Instance import Instance
from F_AlgorithmGRASP import AlgorithmGRASP
from F_ConstructiveRANDOM import ConstructiveRANDOM
from F_LocalSearch1x1 import LocalSearch1x1
from F_CalculatorDistance import CalculatorDistance
if __name__ == "__main__":
    instancia = Instance()
    instancia.read_instance("C:/Users/profesor/Downloads/104_Mostoles_coordenadas.txt")
    algoritmo_GRASP = AlgorithmGRASP(ConstructiveRANDOM(), LocalSearch1x1())
    algoritmo_GRASP.execute(instancia)
    print(algoritmo_GRASP.best_solution.node_list, algoritmo_GRASP.best_solution.distance)
        