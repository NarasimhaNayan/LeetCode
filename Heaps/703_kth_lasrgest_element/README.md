# Kth Largest Element in a Stream

Design a class to efficiently find the kth largest element in a stream of numbers. This class should support the insertion of numbers from the stream and the retrieval of the kth largest element at any point in time.

## Implementing the KthLargest Class

The class should include the following functionalities:

- **KthLargest(int k, int[] nums):** Constructor that initializes the object with the integer `k` and the stream of integers `nums`.
- **int add(int val):** Appends the integer `val` to the stream and returns the kth largest element in the stream after the insertion of `val`.

## Example

```plaintext
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
