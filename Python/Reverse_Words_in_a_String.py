#Example
# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

def reverseWords(self, strin):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def rev(start, end, stringList):
            while start < end:
                stringList[start], stringList[end] = stringList[end], stringList[start]
                start += 1
                end -= 1
            return stringList
        strin = strin[::-1]
        i = 0
        while i < len(strin):
            end = i
            if strin[i] != " ": 
                while end + 1 < len(strin) and strin[end] != " ": 
                    if strin[end + 1] == " ": break
                    end += 1
            strin[:] = rev(i, end, strin)
            i = end + 1
        
    
#Crazy 4 line solution

def rev(start, end, strin):
    while start < end: strlin[start], strlin[end], start, end = strlin[end], strlin[start], start + 1, end - 1
    strin[:], start = strin[::-1], 0
    for i in range(len(strin)): a, start = rev(start, i - 1 if strin[i] == " " else i if len(strin) - 1 == i else start, strin), i + 1 if strin[i] == " " else start

        