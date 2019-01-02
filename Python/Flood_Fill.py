def floodFill(image, sr, sc, newColor):
        if image[sr][sc] == newColor: return image
        def dfs(i, j, newColor, oldColor, image):
            if i >= 0 and j >= 0 and i < len(image) and j < len(image[0]) and image[i][j] == oldColor:
                image[i][j] = newColor
                dfs(i + 1, j, newColor, oldColor, image)
                dfs(i - 1, j, newColor, oldColor, image)
                dfs(i, j + 1, newColor, oldColor, image)
                dfs(i, j - 1, newColor, oldColor, image)
        dfs(sr, sc, newColor, image[sr][sc], image)
        return image

def main():
    print(floodFill([[0,0,0],[0,1,1]], 1, 1, 1))

main()hhh