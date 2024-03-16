class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix_arr = [0]*len(nums)
        # postfix_arr = [0]*len(nums)
        prefix =1
        postfix = 1
        res = [0]*len(nums)

        for i in range(len(nums)) :
            # calculating product till ith ele without including ith ele
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1,-1,-1) :
            # print(i)
            # calculating product from last ele till till ith ele without including ith ele
            res[i]*=postfix
            postfix *= nums[i]

        # print(prefix_arr)
        # print(postfix_arr)
        # for i in range(len(res)):
        #     if i == 0:
        #         res[i] = postfix_arr[i+1]
        #     elif i== len(res)-1 :
        #         res[i] = prefix_arr[i-1]
        #     else :
        #         res[i] = prefix_arr[i-1]*postfix_arr[i+1]
        return res


        

        