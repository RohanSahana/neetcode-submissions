from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = Counter(nums)
                
        return sorted(freq_count, key = lambda x:freq_count[x], reverse=True)[:k]