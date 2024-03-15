# Stack Implementation with Basic Operations

This document describes the implementation of a stack data structure supporting basic operations. A stack follows the Last In, First Out (LIFO) principle. The objective is to design and implement a stack that includes functions for pushing, popping, peeking at the top element, and checking if the stack is empty or full.

## Problem Statement

Implement a stack to perform the following functions:

1. **Push(num)**: Insert the given number into the stack, provided the stack is not full.
2. **Pop**: Remove and print the top element from the stack if it exists; otherwise, print `-1`.
3. **Top**: Print the top element of the stack if it exists; otherwise, print `-1`.
4. **isEmpty**: Print `1` if the stack is empty, otherwise print `0`.
5. **isFull**: Print `1` if the stack is full, otherwise print `0`.

The implementation should handle 'm' operations on the stack effectively.

### Example

Given a stack with a capacity of 2, consider the following sequence of operations:

- Operation 1 1: Insert 1 into the stack.
- Operation 1 2: Insert 2 into the stack.
- Operation 2: Remove and print the top element (prints `2`).
- Operation 3: Print the top element (now prints `1`).
- Operation 4: Check if the stack is empty (prints `0` since the stack is not empty).
- Operation 5: Check if the stack is full (prints `0` since the stack's size is 1, not at full capacity).

### Constraints

- `1 <= n, m <= 10^3`
- Time Limit: 1 second

## Approach

The stack will be implemented using an array and a pointer called `top` to keep track of the top element of the stack. The approach for each function is as follows:

- **Push(num)**: Increase `top` and add the element to the stack if `top` is less than the array length - 1, indicating the stack is not full.
- **Pop**: Store the element at `top`, decrease `top`, and print the stored element. If `top` is -1 (indicating an empty stack), print `-1`.
- **Top**: Return the element at `top` if `top` is not -1; otherwise, print `-1`.
- **isEmpty**: Check if `top` is -1. If yes, print `1` (stack is empty); otherwise, print `0`.
- **isFull**: Check if `top` equals the array length - 1. If yes, print `1` (stack is full); otherwise, print `0`.

This method ensures that all stack operations are performed in compliance with the LIFO principle, efficiently managing data insertion, removal, and status checks.
