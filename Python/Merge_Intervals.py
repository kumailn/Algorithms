#Question: Given a list of time intervals merge overpapping ones together, (ex. [1,3],[2,6] become [1, 6])
#Solution: Sort by start time then traverse intervals, setting each interval to be the [start first, max(end first, end second)] and deleteing the ocurrent one in-place
#Difficulty: Medium

def merge(intervals):
        """
        :type intervals: List[List]
        :rtype: List[List]
        """
        i = 0
        intervals = sorted(intervals, key=lambda x: x[0])
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]: 
                intervals[i] = [intervals[i][0], max(intervals[i+1][1], intervals[i][1])]
                del intervals[i + 1]
            else: i += 1
        return intervals