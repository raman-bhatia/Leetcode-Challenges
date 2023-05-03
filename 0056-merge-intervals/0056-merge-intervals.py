class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        
        intervals.sort(key = lambda i:i[0])
#edge case if there is only one interval so output is that one interval
        output = [intervals[0]]
        
        for start, end in intervals[1: ]:
            last_value = output[-1][1]
            
            if start <= last_value:
                output[-1][1] = max(last_value, end)
            
            else:
                output.append([start, end])
        return output