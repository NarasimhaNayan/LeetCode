import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1 :
            return stones[0]
        max_heap = []
        # Since we need to pop 2 max ele. We need to convert the array to max_heap
        for i in range(len(stones)) :
            heapq.heappush(max_heap, -(stones[i]))
        print(max_heap)

        # We will pop the top 2 elements and if they are not equal we will push 
        # the difference bw stone1 and 2 to the heap
        while len(max_heap) > 1 :
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            print(stone1,stone2)
            if stone1 != stone2 :
                heapq.heappush(max_heap, (stone1-stone2))
            print(len(stones))
            print(max_heap)

        # Return the last ele if exists
        if len(max_heap) == 1 :
            return -1*heapq.heappop(max_heap)
        else :
            return 0

        