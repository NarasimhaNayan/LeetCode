# Top K Frequent Words

## Problem Statement

Given an array of strings `words` and an integer `k`, the goal is to return the `k` most frequent strings. The answer should be sorted by the frequency from highest to lowest, and words with the same frequency should be sorted by their lexicographical order.

## Examples

### Example 1

**Input:** words = ["i","love","leetcode","i","love","coding"], k = 2  
**Output:** ["i","love"]  
**Explanation:** "i" and "love" are the two most frequent words. "i" comes before "love" due to a lower alphabetical order.

### Example 2

**Input:** words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4  
**Output:** ["the","is","sunny","day"]  
**Explanation:** "the", "is", "sunny", and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2, and 1 respectively.

## Constraints

- `1 <= words.length <= 500`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- `k` is in the range `[1, The number of unique words[i]]`

## Approach

To find the `k` most frequent words, we will utilize a max heap to keep track of word frequencies in descending order.

- Count the occurrence of each word in the `words` array. This can be efficiently done using a hashmap or the `collections.Counter` function in Python, which automatically creates a dictionary of words as keys and their frequencies as values.

- Convert the frequency dictionary into a list of tuples `(-value, key)` to prepare for heap insertion. The negative value is used because Python's `heapq` module implements a min-heap, and inverting the frequencies allows us to simulate a max heap.

- Push all elements from the list of tuples into a heap.

- Pop the top `k` elements from the heap. Since we are using negative frequencies, the most negative (i.e., highest frequency) elements will be popped first. For words with the same frequency, the heap will ensure they are sorted lexicographically due to the tuple's second element being the word itself.

- **Step 5:** Collect the words from these top `k` elements into an array and return it.

This approach ensures that we efficiently find and return the `k` most frequent words sorted by frequency and lexicographical order.

