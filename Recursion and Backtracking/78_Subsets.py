"""
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

from typing import List

class Solution:
    
    def find_subsets (self,nums, temp, res, i):
        if i == len(nums) :
            res.append(temp.copy())
            return res
        # Either consider the element or do not consider the element for subset
        res = self.find_subsets(nums,temp,res,i+1)
        res = self.find_subsets(nums,temp+[nums[i]],res,i+1)
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        i = 0
        res = self.find_subsets(nums,temp,res,i)
        return res
    
def main():
    solution = Solution()
    nums = [1,2,3]
    res = solution.subsets(nums)
    print(res)

if __name__ == "__main__" :
    main()
        