"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        temp=[]
        while i<len(s):
            if s[i].isalpha() or s[i].isdigit():
                if s[i].isalpha():
                    temp.append(s[i].lower()) 
                else :   
                    temp.append(s[i])
            i+=1
        result_temp_string = ''.join(temp)
        print(result_temp_string)
        i=0
        j=len(result_temp_string)-1
        while i<j:
            if result_temp_string[i] != result_temp_string[j]:
                return False
            i+=1
            j-=1
        return True 

def main():
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    res = solution.isPalindrome(s)
    print(res)

if __name__ == "__main__" :
    main()