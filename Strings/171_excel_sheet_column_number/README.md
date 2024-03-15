# Excel Sheet Column Number Converter

This utility is designed to convert Excel sheet column titles into their corresponding column numbers, following the standard Excel format. In Excel, columns are labeled with alphabetical characters where "A" represents the first column, "B" the second, continuing through "Z", after which the labels proceed to "AA", "AB", and so forth. This converter facilitates the process of determining the numerical value of any given column label, supporting a range of up to seven characters, which corresponds to Excel's column labeling system up to "FXSHRXW".

## Problem Statement

Given a string `columnTitle` that represents the column title as appears in an Excel sheet, the goal is to return its corresponding column number. This conversion adheres to the alphabetical labeling system used in Excel, where:

- "A" -> 1
- "B" -> 2
- "C" -> 3
- ...
- "Z" -> 26
- "AA" -> 27
- "AB" -> 28
- ...
  
### Examples

- **Example 1:**

  Input: `columnTitle = "A"`
  
  Output: `1`

- **Example 2:**

  Input: `columnTitle = "AB"`
  
  Output: `28`

- **Example 3:**

  Input: `columnTitle = "ZY"`
  
  Output: `701`

### Constraints

- The `columnTitle` length is between 1 and 7 characters.
- `columnTitle` consists only of uppercase English letters.
- `columnTitle` is within the range ["A", "FXSHRXW"].

## Approach

To convert a given Excel column title into its corresponding number, the following approach is adopted:

- Iterate through each character in the `columnTitle`, calculating the numerical value of each based on its position and alphabetical order.
- The numerical value is determined by calculating \((26^{(len(columnTitle) - i - 1)}) \times (ord(char) - ord('A') + 1)\), where \(i\) is the current character's index in the string.
- \(ord(char)\) represents the ASCII value of the character, and subtracting the ASCII value of 'A' and adding 1 aligns 'A' with 1, 'B' with 2, and so forth, following Excel's column labeling convention.
- Accumulate these values in a variable, `count`, which is returned at the end of the iteration.

This method effectively translates the alphabetical column labels into their numerical counterparts, aiding in various applications that require manipulation or interpretation of Excel data programmatically.
