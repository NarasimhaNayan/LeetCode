"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:
1 <= n <= 45
"""

class Solution:
    # Tabulation method
    def climbStairsTabulation(self, n: int) -> int:
        dp = [-1]*(n)
        if n == 1 or n == 2:
            return n
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]

    # Memoization method
    def computeMemoization(self, dp, n):
        if n == 1 or n == 2:
            return n
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.computeMemoization(n-2)+self.computeMemoization(n-1)
        return dp[-1]
    
    def climbStairsMemoization(self, n: int) -> int:
        dp = [-1]*(n+1)
        return self.computeMemoization(dp,n)
        
    
def main():
    solution = Solution()
    n=4
    res = solution.climbStairsMemoization(n)
    print(res)

if __name__ == "__main__":
    main()