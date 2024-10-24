"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in num_set:
        # Find the first ele of the subsequence => ele-1 will not be in the IP
            if num-1 not in num_set:
                length=1
                # Find the consecutive numbers after finding the 1st ele
                while num+1 in num_set:
                    # Increase the length by 1 and move to next num
                    length+=1
                    num+=1
                # Find max_len of the subsequence calculated
                max_len = max(max_len,length)
        return max_len
    
def main() :
    solution = Solution()
    nums = [100,4,200,1,3,2]
    res = solution.longestConsecutive(nums)
    print(res)

if __name__=="__main__":
    main()