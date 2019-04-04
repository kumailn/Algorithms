#Question: Given a image (2D list), a x and y coordinate of a pixel, and a new color, flood fill all neigbboring pixels with the same color to the new color
#Solution: Run a DFS on the input pixel
#Difficulty: Easy

from typing import List
def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        #If the pixel at the given coordinates is already the new color, return the image
        if image[sr][sc] == newColor: return image

        #Define a recursive DFS to help us flood fill
        def dfs(i, j, newColor, oldColor, image):

                #If the coordinates passed are not out of bounds and the color is the same as the previous one
                if i >= 0 and j >= 0 and i < len(image) and j < len(image[0]) and image[i][j] == oldColor:

                        #Set the pixel at the given coordinates to the new color
                        image[i][j] = newColor

                        #Recursively repeat on the pixel left, right, above and below
                        dfs(i + 1, j, newColor, oldColor, image)
                        dfs(i - 1, j, newColor, oldColor, image)
                        dfs(i, j + 1, newColor, oldColor, image)
                        dfs(i, j - 1, newColor, oldColor, image)

        #Call our DFS function on the original inputs
        dfs(sr, sc, newColor, image[sr][sc], image)
        return image

def main():
    print(floodFill([[0,0,0],[0,1,1]], 0, 0, 6))

main()