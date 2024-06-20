class CalculatorDistance:
    
    @staticmethod
    def calculateEuclideanDistance(longitude_1: int, latitude_1: int, longitude_2: int, latitude_2: int) -> int:
        return ((longitude_2 - longitude_1)**2 + (latitude_2 - latitude_1)**2)**0.5
    
    @staticmethod
    def calculateEuclideanDistanceMatrix(latitudes: list[int], longitudes: list[int]) -> list[list[int]]:
        matrix: list[list[int]] = []
        index = 0
        for latitude1, longitude1 in zip(latitudes, longitudes):
            matrix.append([])
            for latitude2, longitude2 in zip(latitudes, longitudes):
                matrix[index].append(CalculatorDistance.calculateEuclideanDistance(longitude1, latitude1, longitude2, latitude2))
            index += 1
        return matrix