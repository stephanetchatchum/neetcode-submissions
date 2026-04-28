class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_s = sorted(s)
        arr_t = sorted(t)
        if arr_s == arr_t:
            return True
        else:
            return False

        