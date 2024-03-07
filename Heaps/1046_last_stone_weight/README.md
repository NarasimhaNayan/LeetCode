# Last Stone Weight

## Problem Statement

Given an array of integers `stones` where `stones[i]` represents the weight of the `i`th stone, we play a game with the stones. On each turn, we choose the two heaviest stones and smash them together. The outcomes of the smash are as follows:

- If the stones are of equal weight `x == y`, both stones are completely destroyed.
- If the stones are of different weights `x != y`, the lighter stone is destroyed, and the weight of the heavier stone is reduced by the weight of the lighter stone.

The game ends when there is at most one stone left. The objective is to return the weight of this last remaining stone, or `0` if there are no stones left.

## Examples

### Example 1

**Input:** stones = [2,7,4,1,8,1]  
**Output:** 1  
**Explanation:**  
- Combine stones of weight 7 and 8 (heaviest pair) to get 1. The array becomes [2,4,1,1,1].
- Combine stones of weight 2 and 4 (heaviest pair) to get 2. The array becomes [2,1,1,1].
- Combine stones of weight 2 and 1 (heaviest pair) to get 1. The array becomes [1,1,1].
- Combine stones of weight 1 and 1 (heaviest pair) to get 0. The array becomes [1].
- The weight of the last stone is 1.

### Example 2

**Input:** stones = [1]  
**Output:** 1  
**Explanation:** There is only one stone in the array, so its weight is returned.

## Constraints

- 1 <= stones.length <= 30
- 1 <= stones[i] <= 1000

## Approach

Aim: Return the weight of the last remaining stone.

Approach:
- Convert the array to a max heap to efficiently pop the two maximum elements since we need to smash the two heaviest stones together.
- Check if the elements popped are different. If they are, push the difference in their weights back onto the heap (as a max heap element). Repeat this process until the length of the heap is greater than 1.
- Check if there are any elements left in the heap. Return the negative of the number (due to max heap conversion) if there is one element left; otherwise, return 0.

This approach ensures we always have access to the two heaviest stones and can perform the smash operation according to the game rules.

