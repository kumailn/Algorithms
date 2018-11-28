def ts(nums, target):
    d = {}
    t = 0
    for i, v in enumerate(nums):
        d[target - v] = d.get(target - v, 0) +  1
        if v in d: t += d[v]
    return t