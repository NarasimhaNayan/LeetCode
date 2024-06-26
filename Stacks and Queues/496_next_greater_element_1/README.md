# Finding Next Greater Element for Subarray Elements

This guide explores an efficient approach to find the next greater element for each element of a subset array (`nums1`) within a larger array (`nums2`). Each element in `nums1` is guaranteed to be present in `nums2`, and the goal is to determine the first greater element to the right of `nums2[j]`, where `nums1[i] == nums2[j]`. If no such element exists, the answer for this query is `-1`.

## Examples

- **Example 1:**

  Input: `nums1 = [4,1,2]`, `nums2 = [1,3,4,2]`
  
  Output: `[-1,3,-1]`
  
  Explanation: The next greater element for each value of `nums1` is as follows:
  - For `4`, no next greater element, hence `-1`.
  - For `1`, the next greater element is `3`.
  - For `2`, no next greater element, hence `-1`.

- **Example 2:**

  Input: `nums1 = [2,4]`, `nums2 = [1,2,3,4]`
  
  Output: `[3,-1]`
  
  Explanation: The next greater element for each value of `nums1` is as follows:
  - For `2`, the next greater element is `3`.
  - For `4`, no next greater element, hence `-1`.

## Constraints

- `1 <= nums1.length <= nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 104`
- All integers in `nums1` and `nums2` are unique.
- All the integers of `nums1` also appear in `nums2`.

## Approach

To efficiently find the next greater elements, we leverage a stack and a dictionary:

- **Initialization**: A stack is used to keep elements in ascending order from top to bottom. A dictionary stores the mappings of each element in `nums2` to its next greater element.
- **Iteration**: We traverse `nums2` from right to left, enabling an easier identification of the next greater elements.
  - For the rightmost element, map `-1` as it has no elements to its right.
  - Use a while loop to remove all smaller elements than `nums2[i]` from the stack. The top of the stack (if any) after removals will be the next greater element.
  - If the stack becomes empty, map `nums2[i]` to `-1`, indicating no greater element to its right.
  - If the stack is not empty, map `nums2[i]` to the top element of the stack.
  - Append `nums2[i]` to the stack for subsequent iterations.
- **Mapping and Result Formation**: Once we have the mapping of next greater elements for `nums2`, iterate through `nums1` to locate the corresponding mappings. Append these values to the result array and return it.

This method ensures an optimal solution to find the next greater elements by maintaining a decreasing stack and efficiently mapping the greater elements for quick lookup.
