#Question: Given two version numbers determine which one is greater
#Solution: Split by the "."s and loop through both and compare
#Difficulty: Easy

def compareVersion(version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        i = 0
        while i < len(v1) and i < len(v2):
            if int(v1[i]) > int(v2[i]): return 1
            elif int(v1[i]) < int(v2[i]): return -1
            i += 1
        if i < len(v1): return 1 if int(v1[-1]) != 0 else 0
        if i < len(v2): return -1 if int(v2[-1]) != 0 else 0
        return 0
        