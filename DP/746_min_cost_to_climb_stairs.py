"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""

from typing import List 

class Solution:
    def computeRecursion(self,index,cost):
        if index == 0 or index == 1:
            return cost[index] 
        if index < 0 :
            return 0
        one_step = cost[index]+self.computeRecursion(index-1,cost)
        two_step = cost[index]+self. computeRecursion(index-2,cost)
        return min(one_step, two_step)
    
    def computeMemoization(self,index,cost,dp):
        if index == 0 or index == 1:
            return cost[index] 
        if index < 0 :
            return 0
        if dp[index] != -1 :
            return dp[index]
        
        one_step = cost[index]+self.computeMemoization(index-1,cost,dp)
        two_step = cost[index]+self. computeMemoization(index-2,cost,dp)
        dp[index] = min(one_step, two_step)
        return dp[index]
    
    def computeTabulation(self,index,cost,dp):
        if index == len(cost):
            return 0
        
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Recursion
        # index = len(cost)
        # return min(self.computeRecursion(index-1,cost), self.computeRecursion(index-2,cost))

        # Memoization
        # index = len(cost)
        # dp = [-1]*index
        # return min(self.computeMemoization(index-1,cost,dp), self.computeMemoization(index-2,cost,dp))
    
        #Tabulation
        if len(cost) == 2:
            return min(cost[0],cost[1])
        
        # index = 0
        dp = [-1]*len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2,len(cost)):
            dp[i] = min(dp[i-2],dp[i-1])+cost[i]
        return min(dp[-1],dp[-2])
    
def main():
    solution = Solution()
    cost = [10,15,20]
    res = solution.minCostClimbingStairs(cost)
    print(res)

if __name__ == "__main__":
    main()
        