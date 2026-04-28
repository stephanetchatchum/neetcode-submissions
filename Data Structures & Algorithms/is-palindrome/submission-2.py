class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(filter(str.isalnum, s)).lower()
        arr = result[::-1]
        if arr == result:
            return True
        else:
            return False