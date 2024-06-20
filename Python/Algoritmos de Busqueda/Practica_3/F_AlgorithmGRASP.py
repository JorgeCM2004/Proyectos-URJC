from F_Algorithm import AlgorithmGRASP
from F_ConstructiveRANDOM import ConstructiveRANDOM
from F_LocalSearch1x1 import LocalSearch1x1
from F_Instance import Instance
from F_Solution import Solution

class AlgorithmGRASP(AlgorithmGRASP):

    def __init__(self, constructive: ConstructiveRANDOM, improvement: LocalSearch1x1) -> None:
        self.constructive = constructive
        self.improvement = improvement
        self.best_solution = None
    
    def execute(self, instance: Instance):
        for _ in range(10):
            solution: Solution = self.constructive.construct(instance)
            solution = self.improvement.improve(solution)
            self.compare(solution)
    
    def compare(self, solution: Solution):
        if self.best_solution is None:
            self.best_solution = solution
        elif self.best_solution.compare(solution) == 1:
            self.best_solution = solution
        