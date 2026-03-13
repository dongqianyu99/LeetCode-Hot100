from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        prefix_sum = 0
        ans = 0

        for num in nums:
            prefix_sum += num
            ans += count.get(prefix_sum - k, 0)
            count[prefix_sum] = count.get(prefix_sum, 0) + 1

        return ans
