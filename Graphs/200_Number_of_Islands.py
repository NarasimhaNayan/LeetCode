"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all 
four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

from collections import deque
from typing import List
class Solution:
    # BFS traversal
    def bfs(self,row,col,grid,queue,visited):
        while len(queue) :
            # print(queue)
            i,j = queue.popleft()
            
            visited[i][j] = 1
            # Check for surrounding cells for land and add them to queue and visited
            # Upper
            if i-1 >=0 and int(grid[i-1][j]) == 1 and visited[i-1][j] == 0:
                visited[i-1][j] = 1
                queue.append((i-1,j))
            # upper right
            # if i-1 >=0 and j+1 < len(grid[i]) and int(grid[i-1][j+1]) == 1 and visited[i-1][j+1] == 0:
            #     visited[i-1][j+1] = 1
            #     queue.append((i-1,j+1))
            # Right
            # m = len(grid[i])
            if j+1 < len(grid[i]) and int(grid[i][j+1]) == 1 and visited[i][j+1] == 0:
                visited[i][j+1] = 1
                queue.append((i,j+1))
            # bottom right
            # if i+1 < len(grid) and j+1<len(grid[i]) and int(grid[i+1][j+1]) == 1 and visited[i+1][j+1] == 0:
            #     visited[i+1][j+1] = 1
            #     queue.append((i+1,j+1))
            #Bottom
            if i+1 < len(grid) and int(grid[i+1][j]) == 1 and visited[i+1][j] == 0:
                visited[i+1][j] = 1
                queue.append((i+1,j))
            # # Bottom Left
            # if i+1 < len(grid) and j-1 >= 0 and int(grid[i+1][j-1]) == 1 and visited[i+1][j-1] == 0:
            #     visited[i+1][j-1] = 1
            #     queue.append((i+1,j-1))
            # Left
            if j-1>=0 and int(grid[i][j-1]) == 1 and visited[i][j-1] == 0:
                visited[i][j-1] = 1
                queue.append((i,j-1))
            # # Upper Left
            # if i-1 >= 0 and j-1 >= 0 and int(grid[i-1][j-1]) == 1 and visited[i-1][j-1] == 0:
            #     visited[i-1][j-1] = 1
            #     queue.append((i-1,j-1))

    # DFS Traversal
    def dfs(self,i,j,grid,visited):
        if i<0 or i==len(grid) or j<0 or j==len(grid[i]) or int(grid[i][j])==0 or visited[i][j]==1:
            return
        visited[i][j]=1
        self.dfs(i-1,j,grid,visited)
        self.dfs(i,j+1,grid,visited)
        self.dfs(i+1,j,grid,visited)
        self.dfs(i,j-1,grid,visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        # Visited arr
        m=len(grid)
        n=len(grid[0])
        visited = []
        for i in range(m):
            visited.append([0]*n)
        # print(visited)
        # Queue
        queue = deque()

        no_of_island = 0

        # Finding Starting node (finding number of islands)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # if the particular cell is not visited and is land
                if visited[i][j] == 0 and int(grid[i][j]) == 1:
                    no_of_island += 1
                    # visited[i][j] =1
                    # queue.append((i,j))
                    # self.bfs(i,j,grid,queue,visited)
                    self.dfs(i,j,grid,visited)

        return no_of_island

def main():
    solution = Solution()
    s = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    res = solution.numIslands(s)
    print(res)

if __name__ == "__main__":
    main()