from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            # Count occurrences of each lowercase letter
            count = [0] * 26

            for ch in s:
                index = ord(ch) - ord('a')
                count[index] += 1

            # Lists cannot be dictionary keys, so convert to a tuple
            key = tuple(count)
            groups[key].append(s)

        return list(groups.values())