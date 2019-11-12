def minMeetingRooms(intervals: List[List[int]]) -> int:
    intervals = sorted(intervals, key=lambda x: x[0])
    heap = []
    for i in intervals:
        # We need a new room, when the heap is empty or when an interval overlaps 
        # An interval overlaps (and thus requires a new room) if its start time is less 
        # than the end time of the first item in the min-heap. We push the end time of the item to the heap.
        # In other words, if this meeting starts before our earliest meeting ends, we need another room.
        if not heap or i[0] < heap[0]:
            heapq.heappush(heap, i[1])
        # If the item does not overlap, then we pop the first item in the heap (as it didn't overlap)
        # and push the current one
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, i[1])
    return len(heap)
