function twoSum(nums, target){
    let countMap = {}, count = 0;
    for(let i = 0; i < nums.length; i++){
        if (countMap[target - nums[i]]) count++;
        countMap[i] = countMap[i] ? countMap[i] + 1: 1
    }
    return count
}

console.log(twoSum([1, 2, 3, 0, 2], 4))