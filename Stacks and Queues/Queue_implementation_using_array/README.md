# Simple Queue Implementation Using Arrays

This document provides a guide on implementing a simple queue using arrays. A queue is a linear data structure that operates under the principle of First In, First Out (FIFO), meaning that elements are inserted from the rear and removed from the front.

## Problem Statement

The task is to implement a queue that supports two types of operations:

1. **Enqueue (e)**: Add element `e` to the end of the queue.
2. **Dequeue**: Remove the element from the front of the queue. If the queue is empty, return `-1`.

The implementation should efficiently manage 'query' queries, which could be either enqueueing or dequeueing operations.

### Constraints

- `1 <= query <= 10^5`
- `1 <= e <= 10^6`

## Approach

The queue will be implemented using an array with two pointers, `front` and `rear`, to manage the enqueue and dequeue operations as follows:

- **Initialization**: Initialize the queue with an array. The `front` and `rear` pointers both start at -1 to indicate an empty queue.

- **Enqueue Operation**:
  - Check if the queue is full. This condition is true if `rear` is at the last position of the array (`rear = arr_len - 1`). If the queue is full, no insertion can be made.
  - If not full, increment `rear` and insert the new element at this position. If it's the first element being added (`front` is -1), also set `front` to 0.

- **Dequeue Operation**:
  - Check if the queue is empty. This condition is true if `front` is -1 or `front > rear`.
  - If the queue is not empty, store the element at `front`, increment `front`, and return the stored element. If after incrementing `front` it goes beyond `rear`, reset `front` and `rear` to -1 to indicate an empty queue.
  - If the queue is empty, return `-1`.

- **Queue Empty Check**: Determine if the queue is empty by checking if `front` is greater than `rear` or `front` is -1.

- **Queue Full Check**: The queue is considered full when `rear = arr_len - 1`.

This approach allows for the efficient handling of enqueue and dequeue operations while maintaining the FIFO nature of the queue. The use of front and rear pointers facilitates the dynamic movement within the array, accommodating the linear progression of elements as they are added and removed.
