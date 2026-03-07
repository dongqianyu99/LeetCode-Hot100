from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        left, right = 0, len(height)-1
        
        while left != right:
            h = min(height[left], height[right])
            w = right - left
            best = max(best, h*w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return best
