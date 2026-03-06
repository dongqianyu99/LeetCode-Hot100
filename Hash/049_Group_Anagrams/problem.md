# 49. Group Anagrams (字母异位词分组)

- Source: https://leetcode.cn/problems/group-anagrams/

## Problem
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all original letters exactly once.

## Examples

Example 1:
- Input: `strs = ["eat","tea","tan","ate","nat","bat"]`
- Output: `[["bat"],["nat","tan"],["ate","eat","tea"]]`

Example 2:
- Input: `strs = [""]`
- Output: `[[""]]`

Example 3:
- Input: `strs = ["a"]`
- Output: `[["a"]]`

## Constraints
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.
