"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #  To avoid Out of Bounds Error we initialize shorted array to num 1 so that mid2 doesnt go out of bounce
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1

        low = 0
        high = len(nums1)-1

        while low <= high:
            # Picking the left half of nums1+nums2
            # First we pick ele till mid 1 from nums1 using binary search.  
            mid1 = (low+high)//2
            # For mid2 we do not need to apply binary search again. 
            # Because the number of elements in the left half = ele till mid 1 from nums1 + (len(nums1+nums2)/2-the number of ele seleceted in nums1 (i.e.. mid1 ele))
            mid2 = (len(nums1)+len(nums2))//2 - mid1

            if mid1 > 0:
                # Prev ele of mid is the last ele from left half in that particular array
                l1 = nums1[mid1-1]
            else:
                l1 = float('-inf')

            if mid1 < len(nums1) :
                r1 = nums1[mid1]
            else:
                r1 = float('inf')
            
            if mid2 > 0:
                # Prev ele of mid is the last ele from left half in that particular array
                l2 = nums2[mid2-1]
            else:
                l2 = float('-inf')

            
            if mid2 < len(nums2) :
                r2 = nums2[mid2]
            else:
                r2 = float('inf')
            
            # Comparing last ele of left half of nums1 with the first ele of right half of nums2
            # compare last element of arr2 left half with first ele of arr1 in the right half
            # if lefts < rights then find median
            if l1 <= r2 and l2 <= r1 :
                if (len(nums1) + len(nums2))%2 == 0 :
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return (min(r1,r2))

            if l2 > r1:
                low = mid1+1
            else:
                high = mid1-1 
        return 0
    
def main():
    solution = Solution()
    nums1 = [1,3]
    nums2 = [2]
    res = solution.findMedianSortedArrays(nums1,nums2)
    print(res)

if __name__ == "__main__":
    main()