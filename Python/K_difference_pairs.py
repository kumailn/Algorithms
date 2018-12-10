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

def main():
    nums = [1, 2, 2, 3, 2, 1]
    print(kpairs(nums, 2))

main()