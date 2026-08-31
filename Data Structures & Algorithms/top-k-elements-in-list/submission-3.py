class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d.update({i:1})
            else:
                d.update({i:d.get(i)+1})
                
        return [number for number, count in sorted(d.items(), key= lambda x : x[1], reverse=True)[:k]] 