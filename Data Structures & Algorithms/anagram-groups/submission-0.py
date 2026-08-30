class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for string in strs:
            fp = self.createFingerprint(string)
            if fp in group:
                group[fp].append(string)
            else:
                group[fp] = [string]
        return list(group.values())

    def createFingerprint(self, string: str) -> tuple:
        freq = [0] * 26
        for char in string:
            freq[ord(char) - ord('a')] += 1

        return tuple(freq)