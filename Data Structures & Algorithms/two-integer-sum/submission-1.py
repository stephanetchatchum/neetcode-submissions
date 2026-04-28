class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            second = target - nums[i]
            if second in nums:
                j = nums.index(second)
                if j != i:
                    return [min(i, j), max(i, j)]