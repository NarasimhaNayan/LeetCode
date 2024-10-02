"""
Islands and Treasure

You are given a m×n m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the 
value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}

"""
from typing import List
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j,0))


        while len(queue) > 0:
            row,col,time = queue.popleft()
            neigbhours = [(row-1,col),(row,col+1),(row+1,col),(row,col-1)]
            for i,j in neigbhours:
                if 0>i or rows==i or 0>j or cols==j or grid[i][j] == -1 or grid[i][j] != 2147483647 :
                    continue
                grid[i][j]=time+1
                queue.append((i,j,time+1))

        print(grid)

def main():
    solution = Solution()
    grid = [[2147483647,-1,0,2147483647], [2147483647,2147483647,2147483647,-1], [2147483647,-1,2147483647,-1], [0,-1,2147483647,2147483647]]
    solution.islandsAndTreasure(grid)

if __name__ == "__main__":
    main()