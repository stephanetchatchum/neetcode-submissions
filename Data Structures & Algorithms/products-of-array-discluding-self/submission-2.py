class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        #sol1
        # for i in range(len(nums)):
        #     ans = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             ans = ans * nums[j]
        #     output.append(ans)
        # return output
        #sol2
        prefix =1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] *= postfix
            postfix*= nums[i]
        return output

