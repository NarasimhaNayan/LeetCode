# Valid Parentheses Checker

This documentation explains the implementation of a function to determine if a string containing just the characters '(', ')', '{', '}', '[' and ']', known as parentheses, is valid. A string is considered valid if it meets the following criteria:

1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples

- **Example 1:**

  Input: `s = "()"`

  Output: `true`

- **Example 2:**

  Input: `s = "()[]{}"`

  Output: `true`

- **Example 3:**

  Input: `s = "(]"`

  Output: `false`

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

## Approach

To validate the parentheses in the given string, the approach involves using a stack to keep track of the opening brackets encountered as we iterate through the string. Here is a step-by-step breakdown:

- **Initialization**: Start with an empty stack.
- **Iteration**: For each character in the string, perform the following:
  - If the character is an opening bracket ('(', '{', or '['), push it onto the stack.
  - If the character is a closing bracket (')', '}', or ']'), check if the stack is empty or the top of the stack is not the corresponding opening bracket. If either condition is true, the string is invalid, and we return `false`.
  - If the stack's top is the corresponding opening bracket, pop the top of the stack.
- **Validation**: After processing all characters, if the stack is empty, all brackets were properly closed and nested, and the string is valid, returning `true`. Otherwise, return `false`.
