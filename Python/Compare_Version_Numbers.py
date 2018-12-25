#Question: Given two version numbers determine which one is greater
#Solution: Split by the "."s and loop through both and compare
#Difficulty: Easy

def compareVersion(version1, version2):
        #Split each version number by the . (For example: 3.14 -> [3, 14])
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        #Keep a difference index, we'll use it to compare indexes in out version lists
        i = 0
        #As long as i is less than the length of both versions
        while i < len(v1) and i < len(v2):
            #If version1[i] is greater than or less than version2[i] return 1 or -1 respectively 
            if int(v1[i]) > int(v2[i]): return 1
            elif int(v1[i]) < int(v2[i]): return -1
            i += 1
        #If i is less than the len of version1 or version 2 return 1 (or -1) if the last item in version1/2 is 0, otherwise return 0
        if i < len(v1): return 1 if int(v1[-1]) != 0 else 0
        if i < len(v2): return -1 if int(v2[-1]) != 0 else 0
        return 0
        