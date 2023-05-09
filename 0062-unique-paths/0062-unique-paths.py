class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        
#Loop through the rows of the grid, except for the last row.
        for i in range(m-1):
#Create a new list newRow with n elements that are all 1
            newRow = [1] * n
#Starting from the second last element of newRow and going backwards, compute the number of unique paths to get to that element by adding the number of unique paths to the element to the right and the element below it in the previous row.
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
#Set row to the newRow for the next iteration. 
            row = newRow
#Return the first element of the last row, which contains the total number of unique paths to get from the top left corner to the bottom right corner of the grid.
        return row[0]
#In summary, m is used to represent rows and n is used to represent columns in the code. The first two lines of code are not using both m and n to represent rows. The first line row = [1] * n uses n to create a list representing the first row of the grid, while the second line for i in range(m-1): uses m to iterate through the rows of the grid.