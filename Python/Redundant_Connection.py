def findRedundantConnection(edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parents = list(range(len(edges) + 1))
        def find(x, parents):
            return x if parents[x] == x else find(parents[x], parents)
        found = []
        for x, y in edges:
            x1, y1 = find(x, parents), find(y, parents)
            if x1 == y1: found = [x, y]
            parents[x1] = y1
        return found