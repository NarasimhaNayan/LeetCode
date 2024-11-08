"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 0
        high = max(piles)

        if len(piles) > h :
            return 0

        while low <= high:
            mid = (low+high)//2
            no_of_hrs = 0
            for i in range(len(piles)):
                if piles[i]%mid == 0 :
                    no_of_hrs += piles[i]//mid
                else:
                    no_of_hrs += (piles[i]//mid)+1
            
            if no_of_hrs > h :
                low = mid+1
            else:
                high = mid-1
        
        return low
    
def main():
    solution = Solution()
    piles = [3,6,7,11]
    h = 8
    res = solution.minEatingSpeed(piles,h)
    print(res)

if __name__ == "__main__":
    main()