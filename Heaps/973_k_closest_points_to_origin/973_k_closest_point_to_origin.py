import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distance = []

        for point in points:
            x = point[0]
            y = point[1]
            dist = pow(point[0],2) + pow(point[1],2)
            distance.append((dist,[x,y]))
        heapq.heapify(distance)

        for _ in range(k) :
            point = heapq.heappop(distance)
            res.append(point[1])
        return res       
