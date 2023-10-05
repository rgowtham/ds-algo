#!/usr/bin/env python3

# Solution to leetcode https://leetcode.com/problems/monotonic-array/description/


from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        curr = nums[0]
        final_list = [True]

        for i in range(1, len(nums)):
            final_list.append(nums[i] >= curr)
            curr = nums[i]
        return sum(final_list) == 0 or sum(final_list) == len(nums) - 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.isMonotonic([1, 4, 5, 5]))
    print(sol.isMonotonic([5, 5, 2, 1, 0]))
