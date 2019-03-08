# Get data from website
import requests

url = 'https://www.nbp.pl/home.aspx?f=/kursy/kursya.html'
response = requests.get(url)
content = response.text
exchange_rate_list = []

# Read nbp_exchange_rates_file
# nbp_exchange_rates_file = open('nbp_exchange_rates.csv','r')

# Get number of lottery types
text_to_find = ' left"'
n = content.count(text_to_find)

# Get starting position and ending position of searched element
start_position = content.find('bgt1 left"')

for i in range(n):

    # Get searched elements: currency name, currency code and exchange rate
    currency_name_pos1 = content.find(' left">', start_position) + len(' left">')
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

# Save output data to exchange_rates.html as a table
with open("exchange_rates.html", "w") as output_file:
    # Save data as html table
    def print_table(data, row_length):
        output_file.write('<table style="border: 1px solid black; border-collapse: collapse">\n')
        counter = 0
        output_file.write('<tr style="text-align: left; border-bottom: 1pt solid black">\n')
        output_file.write('<th>Currency name</td>\n')
        output_file.write('<th>Currency code</td>\n')
        output_file.write('<th>Exchange rate</td>\n')
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

    print_table(exchange_rate_list, 3)

print("\n")
print("Output data saved in exchange_rates.html")

