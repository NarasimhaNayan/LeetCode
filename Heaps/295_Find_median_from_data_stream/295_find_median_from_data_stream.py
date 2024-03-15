import heapq
class MedianFinder:

    def __init__(self):
        # self.arr = []
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        # add num to max_heap
        heapq.heappush(self.max_heap,-num)

        # Check the heap where we should insert the element
        if len(self.min_heap) :
            if -self.max_heap[0] > self.min_heap[0] :
                heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
        else :
            if len(self.max_heap) > 1:
                heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))

        # balance the heaps
        if len(self.max_heap) > len(self.min_heap)+1 :
            heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap) :
            heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))


    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap))%2:
            return -self.max_heap[0]
        else :
            return (-self.max_heap[0]+self.min_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()