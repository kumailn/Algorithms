# Question: Give
# Solution: Track the offset of the inner level of the spiral we're at, keep track of the directions 
# Difficulty: Medium

def minDistance(self, word1: str, word2: str, store={}) -> int:
    # We have 3 base cases, if both words are the same (including null) return 0 as nothing needs to be changed,
    # if of the words is null, return the length of the other one. Lastly, if we've seen this combination of words before, 
    # return the distance we already computed
    if word1 == word2: return 0
    if not word1 or not word2: return len(word1 or word2)
    if (word1, word2) in store: return store[(word1, word2)]

    # If both words start with the same letter, we dont need to edit, so recursively call the function on the substrings without the first character
    if word1[0] == word2[0]: return self.minDistance(word1[1:], word2[1:])

    # The trick here is to realize that even though we can insert any letter, it only makes sense to insert a characher present in the other
    # word, we could go ahead and try inserting all characters from the other word but we can also realize that insertion is actually the same as deletion.
    # If we have two words fog and frog, we clearly need to insert an r (eventually), firstly we delete both f's, we then get the strings og and rog, now we could insert 
    # r infront of og, or we could simply remove the r in rog and pretend like we actually inserted the r in og and deleted both letters since they became the same!

    # We also need to realize that replacing letters is actually the same as deleting them both, or both of them being the same, so we do the same thing as
    # we did in the case where the words started with the same letters, for example to change cat to bat, we would need to replace the c to a b, but this is the same thing
    # as removing the c and the b (adding 1) and then comparing the strings at and at.
    insert = 1 + self.minDistance(word1, word2[1:])
    delete = 1 + self.minDistance(word1[1:], word2)
    replace = 1 + self.minDistance(word1[1:], word2[1:])
    
    store[(word1, word2)] = min(insert, delete, replace)

    return min(insert, delete, replace)