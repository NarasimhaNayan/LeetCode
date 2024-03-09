# Minimum Common Element in Two Sorted Arrays

## Problem Statement

Given two integer arrays `nums1` and `nums2`, both sorted in non-decreasing order, the goal is to return the smallest integer that is common to both arrays. If there is no such integer, return `-1`.

An integer is considered common to `nums1` and `nums2` if both arrays contain at least one occurrence of that integer.

## Examples

### Example 1

**Input:** `nums1 = [1,2,3]`, `nums2 = [2,4]`  
**Output:** `2`  
**Explanation:** The smallest element common to both arrays is `2`.

### Example 2

**Input:** `nums1 = [1,2,3,6]`, `nums2 = [2,3,4,5]`  
**Output:** `2`  
**Explanation:** The common elements are `2` and `3`, with `2` being the smallest.

## Constraints

- `1 <= nums1.length, nums2.length <= 10^5`
- `1 <= nums1[i], nums2[j] <= 10^9`
- Both `nums1` and `nums2` are sorted in non-decreasing order.

## Approach

### Using Two Pointers

- Initialize two pointers `i` and `j` to the start of `nums1` and `nums2`, respectively.
- Iterate through both arrays simultaneously with a while loop until either pointer exceeds the length of its respective array.
- If `nums1[i]` equals `nums2[j]`, return this element as the answer.
- If `nums1[i]` is less than `nums2[j]`, increment `i` to catch up with `j`, otherwise increment `j` to catch up with `i`.

### Using Binary Search

- Iterate through one array using a for loop.
- For each element in the first array, perform a binary search in the second array.
- If `nums2[mid]` equals `nums1[i]`, we've found a common element. Return this element as the answer.
- If `nums1[i]` is less than `nums2[mid]`, adjust the search range to the left by decreasing `high`; otherwise, increase `low` to search the range to the right.