from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # always keep the max one in the window at first
                          # ==>  maintain the queue in decreasing order
                          # value: index
        ans = []

        for i, num in enumerate(nums):
            while q and q[0] <= i - k:  # remove out of date items
                q.popleft()

            while q and nums[q[-1]] <= num:  # maintain decreasing order
                q.pop()

            q.append(i)

            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans




            

