# Get data from website
import requests

url = 'https://www.lotto.pl'
response = requests.get(url)
content = response.text

# Save content of website into content_file
with open('content_file.txt', 'w') as content_file:
    content_file.write(content)

# Read content_file and save it as string
file = open('content_file.txt','r')
file_content = file.readlines()
file_content_string = ''.join(file_content)

# Create empty list
lotto_list =[]

# Get number of lottery types
text_to_find = 'classCenter'
n = file_content_string.count(text_to_find)

# Get starting position of searched element
lotto_starting_pos = file_content_string.find('resultLotto')

for i in range(n):

    # Get lotto lottery type
    results_item_pos1 = file_content_string.find('<div class="resultsItem ', lotto_starting_pos) + len('<div class="resultsItem ')
    results_item_pos2 = file_content_string.find('">', results_item_pos1)
    lotto_result_item = file_content_string[results_item_pos1:results_item_pos2]
    lotto_list.append(lotto_result_item)
    lotto_start_pos = results_item_pos2

    # Get lottery date
    date_pos1 = file_content_string.find('wyniki z dnia <strong>', results_item_pos2) + len('wyniki z dnia <strong>')
    date_pos2 = file_content_string.find('</strong>', date_pos1)
    lotto_date = file_content_string[date_pos1:date_pos2]
    lotto_list.append(lotto_date)
    results_item_pos2 = date_pos2

    # Get winning numbers
    content_to_find_numbers_pos1 = file_content_string.find('<div class="resultsItem ', date_pos2)
    content_to_find_numbers_pos2 = file_content_string.find('"resultsItem', content_to_find_numbers_pos1)
    content_to_find_numbers = file_content_string[content_to_find_numbers_pos1:content_to_find_numbers_pos2]

    result_number_pos = file_content_string.find('resultnumber', lotto_start_pos)

    m = content_to_find_numbers.count('<span>')

    for j in range(6):
        span_pos1 = file_content_string.find('span', result_number_pos) + len('span>')
        span_pos2 = file_content_string.find('</span', span_pos1)

        lotto_number=file_content_string[span_pos1:span_pos2]
        result_number_pos = span_pos2 + len('span')
        lotto_list.append(lotto_number)
        lotto_numbers_string = ' '.join(lotto_list)
        result_number_pos = span_pos2 + len('span')

# Print lotto results
print(lotto_numbers_string)

# Save data to output_file
with open('output_file.txt', 'w') as output_file:
    output_file.write(lotto_numbers_string)

output_file.close()

content_file.close()