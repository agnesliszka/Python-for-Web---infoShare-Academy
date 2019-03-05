# Get data from website
import requests

url = 'https://www.lotto.pl'
response = requests.get(url)
content = response.text

# Save content of website into content_file
with open('content_file.txt', 'w') as content_file:
    content_file.write(content)

# Read content_file
file = open('content_file.txt','r')
file_content = file.readlines()
file_content_string = ''.join(file_content)

lotto_list =[]

# Get number of lottery types
text_to_find = 'classCenter'
n = file_content_string.count(text_to_find)
n = n-1 # For last lottery type Keno - lottery winning numbers are available only on Keno site

# Get starting position of searched element
lotto_start_pos = file_content_string.find('resultLotto')
content_to_find_numbers_pos0 = lotto_start_pos

for j in range(n):

    # Get lotto lottery type
    results_item_pos1 = file_content_string.find('<div class="resultsItem ', lotto_start_pos) + len('<div class="resultsItem ')
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

    # Get number of winning numbers of the corresponding lottery type
    content_to_find_numbers_pos1 = file_content_string.find('<div class="resultnumber">', content_to_find_numbers_pos0)
    content_to_find_numbers_pos2 = file_content_string.find('<div class="resultsItem ', content_to_find_numbers_pos1)
    content_to_find_numbers = file_content_string[content_to_find_numbers_pos1:content_to_find_numbers_pos2]

    content_to_find_numbers_pos0 = content_to_find_numbers_pos2

    m = content_to_find_numbers.count('<span>')
    print(m)
    lotto_single_list = []

    # Get winning numbers
    result_number_pos = file_content_string.find('resultnumber', lotto_start_pos)

    for i in range(m):
            span_pos1 = file_content_string.find('span', result_number_pos) + len('span>')
            span_pos2 = file_content_string.find('</span', span_pos1)

            lotto_number=file_content_string[span_pos1:span_pos2]
            result_number_pos = span_pos2 + len('span')
            lotto_single_list.append(lotto_number)

            result_number_pos = span_pos2 + len('span')

    lotto_list.append(lotto_single_list)

print(lotto_list)

# Save output data to output_file.html as a table
with open("lotto_output_file.html", "w") as output_file:

    # Save data as html table
    def print_table(data, row_length):
        output_file.write('<table style="border: 1px solid black; border-collapse: collapse">\n')
        counter = 0
        output_file.write('<tr style="text-align: left; border-bottom: 1pt solid black">\n')
        output_file.write('<th>Lottery name</td>\n')
        output_file.write('<th>Lottery date</td>\n')
        output_file.write('<th>Winning numbers</td>\n')
        output_file.write('</tr>\n')
        for element in data:
            if counter % row_length == 0:
                output_file.write('<tr>\n')
            output_file.write('<td>%s</td>\n' % element)
            counter += 1
            if counter % row_length == 0:
                output_file.write('</tr>\n')
        if counter % row_length != 0:
            for i in range(0, row_length - counter % row_length):
                output_file.write('<td>&nbsp;</td>\n')
            output_file.write('</tr>\n')
        output_file.write('</table>\n')

    print_table(lotto_list, 3)

print("\n")
print("Output data saved in lotto_output_file.html")
