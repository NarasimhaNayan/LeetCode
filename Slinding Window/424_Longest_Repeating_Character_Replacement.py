"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Base condition
        if len(s) == 0 or len(s) == 1 :
            return len(s)
        # have hashmap to keep track of count of chars
        i,j = 0,0
        hashmap = {}
        max_len = 0
        # max_occurance_of_char = 0

        while j < len(s):
            if s[j] not in hashmap:
                hashmap[s[j]] = 1
            else :
                hashmap[s[j]] += 1

            # Shrinking window
            while ((j-i+1)- max(hashmap.values())) > k :
                    hashmap[s[i]] -= 1
                    i+=1
            max_len = max(max_len,(j-i+1))
            # Expanding window
            j+=1
        return max_len
    
def main():
    solution = Solution()
    s = "ABABBA"
    k = 2
    res = solution.characterReplacement(s,k)
    print(res)

if __name__ == "__main__" :
    main()