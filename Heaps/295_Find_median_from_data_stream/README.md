# Median Finder Implementation

This guide explains the implementation of the `MedianFinder` class, designed to find the median of a stream of integers. The median is the middle value in an ordered list of numbers, and if the list's size is even, the median is the average of the two middle numbers.

## Problem Statement

Implement the `MedianFinder` class with the following functionalities:

- `MedianFinder()`: Initializes the `MedianFinder` object.
- `void addNum(int num)`: Adds the integer `num` from the data stream to the data structure.
- `double findMedian()`: Returns the median of all elements so far. The answer will be accepted if it is within \(10^{-5}\) of the actual answer.

### Examples

- **Input**: `["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]`, `[[], [1], [2], [], [3], []]`
- **Output**: `[null, null, null, 1.5, null, 2.0]`
- **Explanation**: Initially, the median finder is empty. After adding 1 and 2, the median is 1.5. After adding 3, the median becomes 2.0.


## Constraints

- `-10^5 <= num <= 10^5`
- There will be at least one element in the data structure before calling `findMedian`.
- At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.

## Approach

The approach to finding the median in a stream of integers involves using heaps to divide the data into two halves, allowing quick retrieval of the middle elements to calculate the median.

- **Initialization**: Two heaps are used, a max heap (`maxHeap`) for the left half of the elements and a min heap (`minHeap`) for the right half.
- **Adding an Element**:
    1. Add the element to `maxHeap` (insert the negative value to keep the maximum element at the top).
    2. Ensure the element at the top of `maxHeap` is less than the root of `minHeap`. If not, pop the top of `maxHeap` and add it to `minHeap`.
    3. If `maxHeap` has more than one extra element compared to `minHeap`, move the top element from `maxHeap` to `minHeap`. Conversely, if `minHeap` has more elements, move the top from `minHeap` to `maxHeap` to maintain balance.
- **Finding the Median**:
    - If the combined length of both heaps is odd, return the top of `maxHeap` as the median.
    - If even, calculate the average of the tops of `maxHeap` and `minHeap` and return it as the median.

This method ensures an efficient and dynamic calculation of the median as new elements are added to the data stream.
