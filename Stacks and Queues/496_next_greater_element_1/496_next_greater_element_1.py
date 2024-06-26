class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = [] # to keep track of next greater ele
        dic = {} # To store next greater ele in nums2 so that we can compare it with nums1 elements.
        res = []

        # We will iterate from right to left so that it would be easier for us to find next greater ele.
        for i in range(len(nums2)-1,-1,-1) :
            if i == len(nums2)-1 :
                # the rightmost element will not have any greater elements as there will be no elements. 
                # So mapping -1 for the last element
                dic[nums2[i]] = -1
            # next we will remove all the smaller elements than nums2[i] from the stack 
            # and the top element which is greater than nums[i] will be the greatest ele
            while stack and nums2[i] >= stack[-1] :
                stack.pop()
            
            # If all elements are popped then we can conclude that there are no greater elements to the right of nums[i]
            if len(stack) == 0:
                dic[nums2[i]] = -1
            elif nums2[i] < stack[-1]:
                dic[nums2[i]] = stack[-1]

            # We will append the nums2[i] to the stack and treat this as tos and we will check for next elements if this is larger or smaller and proceed
            stack.append(nums2[i])

        # Iterate through nums1 and check if nums1[i] is present in dictinory
        for num in nums1 :
            if num in dic :
                res.append(dic[num])

        return res
            
