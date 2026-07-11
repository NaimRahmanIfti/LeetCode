class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        best = 0
        h = {}
        max_freq = 0
        
        for i in range(len(s)):
            
            h[s[i]] = h.get(s[i], 0) + 1
            max_freq= max(h.values())
            

            if (i - left + 1) - max_freq > k:
                h[s[left]] -= 1
                left += 1
            
            best = max(best, i - left + 1)
        return best

