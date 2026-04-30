class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRight = 0
        water = 0
        total = 0
        for i in range(len(height)):
            maxLeft = max(height[:i]) if i > 0 else 0
            maxRight = max(height[i:])
            water = max(0, min(maxLeft, maxRight) - height[i])
            total += water
        return total