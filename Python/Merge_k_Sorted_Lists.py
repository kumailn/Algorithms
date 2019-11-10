# Question (#23): 
# Solution: Use a heap! It'll track all heads of the various linked lists, and at any given
#           point you can poll for the smallest head and add that to your output linked list

def mergeKLists(lists: List[ListNode]) -> ListNode:
    # Create a heap with all heads of our linkedlists, note the item we're storing in the heap  
    # is a tuple of 3 items, the value of the head (this will help the heap store the smallest value), the index
    # of the head (this will help the heap distinuish heads if their values are the same in the heap), and the actual 
    # node, this let's us access the rest of the linked list.
    heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
    heapq.heapify(heap)

    origin = head = ListNode(None)

    while heap:
        # Pop off the smallest item in the heap (the node with the lowest value)
        v, i, node = heapq.heappop(heap)

        # If the node we just popped off has a next, then we need to put that back into
        # our heap, since it's a value we'll need later on
        if node.next: 
            heapq.heappush(heap, (node.next.val, i, node.next))

        # Append the node we popped off to our head and move on to the next
        head.next = node
        head = head.next

    return origin.next
