"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    # Recurssion
    def longestPalindromeRecurssion(self, s: str) -> str:
        if s == s[::-1] :
            return s
        left = self.longestPalindromeRecurssion(s[1:])
        right = self.longestPalindromeRecurssion(s[:-1])
        if len(left) >len(right):
            return left 
        else:
            return right  

    # Expanding around the center
    def longestPalindromeAroundCenter(self, s: str) -> str :
        longest_substring = ""
        for i in range(len(s)):
            # For odd longest_palindrom
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right] :
                if len(longest_substring) < len(s[left:right+1]):
                    longest_substring = s [left:right+1]
                left-=1
                right+=1

            # For even longest_palindrom
            left = i 
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right] :
                if len(longest_substring) < len(s[left:right+1]):
                    longest_substring = s [left:right+1]
                left-=1
                right+=1 
        return longest_substring
    
def main():
    solution = Solution()
    s = "aaca"
    res = solution.longestPalindromeAroundCenter(s)
    print(res)

if __name__ == "__main__":
    main()