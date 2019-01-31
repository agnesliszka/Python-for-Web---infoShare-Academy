''' Function for finding maximum sum
 m - maximum index of elements of sigle list
 n - maximum index of number of lists in the list
 i - lists in list
 j - element in list'''

def maxPathSum(triangle, m, n): 
    # loop for bottom-up calculation
    for i in range(m-1, -1, -1): 
        for j in range(i+1): 
             ''' for each element, check both 
             elements just below the number 
             and below right to the number 
             add the maximum of them to it '''
            #checking if element below the number is greater than the element below right to the number 
            if (triangle[i+1][j] > triangle[i+1][j+1]):
                # adding element below the number to the number 
                triangle[i][j] += triangle[i+1][j] 
            else:
                # adding element below right to the number 
                triangle[i][j] += triangle[i+1][j+1] 
    # return the top element which stores the maximum sum    
    return triangle[0][0]

triangle = [[1, 0, 0, 0], 
           [2, 3, 0, 0], 
           [4, 5, 6, 0],
           [7, 8, 9, 10]]

m = len(triangle[0])-1
n = len(triangle[0])-1

print(maxPathSum(triangle, m, n)) 
