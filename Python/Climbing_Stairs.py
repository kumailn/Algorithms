#Question: Given a number of stairs to climb, you can climb it by taking 2 steps or 1 at a time, return the number of possible combinations you could climb them.
#Solution: Each stair depends on the number of ways you can climb the previous + number of ways you can count the 2nd previous step
#Difficulty: Easy

def climbStairs(n):
        #Initialize a array to hold the number of combinations at each step, initialize step 0 and step 1 to 1 because they only have 1 combination (no steps and 1 step)
        prevSteps = [0] * (n + 1); prevSteps[0] = 1; prevSteps[1] = 1
        #For each step starting from step 2 up to the last one
        for i in range(2, n + 1):
            #The steps combination is equivalent to the combinations possible at step - 1 + step - 2
            prevSteps[i] = prevSteps[i - 2] + prevSteps[i - 1]
        #Return the combinations at the last step
        return prevSteps[-1]