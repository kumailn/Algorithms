def letterCombinations(digits):
        res = []
        if not digits: return res
        kp = {1: None, 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        def r(ds, s):
            if not ds: res.append(s)
            else: 
                for i in kp[int(ds[0])]:
                    r(ds[1:], s + i)
        r(digits, "")
        return res