import java.util.Arrays

fun twoSum(nums: IntArray, target: Int): IntArray {
    val lookingFor = HashMap<Int, Int>();
    for (i in nums.indices) {
        if (lookingFor.containsKey(nums[i])) return intArrayOf(lookingFor.get(nums[i])!!, i);
        lookingFor.put(target - nums[i], i);
    }

    return intArrayOf(0, 0);
}

fun main(args: Array<String>) {
    println(Arrays.toString(twoSum(intArrayOf(2, 11, 15, 7), 9)));
}