//Question: Move 0s to the end of a list
//Difficulty: Easy
//Solution: Keep an index to place non zeros at and keep incrementing it each time you encounter a non zero
//Space Complexity: O(1)
//Time Complexity: O(n)

var moveZeroes = function(nums) {
    let notZeroIndex = 0;
    nums.forEach((val, i) => {
        //If the element is not 0, swap it with the item at 'nonZeroIndex' and increment 'NnonZeroIndex'
        if (val != 0) {
            nums[i] = nums[notZeroIndex];
            nums[notZeroIndex] = val;
            notZeroIndex++;
        }
    })
};


let main = () => {
    let test = [1, 4, 0, 4, 3, 0, 6, 0, 9];
    moveZeroes(test);
    console.log(test);
};

main();