import 'dart:math';

num maxSubArray(List<num> nums) {
  num globalMax = 0, localMax = 0;
  for (int i = 0; i < nums.length; ++i) {
    localMax = max(nums[i], localMax + nums[i]);
    if(localMax > globalMax) globalMax = localMax;
  }
  return globalMax; 
}

void main () {
  print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]));
}