"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]


Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""


from typing import List

class Solution:
    def computePermutations(self,processed,unprocessed,res):
        if len(unprocessed) == 0 :
            res.append(processed.copy())
            return
        
        
        for i in range(len(processed)+1):
            processed.insert(i,unprocessed[0])
            self.computePermutations(processed,unprocessed[1:],res)
            processed.pop(i)
            if i< len(processed) and unprocessed[0] == processed[i]:
                break
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.computePermutations([],nums,res)
        return res
    
def main() :
    solution = Solution()
    nums = [1,3,1]
    res = solution.permute(nums)
    print(res)

if __name__ == "__main__":
    main()