# Queue Implementation Using Two Stacks

This guide describes how to implement a First-In-First-Out (FIFO) queue using two stacks. By utilizing only standard stack operations, this approach simulates all functionalities of a normal queue, including push, peek, pop, and checking if the queue is empty.

## Problem Statement

The challenge is to simulate the behavior of a queue, ensuring FIFO order, using two stacks. The queue should support the following operations:

- `void push(int x)`: Inserts element x to the back of the queue.
- `int pop()`: Removes the element from the front of the queue and returns it.
- `int peek()`: Returns the element at the front of the queue without removing it.
- `boolean empty()`: Checks if the queue is empty and returns true if it is, otherwise false.

### Constraints

- The value of `x` is between 1 and 9.
- Up to 100 calls will be made to push, pop, peek, and empty.
- All the calls to pop and peek are valid.

## Approach

The implementation involves two stacks which will simulate the queue operations as follows:

- **Initialization**: Two stacks are initialized to help in simulating the queue operations. The first stack (`stack1`) is used for the push operation, and the second stack (`stack2`) for the pop and peek operations.

- **Push Operation**: The push operation is straightforward; elements are pushed onto `stack1`, adhering to the LIFO (Last-In-First-Out) principle of a stack.

- **Pop Operation**: To perform the pop operation in FIFO order, we check if `stack2` is empty. If it is not, we directly pop from `stack2`. If `stack2` is empty, we transfer all elements from `stack1` to `stack2`, thereby reversing the order of elements to match FIFO, and then perform the pop operation from `stack2`.

- **Peek Operation**: The peek operation is similar to pop but without removing the element from the queue. If `stack2` is empty, elements are transferred from `stack1` to `stack2` to ensure the correct order. The top element of `stack2` is then returned. If the pop operation is performed for peeking, the element is pushed back onto `stack2` to maintain the queue's state.

- **Empty Operation**: To check if the queue is empty, the emptiness of both stacks is verified. If both `stack1` and `stack2` are empty, the queue is considered empty; otherwise, it is not.

By leveraging two stacks and managing the transfer of elements between them, this method effectively simulates a FIFO queue with only LIFO stack operations. This approach ensures that all queue operations are efficiently implemented using stacks.
