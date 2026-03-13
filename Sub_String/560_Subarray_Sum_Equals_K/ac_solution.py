from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        prefix[i] = nums[0] + nums[1] + ... + nums[i]
        prefix[r] - prefix[l - 1] = k  ==>  prefix[l - 1] = prefix[r] - k

        Calculate prefix[r] while counting prefix[r] - k.
        """
        count = {0: 1}  # key: prefix sum, value: count
                        # init: prefix[l - 1] = 0 while l = 0
        prefix_sum = 0
        ans = 0

        for num in nums:
            prefix_sum += num
            ans += count.get(prefix_sum - k, 0)
            count[prefix_sum] = count.get(prefix_sum, 0) + 1

        return ans
