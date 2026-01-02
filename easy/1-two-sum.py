"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List, Dict


class Solution:
    # basic naive version, time complexity is O(n2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l: int = len(nums)
        for i in range(l):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # try to improve, incorrect
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l: int = len(nums)
        for i in range(l):
            if nums[i] > target:
                continue  # incorrect, can have negative numbers
            for j in range(i + 1, l):
                if nums[j] > target:
                    continue  # incorrect, can have negative numbers
                if nums[i] + nums[j] == target:
                    return [i, j]

    # sample code
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        i = 0
        while i < len(nums):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    break
                else:
                    continue
            i += 1

    # attempt 1 after seeing fastest solution. Much better
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # idea is instead of trying one by one, we do look up of target
        l: int = len(nums)
        for i in range(l):
            first_num: int = nums[i]
            second_num: int = target - first_num
            if second_num in nums[i + 1:]:
                return [i, i + 1 + nums[i + 1:].index(second_num)]

    # attemp 2, same as fastest solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # idea is instead of trying one by one, we do look up of target
        # also keep track of the numbers we have already seen
        l: int = len(nums)
        history: Dict[int, int] = {}
        for i in range(l):
            first_num: int = nums[i]
            second_num: int = target - first_num
            if second_num in history:
                return [i, history[second_num]]
            # record the index
            history[first_num] = i
