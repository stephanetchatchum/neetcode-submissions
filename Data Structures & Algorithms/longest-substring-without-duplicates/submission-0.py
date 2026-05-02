class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen, L, R= 0, 0, 0
        arr = []
        s_arr = list(s)
        for i in range(len(s_arr)):
            if s_arr[i] in arr:
                while s_arr[L] != s_arr[i]:
                    arr.remove(s_arr[L])
                    L +=1
                    
                L +=1
                arr.remove(s_arr[i])
                arr.append(s_arr[i]) 
            else:
                arr.append(s_arr[i])
                R +=1
            maxLen = max(maxLen, len(arr))
            
        return maxLen