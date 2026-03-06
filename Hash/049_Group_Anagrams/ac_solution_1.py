from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  # defaultdict(list) is a dictionary that will return a list if the key is not found

        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)

        return list(groups.values())