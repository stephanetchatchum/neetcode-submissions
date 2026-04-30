class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRights = [0] * len(height)
        maxRights = [0] * len(height)
        for i in range(len(height)-2, -1, -1):
            maxRights[i] = max(maxRights[i+1], height[i+1])
        total = 0
        for i in range(len(height)):
            maxLeft = max(maxLeft, height[i-1]) if i > 0 else 0
            maxRight = maxRights[i]
            total += max(0, min(maxLeft, maxRight) - height[i])
        return total