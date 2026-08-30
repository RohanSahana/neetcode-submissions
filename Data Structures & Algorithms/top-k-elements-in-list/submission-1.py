class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums).most_common(k)
        b = []
        for i in a:
            b.append(i[0])
        return b
        