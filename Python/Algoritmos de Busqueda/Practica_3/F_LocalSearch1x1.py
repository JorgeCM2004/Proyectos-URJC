from F_Solution import Solution
from F_Improvement import Improvement

class LocalSearch1x1(Improvement):
    def improve(self, solution: Solution) -> Solution:
        improved = False
        while not improved:
            for i in range(len(solution.node_list) - 1):
                for j in range(i + 1, len(solution.node_list)):
                    new_solution = solution.node_list.copy()
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_sol = Solution(new_solution, solution.instance)
                    if solution.compare(new_sol) == 1:
                        solution = new_sol
                        improved = True
        return solution
