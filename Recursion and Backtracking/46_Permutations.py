"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List

class Solution:
    # def compute_permutation(self,nums,temp,res,index) :
        # if index == len(nums):
        #     if len(temp) == len(nums) :
        #         # Convert set to list and append to res
        #         # temp_list = list(temp)
        #         res.append(temp.copy())
        #     return
        # if nums[index] not in temp :
        #     temp.append(nums[index])
        # for i in range(len(nums)):
        #     self.compute_permutation(nums,temp,res,index+1)
        #     index-= 1
        #     temp.pop()

    def compute_permutations(self,processed,unprocessed,res):
        if len(unprocessed) == 0:
            res.append(processed.copy())
            return
        num_to_be_added = unprocessed[0]
        for i in range(len(processed)+1):
            processed.insert(i,num_to_be_added)
            self.compute_permutations(processed,unprocessed[1:],res)
            processed.remove(num_to_be_added)

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.compute_permutations([],nums,res)
        return res

def main() :
    solution = Solution()
    nums = [1,2,3]
    res = solution.permute(nums)
    print(res)

if __name__ == "__main__":
    main()