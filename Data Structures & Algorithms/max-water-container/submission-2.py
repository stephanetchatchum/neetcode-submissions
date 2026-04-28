class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        maxWater = 0
        while L != R:
            w = R - L
            h = min(heights[L], heights[R])
            water = h*w
            maxWater = max(maxWater, water)
            if h == heights[L]:
                L += 1
            else:
                R -= 1
        return maxWater