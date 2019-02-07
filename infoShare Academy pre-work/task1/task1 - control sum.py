# Define variables
rows = []
total = []
control_sum = []

i = 0

# Read a file
file = open('rows.txt','r')

# Split file into lines 
result = [line.split() for line in file.readlines()]

# Get numbers from relative lines and save them as a list
for item in result:
    item = [int(k) for k in item]
    rows.append(item)   

# Get minimum, maximum, difference, total and control sum values
while True:
    maximum = max((rows[i]))
    minimum = min((rows[i]))
    difference = maximum - minimum
    total.append(difference)
    i += 1
    if i == len(rows):
        control_sum.append(sum(total))
        break

# Print control sum
print('Control sums of given file:', str(control_sum))
