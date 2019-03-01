# Get data from website
import requests

url = 'https://www.nbp.pl/home.aspx?f=/kursy/kursya.html'
response = requests.get(url)
content = response.text
exchange_rate_list = []

# Read nbp_exchange_rates_file
# nbp_exchange_rates_file = open('nbp_exchange_rates.csv','r')

# Get number of lottery types
text_to_find = '"bgt1 left"'
n = content.count(text_to_find)

# Get starting position and ending position of searched element
start_position = content.find('bgt1 left"')

for i in range(n):

    # Get searched elements
    currency_name_pos1 = content.find('bgt1 left">', start_position) + len('bgt1 left">')
    currency_name_pos2 = content.find('</td>', currency_name_pos1)
    currency_name = content[currency_name_pos1:currency_name_pos2]
    exchange_rate_list.append(currency_name)
    currency_code_pos1 = currency_name_pos2 + 31
    currency_code_pos2 = content.find('</td>', currency_code_pos1)
    currency_code = content[currency_code_pos1:currency_code_pos2]
    exchange_rate_list.append(currency_code)
    #print(currency_code_pos2)
    exchange_rate_pos1 = currency_code_pos2 + 29
    #print(exchange_rate_pos1)
    exchange_rate_pos2 = content.find('</td>', exchange_rate_pos1)
    exchange_rate = content[exchange_rate_pos1:exchange_rate_pos2]
    exchange_rate_list.append(exchange_rate)
    start_position = exchange_rate_pos2

print(exchange_rate_list)
exchange_rate_string = ' '.join(exchange_rate_list)

# Save data to output_file
with open('output_file.txt', 'w') as output_file:
    output_file.write(exchange_rate_string)

#output_file.close()