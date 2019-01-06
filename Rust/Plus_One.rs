fn plus_one(mut nums: Vec<i32>) -> std::vec::Vec<i32> {
    for i in (0..nums.len()).rev() {
        if nums[i] < 9 {
            nums[i] += 1;
            return nums;
        }
        nums[i] = 0;
    }
    let mut newnum = vec![1];
    newnum.extend(nums);
    return newnum;
}

fn main(){
    println!("{:?}",(plus_one([1, 3, 9].to_vec())));
}