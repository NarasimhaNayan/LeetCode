# Product of Array Except Self

This guide explains how to compute an array where each element is the product of all elements in the original array except itself, adhering to the constraints that the solution must run in O(n) time without using the division operation.

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` equals the product of all the elements of `nums` except `nums[i]`. It is guaranteed that the product of any prefix or suffix of `nums` will fit in a 32-bit integer.

### Examples

- **Example 1:**

  Input: `nums = [1,2,3,4]`
  
  Output: `[24,12,8,6]`
  
  Each element in the output array is the product of all other elements except the current one. For instance, `answer[0] = 2*3*4 = 24`, and similarly for the others.

- **Example 2:**

  Input: `nums = [-1,1,0,-3,3]`
  
  Output: `[0,0,9,0,0]`
  
  Elements corresponding to a zero in the input array result in all zeros in the output array because the product will include zero.

### Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

## Approach

To compute the desired output without using the division operation and in O(n) time complexity, we can utilize the concept of prefix and postfix product arrays. However, to adhere to the follow-up challenge of achieving O(1) extra space complexity (excluding the output array), we modify this approach slightly:

1. **Initial Prefix Product**: Start by calculating the prefix product for each element and store it in the result array (`res`). For the first element, this product is 1 as there are no elements before it. Iterate through the array from the second element, updating `res[i]` as the product of `res[i-1]` and `nums[i-1]`. This step gives us the product of all elements to the left of each index.

2. **Postfix Product Multiplication**: Next, traverse the array backwards, starting from the last element. Keep track of the postfix product as you move towards the first element. Multiply the current value in `res[i]` by this postfix product before updating the postfix product by multiplying it with `nums[i]`. This ensures that each element of `res` is multiplied by the product of all elements to its right.

This two-step approach effectively calculates the product of all elements except `nums[i]` for each element in the input array, satisfying the problem constraints and the follow-up challenge of minimal space usage.
