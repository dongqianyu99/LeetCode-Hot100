# 11. Container With Most Water (盛最多水的容器)

- Source: https://leetcode.cn/problems/container-with-most-water/

## Problem
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Note: You may not slant the container.

## Examples

Example 1:
![Example 1](./image.png)
- Input: `height = [1,8,6,2,5,4,8,3,7]`
- Output: `49`
- Explanation: The maximum area is obtained between index `1` and index `8` (0-based), giving width `7` and height `7`.

Example 2:
- Input: `height = [1,1]`
- Output: `1`

## Constraints
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`
