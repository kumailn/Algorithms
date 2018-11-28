def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(map(lambda x: [0 if i == 1 else 1 for i in x], list(map(lambda x: x[::-1], A))))