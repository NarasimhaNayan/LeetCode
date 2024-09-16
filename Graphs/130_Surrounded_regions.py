"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""

from typing import List
from collections import deque
class Solution:
    # def bfs(self, i, j, board) :
    #     count = 0
    #     adj = [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]
    #     for r,c in adj :
    #         if board[r][c] == 'X' :
    #             count+=1
    #     # Check if all 3 sides are surrounded by X
    #     if count > 2:
    #         board[i][j] = 'X'

    def bfs(self, queue, board):
        while len(queue) > 0 :
            i,j = queue.popleft()
            adj = [(i-1,j), (i,j+1), (i+1,j), (i,j-1)]
            for r,c in adj:
                if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == 'O' :
                    queue.append((r,c))
                    board[r][c] = 'N'

    def dfs(self, i, j, board):
        if 0>i or i==len(board) or 0>j or j==len(board[0]) or board[i][j] == 'X' or board[i][j] == 'N' :
            return
        board[i][j] = 'N'
        adj = [(i-1,j), (i,j+1), (i+1,j), (i,j-1)]
        for r,c in adj:
            self.dfs(r,c,board)
            


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        # queue = deque()

        if rows < 3 or cols < 3 :
            return

        # Find O's in edges and O's which are connected to them.
        for i in range(cols):
            # Top row
            if board[0][i] == 'O':
                # board[0][i] = 'N'
                # queue.append((0,i))
                # self.bfs(queue,board)
                self.dfs(0,i,board)
            # Bottom row
            if board[rows-1][i] == 'O':
                # board[rows-1][i] = 'N'
                # queue.append((rows-1,i))
                # self.bfs(queue,board)
                self.dfs(rows-1,i,board)
        
        for i in range(rows):
            # Leftmost Col
            if board[i][0] == 'O':
                # board[i][0] = 'N'
                # queue.append((i,0))
                # self.bfs(queue,board)
                self.dfs(i,0,board)
            # Rightmost col 
            if board[i][cols-1] == 'O':
                # board[i][cols-1] = 'N'
                # queue.append((i,cols-1))
                # self.bfs(queue,board)
                self.dfs(i,cols-1,board)

        # We will not checl the borders for O
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' :
                    board[i][j] = 'X'
                elif board[i][j] == 'N' :
                    board[i][j] = 'O'
        

def main():
    solution = Solution()
    board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    solution.solve(board)
    print(board)

if __name__ == "__main__" :
    main()
        