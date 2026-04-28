class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        arr = s[::-1]
        if arr == s:
            return True
        else:
            return False