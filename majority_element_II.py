#!/usr/bin/env python3

# Solution to https://leetcode.com/problems/majority-element-ii/

from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        counts = Counter(nums)
        return [x for x in counts.keys() if counts[x] > threshold]


if __name__ == "__main__":
    nums = [3, 2, 3]
    print(Solution().majorityElement(nums))
