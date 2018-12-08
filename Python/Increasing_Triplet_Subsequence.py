#Question: Given an array of numbers, determine if a triplet that is increasing exists (doesn't need to be continious)
#Solution: Keep track of first, second and third largest numbers
#Difficulty: Medium
#Complexity: O(N)

def increasingTriplet(nums):
    #Keep track of the first largest, and second largest numbers, where second <= first
    first = second = float('inf')
    for i, v in enumerate(nums):
        #If the current number is less than or equal to the first largest number, set first to it
        if v <= first: first = v
        #Otherwise if its not less than the first largest number, but less than the second largest, set second to that
        elif v <= second: second = v
        else: return True
    return False 
