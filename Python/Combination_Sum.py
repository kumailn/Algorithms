def combinationSum(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #Firstly we sort the candidates so we can keep track of our progression
        candidates = sorted(candidates)
        
        def backTrack(left, current, results):
            #Our base case is when nothing is left, in which case we add the current solution to the results
            if not left:
                results += [current]
                return
            
            #Now we address all candidates 
            for number in candidates:
                
                #If the number is greater than whats left over, we can break this loop, and in turn the recursio
                if number > left: break
                
                #This (along with the sorted candidates) ensures uniqueness because if the number we're at is less than the last number in the curent solution, we can skip it over
                if current and number < current[-1]: continue 
                
                #In the case that this number is smaller than whats left over, we continue backtracking
                backTrack(left - number, current + [number], results)
            
            #We can return results in the higest function call
            return results
        
        return backTrack(target, [], [])