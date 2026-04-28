class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        waters = []
        while L != R:
            w = R - L
            h = min(heights[L], heights[R])
            water = h*w
            waters.append(water)
            if h == heights[L]:
                L += 1
            else:
                R -= 1
        return max(waters)