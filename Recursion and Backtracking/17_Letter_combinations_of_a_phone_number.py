"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

from typing import List

# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         hashset = {}
#         hashset[2] = ['a','b','c']
#         hashset[3] = ['d','e','f']
#         hashset[4] = ['g','h','i']
#         hashset[5] = ['j','k','l']
#         hashset[6] = ['m','n','o']
#         hashset[7] = ['p','q','r','s']
#         hashset[8] = ['t','u','v']
#         hashset[9] = ['w','x','y','z']
#         if len(digits) == 0 :
#             return []
#         elif len(digits) == 1:
#             return list(hashset[digits[0]])
#         elif len(digits) == 2 :
#             res = []
#             # list_temp = hashset[int(digits[0])]
#             for i in hashset[int(digits[0])]:
#                 for j in hashset[int(digits[1])]:
#                     res.append(str(i)+str(j))
#             return res
#         else :
#             res = []
#             for i in hashset[int(digits[0])]:
#                 for j in hashset[int(digits[1])]:
#                     for k in hashset[int(digits[2])]:
#                         res.append(str(i)+str(j)+str[k])
#             return res

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        hashset ={
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        temp = []
        res = []
        def computeCombinations(index,digits,temp,res):
            if len(temp) == len(digits):
                res.append(''.join(temp))
                return
            if index == len(digits) :
                return
            for i in hashset[digits[index]]:
                # print(hashset[index][i])
                temp.append(i)
                computeCombinations(index+1,digits,temp,res)
                temp.pop()
        computeCombinations(0,digits,temp,res)  
        return res

        
def main():
    solution = Solution()
    # candidates = [8,7,4,3] 
    digits = '23'
    res = solution.letterCombinations(digits)
    print(res)

if __name__ == "__main__" :
    main()