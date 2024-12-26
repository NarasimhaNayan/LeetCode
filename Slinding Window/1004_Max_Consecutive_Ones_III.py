"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Variable to keep track of number of zeros and 2 pointers
        zero_count = 0
        max_ones = 0
        i,j = 0,0
        # start iterating through the nums arr
        while j < len(nums):
            # if nums[index] is 0 then increase zero_count
            if nums[j] == 0 :
                zero_count += 1

            # if zero_count > k move the left pointer till zero_count become <= k
            while zero_count > k :
                # print(i)
                if nums[i] == 0:
                    zero_count -= 1
                i+=1
            
            # Calculate the max_len
            max_ones = max(max_ones,(j-i+1))
            j+=1

        return max_ones
        
def main():
    solution = Solution()
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    res = solution.longestOnes(nums,k)
    print(res)

if __name__ == "__main__" :
    main()