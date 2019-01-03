def kpairs(nums, k):
    lookingFor = {}
    pairs = 0
    for i, v in enumerate(nums):
        if v + k in lookingFor: 
            pairs += lookingFor[v + k]
        if v - k in lookingFor:
            pairs += lookingFor[v - k]
        if v in lookingFor:
            lookingFor[v] += 1
        else: 
            lookingFor[v] = 1
    return pairs

def kk(nums, k):
    lookingFor = {}; pairs = 0
    for i, v in enumerate(nums):
        lookingFor[v] = lookingFor.get(v, 0) + 1
    for i in lookingFor:
        if (i + k) in lookingFor: pairs += 1; print("pair ", i+k, i)
    print(lookingFor, 'look')
    return pairs

def main():
    nums = [1, 3, 6, 8, 5]
    #print(kk(nums, 2))

    print(kk([8, 12, 16, 4, 0, 0, 20], 4))

main()