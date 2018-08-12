function pivot(nums) {
    let total = nums.reduce((a, b) => a + b, 0);
    for(let i = 0; i < nums.length; i++){
        let left_sum = nums.slice(0, i).reduce((a, b) => a + b, 0);
        console.log(left_sum)
        if(left_sum === total - left_sum - nums[i]){
            return i;
        }
    }
}

console.log(pivot([1, 7, 3, 6, 5, 6]));