class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # hashmap to check frequencies
        hashmap = {}
        for i in range(len(nums)) :
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else :
                hashmap[nums[i]] = 1

        # check for max frequency and return the sum
        hashmap = sorted(hashmap.items(), key = lambda x:x[1], reverse = True)
        max_frequency = hashmap[0][1]

        count = 0

        for i in hashmap :
            print(count,max_frequency)
            ele, freq = i
            if freq == max_frequency :
                count+= max_frequency
            else :
                break
        return count