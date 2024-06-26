class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        res = []
        # print(res)
        for i in range(len(arr)-1,-1,-1):
            if len(arr[i]) > 0 :
                res.append(arr[i])

        for i in range(len(res)):
            if i < len(res)-1 :
                res[i] = res[i]+" "
        
        return ''.join(res)

        