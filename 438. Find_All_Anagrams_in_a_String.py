class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        s_count = {}
        p_count = {}
        res = []
        left = 0

        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1

            if i - left +1 > len(p):
                s_count[s[left]] -= 1
                if s_count[s[left]] == 0:
                    del s_count[s[left]]
                left += 1 

            if i - left + 1 == len(p): 
                if p_count == s_count:
                    res.append(left)
                    
        return res
