class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        total = 0
        
        while L < R:
            if height[L] <= height[R]:
                if height[L] >= maxLeft:
                    maxLeft = height[L]
                else:
                    total += maxLeft - height[L]
                L += 1
            else:
                if height[R] >= maxRight:
                    maxRight = height[R]
                else:
                    total += maxRight - height[R]
                R -= 1
                
        return total