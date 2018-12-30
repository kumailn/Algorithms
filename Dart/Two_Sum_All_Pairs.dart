num twoAll(List<num> nums, num target) {
  Map targetCounts = Map();
  num pairCount = 0;
  for(int i=0; i<nums.length; i++) {
    if (targetCounts.containsKey(nums[i])) pairCount += targetCounts[nums[i]];
    if (targetCounts.containsKey(target - nums[i])) targetCounts[target - nums[i]]++;
    else targetCounts[target - nums[i]] = 1;
  }
  return pairCount;
}

void main(List<String> args) {
    var nums = [2, 3, 1, 3, 2, 1];
    var nums2 = [1, 1, 1, 1, 1, 2, 0, 3, 0];
    print(twoAll(nums, 5));
    print(twoAll(nums2, 3));
}