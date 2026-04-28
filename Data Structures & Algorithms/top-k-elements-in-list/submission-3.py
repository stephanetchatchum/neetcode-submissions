class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        output = []
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1

        sorted_array = sorted(dic, key = dic.get, reverse=True)
        return sorted_array[:k]