class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_arr = set()
        for num in nums:
            if num in new_arr:
                return True
            else:
                new_arr.add(num)
        return False
        