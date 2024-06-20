from F_Instance import Instance

class Solution:
    def __init__(self, node_list: list[int], instance: Instance):
        self.node_list: list[int] = node_list
        self.distance: int = 0
        self.instance: Instance = instance
        self.evaluate()
    
    def compare(self, solution: 'Solution') -> int:
        if self.distance < solution.distance:
            return -1
        elif self.distance == solution.distance:
            return 0
        else:
            return 1
    
    def evaluate(self): 
        for pos_node in range(len(self.node_list) - 1): 
            node1 = self.node_list[pos_node] - 1
            node2= self.node_list[pos_node + 1] - 1
            self.distance += self.instance.distanceMatrix[node1][node2]

        primer_nodo = self.node_list[0] - 1
        ultimo_nodo = self.node_list[len(self.node_list)-1] - 1
        self.distance += self.instance.distanceMatrix[ultimo_nodo][primer_nodo]
        