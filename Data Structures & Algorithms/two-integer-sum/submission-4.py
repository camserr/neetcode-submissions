class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in diffs:
                return [diffs[diff], n]
            else:
                diffs[nums[n]] = n