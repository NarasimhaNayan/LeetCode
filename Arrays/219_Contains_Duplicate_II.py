"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that 
nums[i] == nums[j] and abs(i - j) <= k.
 
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        positions = dict()
        i = 0
        for num in nums:
            if num in positions:
                if i-positions[num] <= k:
                    return True
            positions[num] = i
            i +=1
        return False
    
def main():
    solution = Solution()
    s = [1,2,3,1]
    k=2
    res = solution.containsNearbyDuplicate(s,k)
    print(res)

if __name__ == "__main__":
    main()