function plusOne(nums) {
    for(let i = nums.length; i >= 0; i--){
        if (nums[i] < 9) {
            nums[i]++;
            return nums;
        }
        nums[i] = 0;
    }
    return [1].concat(nums);
}

function main() {
    console.log(plusOne([1, 2, 3]));
    console.log(plusOne([9, 9, 9]));
    console.log(plusOne([0]));
}

main();