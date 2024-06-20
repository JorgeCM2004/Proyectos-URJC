from F_Instance import Instance
from F_Solution import Solution
from F_CalculatorDistance import CalculatorDistance
from F_Constructive import Constructive
from random import shuffle

class ConstructiveRANDOM(Constructive):
    def construct(self, instance: Instance) -> Solution:
        rand_node_list = instance.node_list.copy()
        shuffle(rand_node_list)
        sol = Solution(rand_node_list, instance)
        return sol