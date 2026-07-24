class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        u = sorted(s)
        v = sorted(t)
        if u == v:
            return True
        return False