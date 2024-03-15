# Finding the Pivot Integer

This document outlines a method to find a pivot integer `x` for a given positive integer `n`, where the sum of all elements from 1 to `x` (inclusive) equals the sum of all elements from `x` to `n` (inclusive). If such an integer exists, the method returns the pivot integer `x`; otherwise, it returns -1. It is assured that there will be at most one pivot index for the given input.

## Problem Statement

Given a positive integer `n`, find the pivot integer `x` such that:

- The sum of all elements between 1 and `x` inclusively equals the sum of all elements between `x` and `n` inclusively.
- Return the pivot integer `x`. If no such integer exists, return -1.

### Examples

- **Example 1:**

  Input: `n = 8`
  
  Output: `6`
  
  Explanation: 6 is the pivot integer since the sum of numbers 1 to 6 is equal to the sum of numbers 6 to 8, both summing up to 21.

- **Example 2:**

  Input: `n = 1`
  
  Output: `1`
  
  Explanation: 1 is the pivot integer since the sums on both sides are equal, considering there's only one element.

- **Example 3:**

  Input: `n = 4`
  
  Output: `-1`
  
  Explanation: There's no pivot integer that satisfies the condition.

### Constraints

- `1 <= n <= 1000`

## Approach

To find the pivot integer `x`, the approach involves calculating prefix and postfix sums and comparing them to identify the pivot. Here's a step-by-step explanation:

- **Initialize Prefix and Postfix Sums**: Calculate the cumulative sum from the start (prefix sum) and the cumulative sum from the end (postfix sum) for the range from 1 to `n`.

- **Comparison for Pivot**: Iterate through the calculated sums to check if there exists an index `i` for which `prefix_sum[i] == postfix_sum[n-i-1]`. If such an index is found, `i+1` is the pivot integer.

- **Return Value**: If a matching index is found, return `i+1` as the pivot integer. If no such index exists, return `-1`.

This method efficiently determines the pivot integer by utilizing sum comparisons, avoiding the need for extensive computations or iterations through the entire range multiple times.

