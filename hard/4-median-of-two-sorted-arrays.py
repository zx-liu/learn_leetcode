"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
from typing import List


class Solution:

    # sneaky version
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array: List[int] = sorted(nums1 + nums2)
        merged_array_len = len(merged_array)

        if merged_array_len % 2 == 0:
            idx_1: int = int(merged_array_len / 2 - 1)
            idx_2: int = int(merged_array_len / 2)
            return (merged_array[idx_1] + merged_array[idx_2]) / 2
        else:
            idx: int = int(((merged_array_len + 1) / 2) - 1)
            return merged_array[idx]
