class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        from bisect import bisect_right, bisect_left
        
        starts = sorted(s for s, e in flowers)
        ends = sorted(e for s, e in flowers)
        
        result = []
        for p in people:
            # Count flowers that started <= p
            started = bisect_right(starts, p)
            # Count flowers that ended < p
            ended = bisect_left(ends, p)
            result.append(started - ended)
        
        return result