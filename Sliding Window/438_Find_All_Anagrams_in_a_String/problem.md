# 438. Find All Anagrams in a String (找到字符串中所有字母异位词)

- Source: https://leetcode.cn/problems/find-all-anagrams-in-a-string/

## Problem
Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`.
You may return the answer in any order.

## Examples

Example 1:
- Input: `s = "cbaebabacd"`, `p = "abc"`
- Output: `[0,6]`
- Explanation:
The substring with start index `0` is `"cba"`, which is an anagram of `"abc"`.
The substring with start index `6` is `"bac"`, which is an anagram of `"abc"`.

Example 2:
- Input: `s = "abab"`, `p = "ab"`
- Output: `[0,1,2]`
- Explanation:
The substrings with start indices `0`, `1`, and `2` are `"ab"`, `"ba"`, and `"ab"`.

## Constraints
- `1 <= s.length, p.length <= 3 * 10^4`
- `s` and `p` consist of lowercase English letters.
