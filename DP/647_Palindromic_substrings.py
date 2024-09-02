"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        no_of_palindrom_substring = 0
        for i in range(len(s)):
            # For odd_palindorm
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right] :
                no_of_palindrom_substring += 1
                left -= 1
                right += 1
            
            # For even_palindrom
            left = i 
            right = i+1
            while left >= 0 and right < len(s) and s[left] ==s[right] :
                no_of_palindrom_substring += 1
                left -= 1
                right += 1

        return no_of_palindrom_substring
    
def main():
    solution = Solution()
    s = "aaca"
    res = solution.countSubstrings(s)
    print(res)

if __name__ == "__main__":
    main()