# Question: Given two strings find the minimum number of letters you need to delete from each to get the same strings
# Solution: Implement a top down or bottom up DP
# Difficulty: Medium

def minDistance(w1: str, w2: str, store={}) -> int:
    # Our base cases are, if both strings are the same (this includes when they're both null) return 0 because nothing needs to be 
    # deleted, if only one of them is non-null, then return the length of it since everything needs to be deleted
    if w1 == w2: return 0
    if not w1 or not w2: return len(w1 or w2)

    # If we have this pair of words in our store then just return the deletion distance from that
    if (w1,w2) in store: return store[(w1,w2)]
    
    # If both words start with the same letter, nothing needs to be deleted, so just rerun the function
    # on the substrings with the first character removed, otherwise try deleting the first letter from each word 
    # and seeing which one results in the shorter deletion distance
    if w1[0] == w2[0]: 
        edit = self.minDistance(w1[1:], w2[1:], store)
    else:
        edit = 1 + min(self.minDistance(w1[1:], w2, store), self.minDistance(w1, w2[1:], store))

    # Once the computation is completed, store
    store[(w1,w2)] = edit
    return edit