"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        while low <= high :
            mid = (low+high)//2
            if nums[mid] == target :
                start = mid
                end = mid
                while start > 0 and nums[start-1] == target:
                    start -= 1
                while end < len(nums)-1 and nums[end+1] == target:
                    end+=1
                return [start,end]
            elif nums[mid] > target:
                high = mid-1
            else:
                low =mid+1
        return [-1,-1]

def main():
    solution = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    res = solution.searchRange(nums,target)
    print(res)

if __name__ == "__main__":
    main()
        