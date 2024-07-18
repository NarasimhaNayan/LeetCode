"""
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""
from typing import List

class Solution:
    # wrtie a function to check if the string is a palindrome
    def isPalindrome(self,string) :
        start = 0
        end = len(string)-1
        while start <= end:
            if string[start] != string[end] :
                return False
            start += 1
            end -= 1
        return True
    
    # function to findPartitions
    def findPartitions(self,temp,s,index,res):
        if index == len(s):
            res.append(temp.copy()) 
            return
        for i in range(index,len(s)):
            if self.isPalindrome(s[index:i+1]):
                temp.append(s[index:i+1])
                self.findPartitions(temp,s,i+1,res)
                temp.pop()
         
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.findPartitions([],s,0,res)
        return res

def main():
    solution = Solution()
    s = "abac"
    res = solution.partition(s)
    print(res)

if __name__ == "__main__":
    main()