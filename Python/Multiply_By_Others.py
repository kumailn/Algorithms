#Question: Given a list of numbers, multiply each number by all other numbers except itself
#Solution: Traverse right then left while multiplying
#Difficulty: Hard

def multiplyRest(nums):
    #Create new list with 1s
    nums2 = [1 for i in nums]
    #Initialize the multiplier to 1
    multiplier = 1
    #Loop through to the right side
    for i in range(1, len(nums2)):
        #Let the multiplier be the product of itself the previous number
        multiplier *= nums[i - 1]
        #Set temp list[i] to the mutiplier
        nums2[i] = multiplier
    #Reset multiplier 
    multiplier = 1
    #Repeat process but go from right to left
    for i in range(len(nums2) - 1)[::-1]:
        multiplier *= nums[i + 1]
        nums2[i] *= multiplier
    return nums2

def main():
    print(multiplyRest([1, 2, 3, 4]))
    print(multiplyRest([4,3,2,1,2]))
main()
