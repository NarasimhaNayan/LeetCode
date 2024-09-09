"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums :
            if num in hashmap :
                return True
            else:
                hashmap[num] = 1
        return False
    
def main():
    solution = Solution()
    s = [1,2,3,4]
    res = solution.containsDuplicate(s)
    print(res)

if __name__ == "__main__":
    main()