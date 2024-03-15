class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix_sum = 0
        postfix_sum = 0
        prefix_arr = []
        postfix_arr = []
        for i in range(1,n+1):
            prefix_sum += i
            prefix_arr.append(prefix_sum)

        for i in range(n,0,-1):
            postfix_sum += i
            postfix_arr.append(postfix_sum)


        for i in range(len(prefix_arr)) :
            if prefix_arr[i] == postfix_arr[n-i-1] :
                return i+1
        return -1
        