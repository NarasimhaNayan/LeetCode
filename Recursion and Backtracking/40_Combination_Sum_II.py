"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.


Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

from typing import List

class Solution:
    def findCombination(self,processed,unprocessed,target,res,sett,prev):
        if target == 0 :
            temp_tuple = tuple(processed.copy())
            if temp_tuple not in sett:
                res.append(list(temp_tuple))
                sett.add(temp_tuple)
            return
        if target < 0:
            return
            
        for i in range(len(unprocessed)):
            if prev == unprocessed[i] :
                continue
            self.findCombination(processed+[unprocessed[i]],unprocessed[i+1:],target-unprocessed[i],res,sett,prev)
            prev = unprocessed[i]
            # target = target+processed.pop(-1)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sett = set()
        self.findCombination([],sorted(candidates),target,res,sett,-1)
        return res

def main():
    solution = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    res = solution.combinationSum2(candidates,target)
    print(res)

if __name__ == "__main__":
    main() 
