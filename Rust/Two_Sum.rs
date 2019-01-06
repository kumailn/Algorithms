fn two_sum(nums: Vec<i32>, target: i32) -> i32 {
        use std::collections::HashMap;
        let mut counts: HashMap<i32, i32> = HashMap::new();
        for i in 0..nums.len() {
            counts.insert(nums[i], i as i32);
        }
        let mut count = 0;
        for i in 0..nums.len() {
            match counts.get(&(target - nums[i])) {
                Some(index) if i as i32 != *index => count += 1,
                None => (),
                _ => ()
            }
        }
    return count;
}

fn main(){
    println!("{:?}",(two_sum([1, 3, 9, 2, 5, -2].to_vec(), 4)));
}