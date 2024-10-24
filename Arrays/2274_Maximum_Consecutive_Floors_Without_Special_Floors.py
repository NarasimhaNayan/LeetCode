"""
Alice manages a company and has rented some floors of a building as office space. Alice has decided some of these floors should be special floors, used for relaxation only.

You are given two integers bottom and top, which denote that Alice has rented all the floors from bottom to top (inclusive). You are also given the integer array special, where special[i] denotes a special floor that Alice has designated for relaxation.

Return the maximum number of consecutive floors without a special floor.

 

Example 1:

Input: bottom = 2, top = 9, special = [4,6]
Output: 3
Explanation: The following are the ranges (inclusive) of consecutive floors without a special floor:
- (2, 3) with a total amount of 2 floors.
- (5, 5) with a total amount of 1 floor.
- (7, 9) with a total amount of 3 floors.
Therefore, we return the maximum number which is 3 floors.
Example 2:

Input: bottom = 6, top = 8, special = [7,6,8]
Output: 0
Explanation: Every floor rented is a special floor, so we return 0.
 

Constraints:

1 <= special.length <= 105
1 <= bottom <= special[i] <= top <= 109
All the values of special are unique.
"""

from typing import List
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special = sorted(special)
        # All floors from bottom till first spl floor can be given to rent
        max_floors = special[0]-bottom
        for i in range(len(special)-1):
            # If 2 consecutive floors are spl floors we cannot rent both the floors
            if special[i+1]-special[i] == 1:
                continue
            # As we will not rent the spl floors the number of floors bw these floors can be rented
            max_floors = max(max_floors,(special[i+1]-special[i]-1))
        # All the floors above the last spl floor can be rented
        rem_floors = top-special[-1]
        max_floors = max(max_floors,rem_floors)
        return max_floors
    
def main():
    solution = Solution()
    bottom=28
    top=50
    special=[35,48]
    res=solution.maxConsecutive(bottom,top,special)
    print(res)

if __name__=="__main__":
    main()



        