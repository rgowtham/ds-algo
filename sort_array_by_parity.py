#!/usr/bin/env python3

# Solution to https://leetcode.com/problems/sort-array-by-parity/description/

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_array = []
        even_array = []

        # Identify if a number is odd and then add it to new_nums
        for num in nums:
            if num % 2:
                odd_array.append(num)
            else:
                even_array.append(num)
        even_array.extend(odd_array)
        return even_array

    def sortArrayByParityTwoPointer(self, nums: List[int]) -> List[int]:
        # Uses two pointer approach
        # This approach changes the order in which elements appear
        # But still it solves the problem by keeping all even numbers in front
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] % 2:
                if not nums[r] % 2:
                    # this means element at left index is odd and element at right index is even
                    # swap these two elements
                    nums[l], nums[r] = nums[r], nums[l]
                else:
                    # this means element at left index is odd and element at right index is also odd
                    # Reduce the right index and check the previous element
                    r -= 1
            else:
                # this means element at left index is even
                # check the next element
                l += 1
        return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortArrayByParity([1, 2, 3, 4]))
    print(sol.sortArrayByParity([3, 1, 2, 4]))
    print(sol.sortArrayByParityTwoPointer([1, 2, 3, 4]))
    print(sol.sortArrayByParityTwoPointer([3, 1, 2, 4]))
