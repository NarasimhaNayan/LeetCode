from collections import deque
from typing import List
class Solution:
    # BFS
    def bfs(self,grid,queue,visited,max_time) :
        while len(queue) :
            flag = 0
            i,j,time = queue.popleft()
            # Upper
            if i>0 and grid[i-1][j] == 1 and visited[i-1][j] == 0:
                visited[i-1][j] = 1
                grid[i-1][j] = 2
                queue.append((i-1,j,time+1))
                max_time[0] = max(max_time[0],time+1)
            # Right
            # print(i,j)
            if j+1<len(grid[i]) and grid[i][j+1] == 1 and visited[i][j+1] == 0:
                visited[i][j+1] = 1
                grid[i][j+1] = 2
                queue.append((i,j+1,time+1))
                max_time[0] = max(max_time[0],time+1)
            # Bottom
            if i+1<len(grid) and grid[i+1][j] == 1 and visited[i+1][j] == 0:
                visited[i+1][j] = 1
                grid[i+1][j] = 2
                queue.append((i+1,j,time+1))
                max_time[0] = max(max_time[0],time+1)
            # Left  
            if j>0 and grid[i][j-1] == 1 and visited[i][j-1] == 0:
                visited[i][j-1] = 1
                grid[i][j-1] = 2
                queue.append((i,j-1,time+1))
                max_time[0] = max(max_time[0],time+1)
                
                
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # Visited
        visited = []
        for _ in range(m):
            visited.append([0]*n)
        print(visited)
        # Queue
        queue = deque()
        time = 0
        max_time = [0]

        # Find first rotten orange
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 and visited[i][j] == 0 :
                    visited[i][j] = 1
                    queue.append((i,j,time))
        self.bfs(grid,queue,visited,max_time)
        
        # To check if there are any fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 :
                    return -1
        return max_time[0] 

def main():
    solution = Solution()
    s = [[2,1,1],[1,1,1],[0,1,2]]
    res = solution.orangesRotting(s)
    print(res)

if __name__ == "__main__":
    main()