"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, 
adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were 
broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob 
tonight without alerting the police.

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""

from typing import List

class Solution:
    def robsRecursion(self,start,end,nums):
        if end < start:
            return 0
        if end == start :
            return nums[end]
        pick = nums[end] + self.robsRecursion(start,end-2,nums)
        no_pick = 0 + self.robsRecursion(start,end-1,nums)
        return max(pick,no_pick)
    
    # Memoization
    def robsMemoization(self,start,end,nums,dp):
        if end < start:
            return 0
        if end == start :
            return nums[end]
        if dp[end] != -1 :
            return dp[end]
        pick = nums[end] + self.robsMemoization(start,end-2,nums,dp)
        no_pick = 0 + self.robsMemoization(start,end-1,nums,dp)
        dp[end] = max(pick,no_pick)
        return max(dp)
    
    def rob(self, nums: List[int]) -> int:
        # Recursion
        # return max(self.robsRecursion(0,len(nums)-2,nums), self.robsRecursion(1,len(nums)-1,nums))
    
        #Memoization
        # if len(nums) == 1 :
        #     return nums[0]
        # if len(nums) == 2 :
        #     return max(nums[0],nums[1])
        # dp1 =  [-1]*len(nums)
        # dp2 =  [-1]*len(nums)
        # return max(self.robsMemoization(0,len(nums)-2,nums,dp1), self.robsMemoization(1,len(nums)-1,nums,dp2))

        # Tabulation
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2 :
            return max(nums[1],nums[0])
        # if len(nums) == 3:
        #     return max(nums[2]nums[0], max())
        dp1 = [-1]*len(nums)
        dp2 = [-1]*len(nums)
        dp1[0] = nums[0]
        dp1[1] = dp2[1] = nums[1]
        dp2[2] = nums[2]

        for i in range(2,len(nums)-1):
            dp1[i] = max(dp1[i-2]+nums[i],dp1[i-1])
        dp1_max = max(dp1[-2],dp1[-3])

        for i in range(3,len(nums)):
            dp2[i] = max(dp2[i-2]+nums[i],dp2[i-1])
        dp2_max = max(dp2[-1],dp2[-2])

        return max(dp1_max,dp2_max)
        # TODO: Complete the sol
        # dp1[2] = nums
def main():
    solution = Solution()
    nums = [1,2,3,1]
    res = solution.rob(nums)
    print(res)

if __name__ == "__main__":
    main()