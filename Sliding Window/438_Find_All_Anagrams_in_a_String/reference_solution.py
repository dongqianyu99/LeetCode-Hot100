from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []

        target = [0] * 26
        window = [0] * 26

        for ch in p:
            target[ord(ch) - ord("a")] += 1

        for i in range(m):
            window[ord(s[i]) - ord("a")] += 1

        ans = []
        if window == target:
            ans.append(0)

        for right in range(m, n):
            window[ord(s[right]) - ord("a")] += 1
            left = right - m
            window[ord(s[left]) - ord("a")] -= 1

            if window == target:
                ans.append(left + 1)

        return ans
