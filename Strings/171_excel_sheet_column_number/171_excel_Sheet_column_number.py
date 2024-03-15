class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count = 0

        for i in range(len(columnTitle)) :
            # print(ord(columnTitle[i])-ord('A')+1)
            char_count = pow(26,len(columnTitle)-i-1)*(ord(columnTitle[i])-ord('A')+1)
            count += char_count
            
        return count
        