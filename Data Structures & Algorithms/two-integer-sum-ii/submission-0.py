class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            second = target - numbers[i]
            if second in numbers:
                j = numbers.index(second)
                if j != i:
                    return [min(i+1, j+1), max(i+1, j+1)]
        