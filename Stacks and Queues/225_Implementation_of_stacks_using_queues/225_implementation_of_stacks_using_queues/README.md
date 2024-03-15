# Stack Implementation Using Two Queues

This documentation outlines the approach to implement a Last-In-First-Out (LIFO) stack using two queues. The implementation supports all standard stack operations including push, pop, top, and checking if the stack is empty. This method utilizes only the standard operations of a queue, such as push to back, peek/pop from front, size, and is empty checks.

## Problem Statement

The task is to simulate a stack's behavior using two queues. The stack should support the following operations:

- `void push(int x)`: Pushes element x to the top of the stack.
- `int pop()`: Removes the element on the top of the stack and returns it.
- `int top()`: Returns the element on the top of the stack without removing it.
- `boolean empty()`: Returns true if the stack is empty, otherwise false.

### Constraints

- The value of `x` is between 1 and 9.
- A maximum of 100 calls will be made to the methods push, pop, top, and empty.
- All calls to pop and top are valid.

## Approach

The implementation of a stack using two queues involves a primary queue (`q1`) for the stack operations and a secondary queue (`q2`) as a helper during certain operations. The approach for each operation is as follows:

- **Push Operation**: Directly push the new element to the back of `q1`, which serves as the primary queue.

- **Pop Operation**: To simulate the pop operation of a stack, we transfer all elements except the last from `q1` to `q2`. The last element of `q1` is the one to be popped. After popping this element, we swap `q1` and `q2` to maintain the stack order in the primary queue.

- **Top Operation**: Similar to the pop operation, we move elements from `q1` to `q2` until we reach the last element. This last element is the "top" element of the stack. Unlike pop, after accessing the top element, we also move it to `q2` before swapping `q1` and `q2`.

- **Empty Operation**: The stack is considered empty if `q1` has no elements. Therefore, we return true if the length of `q1` is zero; otherwise, false.

This method efficiently simulates stack operations using two queues by leveraging the queue's FIFO (First-In-First-Out) nature to mimic the LIFO behavior of a stack. The swapping of queues ensures that the most recently added element (which would be at the back of `q1`) is accessible for pop and top operations, maintaining the stack's LIFO property.
