"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates 
where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations 
for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
"""

from typing import List

class Solution:
    def findCombination(self,processed,unprocessed,target,res,sett):
        if target < 0 :
            return
        if target == 0 :
            temp_tuple = tuple(sorted(processed.copy()))
            if temp_tuple not in sett :
                res.append(list(temp_tuple))
                sett.add(temp_tuple)
            return
        
        for i in range(len(unprocessed)):
            self.findCombination(processed+[unprocessed[i]],unprocessed,target-unprocessed[i],res,sett)


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sett = set()
        self.findCombination([],candidates,target,res,sett)
        return res
    
def main():
    solution = Solution()
    candidates = [2,3,6,7]
    target = 7
    res = solution.combinationSum(candidates,target)
    print(res)

if __name__ == "__main__":
    main()