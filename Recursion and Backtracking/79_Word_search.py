"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or 
vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

from typing import List

class Solution:
    def findpath(self,board,row,col,index,word,row_len,col_len,sett,res):
        if index == len(word):
            return True
        if row < 0 or row == row_len or col < 0 or col == col_len or board[row][col] != word[index] or (row,col) in sett  :
            return False
        
        # res = 
        sett.add((row,col))
        res= (self.findpath(board,row,col+1,index+1,word,row_len,col_len,sett,res) or 
                self.findpath(board,row+1,col,index+1,word,row_len,col_len,sett,res) or 
                self.findpath(board,row,col-1,index+1,word,row_len,col_len,sett,res) or 
                self.findpath(board,row-1,col,index+1,word,row_len,col_len,sett,res))
        sett.remove((row,col))
        return res

    
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len = len(board)
        col_len = len(board[0])
        res = False
        sett = set()
        for row in range(row_len):
            for col in range(col_len):
                if word[0] == board[row][col]:
                    res = self.findpath(board,row,col, 0,word,row_len,col_len,sett,res)
                    if res == True :
                        return res
        return res
    
def main():
    solution = Solution()
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCEFSADEESE"
    res = solution.exist(board,word)
    print(res)

if __name__ == "__main__":
    main()
    