from F_CalculatorDistance import CalculatorDistance

class Instance:
    def __init__(self):
        self.node_list: list[int] = []
        self.latitude: list[float] = []
        self.longitude: list[float] = []
        self.distanceMatrix: list[list[float]] = []

    def calculate_distance_matrix(self):
        if not self.latitude or not self.longitude:
            raise ValueError("Latitude and longitude lists cannot be empty.")
        self.distanceMatrix = CalculatorDistance.calculateEuclideanDistanceMatrix(self.latitude, self.longitude)

    def read_instance(self, absolute_route: str):
        with open(absolute_route) as archivo:
            archivo.readline()
            for line in archivo:
                identificador, latitud, longitud, _ = line.strip().split(";")
                self.node_list.append(int(identificador))
                self.latitude.append(float(latitud))
                self.longitude.append(float(longitud))
        self.calculate_distance_matrix()
