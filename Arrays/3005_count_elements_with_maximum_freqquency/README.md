# Maximum Frequency Element Counter

## Problem Statement

Given an array `nums` consisting of positive integers, the task is to return the total count of elements in `nums` that all have the maximum frequency. The frequency of an element is defined as the number of occurrences of that element in the array.

## Examples

### Example 1

**Input:** `nums = [1,2,2,3,1,4]`  
**Output:** `4`  
**Explanation:** The elements `1` and `2` each have a frequency of `2`, which is the maximum frequency in the array. Thus, the total number of elements with the maximum frequency is `4` (`1`, `1`, `2`, `2`).

### Example 2

**Input:** `nums = [1,2,3,4,5]`  
**Output:** `5`  
**Explanation:** All elements of the array have a frequency of `1`, which is the maximum. So, the total number of elements with the maximum frequency is `5`.

## Constraints

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Approach

To solve this problem, we employ the following approach:

- Utilize a hashmap to count the frequency of all elements within the array.
- Sort the dictionary with respect to values to identify the maximum frequency. This is achieved by converting the dictionary to a list of tuples using the `.items()` method and then applying a lambda function for sorting.
- Determine the highest frequency from the sorted data.
- Sum up all frequencies that are equal to the highest frequency and return the total count.

This method efficiently calculates the total number of elements having the maximum frequency, thereby solving the problem.

