"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        hashmap = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hashmap:
                temp = []   
            else:
                temp = hashmap[sorted_word]
            temp.append(word)
            hashmap[sorted_word] = temp
        # print(hashmap)
        result = []
        for lst in hashmap:
            result.append(hashmap[lst])
        return result


def main():
    solution = Solution()
    strs=["eat","tea","tan","ate","nat","bat"]
    res = solution.groupAnagrams(strs)
    print(res)

if __name__ == "__main__":
    main()