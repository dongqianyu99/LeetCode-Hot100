# 3. Longest Substring Without Repeating Characters (无重复字符的最长子串)

- Source: https://leetcode.cn/problems/longest-substring-without-repeating-characters/

## Problem
Given a string `s`, find the length of the longest substring without duplicate characters.

## Examples

Example 1:
- Input: `s = "abcabcbb"`
- Output: `3`
- Explanation: The answer is `"abc"`, with the length of `3`.

Example 2:
- Input: `s = "bbbbb"`
- Output: `1`
- Explanation: The answer is `"b"`, with the length of `1`.

Example 3:
- Input: `s = "pwwkew"`
- Output: `3`
- Explanation: The answer is `"wke"`, with the length of `3`.
- Note that the answer must be a substring, and `"pwke"` is a subsequence rather than a substring.

## Constraints
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.
