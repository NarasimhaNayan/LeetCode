"""
Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

from typing import List

class Solution:
    def findSubsets(self, nums, temp, res, index,sett):
        if index == len(nums):
            temp_tuple = tuple(sorted(temp.copy()))
            if temp_tuple not in sett :
                res.append(list(temp_tuple))
                sett.add(temp_tuple)
            return
        
        self.findSubsets(nums,temp,res,index+1,sett)
        self.findSubsets(nums,temp+[nums[index]],res,index+1,sett)        

    def findSubsetUsingProcessedAndUnprocessed(self, processed, unprocessed,res,sett):
        if len(unprocessed) == 0 :
            temp_tuple = tuple(processed.copy())
            if temp_tuple not in sett:
                res.append(list(temp_tuple))
                sett.add(temp_tuple)
            return
        
        self.findSubsetUsingProcessedAndUnprocessed(processed+[unprocessed[0]],unprocessed[1:],res,sett)
        self.findSubsetUsingProcessedAndUnprocessed(processed,unprocessed[1:],res,sett)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res =[]
        temp = []
        index = 0
        sett = set()
        # self.findSubsets(nums,temp,res,index,sett)
        self.findSubsetUsingProcessedAndUnprocessed([],nums,res,sett)
        return res
    
def main():
    solution = Solution()
    nums= [1,2,2]
    res = solution.subsetsWithDup(nums)
    print(res)

if __name__ == "__main__":
    main()