import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = {}
        heap = []
        res = []

        for i in range(len(words)):
            if words[i] in hashmap:
                hashmap[words[i]] += 1
            else :
                hashmap[words[i]] = 1

        for i in hashmap.items() :
            key, value = i
            heapq.heappush(heap,(-value,key))
            
        while k > 0:
            word = heapq.heappop(heap)
            res.append(word[1])
            k-=1
        heap = heapq.nlargest(k,heap)
        return res


        