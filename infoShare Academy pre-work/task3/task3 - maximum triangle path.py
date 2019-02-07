''' Function for finding maximum sum
 m - maximum index of elements of sigle list
 n - maximum index of number of lists in the list
 i - lists in list
 j - element in list'''

# Define variables
triangle_basic = []
triangle_final = []

# Create a function to get the maximum path sum
def maxPathSum(triangle, m, n): 
    ''' for each element, check both 
             elements just below the number 
             and below right to the number 
             add the maximum of them to it '''
    # Loop for bottom-up calculation
    for i in range(m-1, -1, -1): 
        for j in range(i+1): 
            if (triangle[i+1][j] > triangle[i+1][j+1]):  # Check if element below the number is greater than the element below right to the number 
                triangle[i][j] += triangle[i+1][j] # Add element below the number to the number 
            else:
                triangle[i][j] += triangle[i+1][j+1] # Add element below right to the number 
    # Return the top element which stores the maximum sum    
    return triangle[0][0]

# Read a file
file = open('task3_triangle_big.txt','r')

# Split file into lines 
result = [line.split() for line in file.readlines()]

# Get numbers from relative lines and save them as a list
for element in result:
    element = [int(k) for k in element]
    triangle_basic.append(element)

triangle_length = len(triangle_basic[-1])

for short_list in triangle_basic:
    length = len(short_list)
    small_list_converted = short_list + [0] * (triangle_length - length)
    triangle_final.append(small_list_converted)    

m = len(triangle_final[0])-1
n = len(triangle_final[0])-1

# Get the maximum path sum
print(maxPathSum(triangle_final, m, n)) 
