# Custom String Sorting

This utility is designed to permute the characters of a given string `s` to match a previously defined custom order specified by the string `order`. Each character in `order` is unique and sorted in a custom manner. The task is to rearrange `s` such that, if a character `x` occurs before a character `y` in `order`, then `x` should occur before `y` in the permuted string. The function returns any valid permutation of `s` that satisfies this condition.

## Problem Statement

Given two strings `order` and `s`, where all characters of `order` are unique and were sorted in some custom order previously, permute the characters of `s` so that they match the custom order specified by `order`. Specifically, if a character `x` occurs before a character `y` in `order`, then `x` should occur before `y` in the permuted string. Return any permutation of `s` that adheres to this rule.

### Examples

- **Example 1:**

  Input: `order = "cba"`, `s = "abcd"`
  
  Output: `"cbad"`
  
  Explanation: "a", "b", "c" appear in `order`, so the order of "a", "b", "c" should be "c", "b", and "a". Since "d" does not appear in `order`, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

- **Example 2:**

  Input: `order = "bcafg"`, `s = "abcd"`
  
  Output: `"bcad"`
  
  Explanation: The characters "b", "c", and "a" from `order` dictate the order for the characters in `s`. The character "d" in `s` does not appear in `order`, so its position is flexible. Following the order of appearance in `order`, "b", "c", "a" from `s` should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in `order`. The output "bcad" correctly follows this rule.

### Constraints

- `1 <= order.length <= 26`
- `1 <= s.length <= 200`
- `order` and `s` consist of lowercase English letters.
- All the characters of `order` are unique.

## Approach

To rearrange the string `s` according to the custom order specified by `order`, the following steps are proposed:

1. **Frequency Map:** Store the frequency of each character of the string `s` in a hashmap to easily track how many times each character occurs.

2. **Ordered Insertion:** Traverse the character array of `order`. For each character, add it to a result array according to its frequency in `s`. If a character appears more than once in `s`, ensure it is added to the result array the corresponding number of times.

3. **Remaining Characters:** After processing all characters in `order`, append the remaining characters from `s` that were not mentioned in `order` to the result array. These characters can be placed in any position as they are not specified in the custom order.

4. **Final Permutation:** Convert the result array to a string using the `join` method to obtain any valid permutation of `s` that follows the custom order specified by `order`.

This approach guarantees that the resulting permutation of `s` will adhere to the custom sorting order specified by `order`, ensuring the desired ordering of characters while accommodating characters in `s` not present in `order`.
