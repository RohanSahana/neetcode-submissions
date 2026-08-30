class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}

        for i in s:
            a.update({i : a.get(i, 0) + 1})
        
        for j in t:
            a.update({j : a.get(j, 0) - 1})
            if(a.get(j) == 0):
                a.pop(j)
        if a == {}:
                return True
        for key, value in a.items():
            if value != 0:
                return False
            else:
                return True