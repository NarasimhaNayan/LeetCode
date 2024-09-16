"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
from typing import List
from collections import deque
class Solution:
    def dfs(self,r,c,visited,grid,max_area,area):
        if r < 0 or r== len(grid) or c < 0 or c == len(grid[0]) or grid[r][c] == 0 or visited[r][c] == 1 :
            return
        visited[r][c] = 1
        area[0]+=1
        adj = [(r-1,c),(r,c+1),(r+1,c),(r,c-1)]
        for i,j in adj:
            
        #     if grid[r][c] == 1 and visited[r][c] == 0:
                
                self.dfs(i,j,visited, grid, max_area,area)
        # self.dfs(r-1,c,visited,grid,max_area,area)
        # self.dfs(r,c+1,visited,grid,max_area,area)
        # self.dfs(r+1,c,visited,grid,max_area,area)
        # self.dfs(r,c-1,visited,grid,max_area,area)

        # if max_area[0] < area[0] :
        max_area[0] = max(max_area[0], area[0])


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Initializations
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        max_area = [0]
        area = [0]
        for _ in range(rows):
            visited.append([0]*cols)
        
        # Finding cells starting with 1 to mark as start of island and thaat not visited
        for i in range(rows) :
            for j in range(cols) :
                if grid[i][j] == 1 and visited[i][j] == 0:
                        area[0] = 0
                        self.dfs(i,j,visited, grid,max_area,area)

        return max_area[0]

def main():
    solution = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    max_area = solution.maxAreaOfIsland(grid)
    print(max_area)

if __name__ == "__main__" :
    main()