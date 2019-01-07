def countComponents(n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parents = list(range(n))
        def find(x, parents):
            return x if parents[x] == x else find(parents[x], parents)
        for x, y in edges:
            x, y = find(x, parents), find(y, parents)
            parents[x] = y
        count = 0
        for i in range(len(parents)): count += 1 if parents[i] == i else 0
        return count