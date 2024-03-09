class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # for i in range(len(nums1)):
        #     # key = nums[i]
        #     low = 0
        #     high = len(nums2)-1
        #     while low <= high :
        #         mid = (low+high)//2
        #         if nums2[mid] == nums1[i] :
        #             return nums2[mid]
        #         elif nums2[mid] > nums1[i] :
        #             high = mid-1
        #         else :
        #             low = mid+1
        # return -1
    
        # Two pointer solution
        i = 0
        j = 0
        while i<len(nums1) and j<len(nums2) :
            if nums1[i] == nums2[j] :
                return nums1[i]
            elif nums1[i] < nums2[j] :
                i+=1
            else :
                j+=1
        return -1
