
import requests

cities = ['Gdansk', 'Krakow', 'Lublin', 'Poznan', 'Szczecin', 'Warszawa', 'Wrocław']

# Create empty list
infoshare_list = []

# Get data from website
for i in range(7):
    url = 'https://infoshareacademy.com/?s&city=%s' %cities[i]

    response = requests.get(url)
    content=str(response.content)

    results_position=content.find('course-title')
    beginning_text_to_find = '<span>'
    ending_text_to_find = '</span>'

    second_results_position = content.find('course-info__paragraph course-info__paragraph--date')
    second_beginning_text_to_find ='--date">'
    second_ending_text_to_find = '</p>'

    # Count number of courses available in all cities
    text_to_find = '--date">'
    n = content.count(text_to_find)

    # Get course title, name of the course and course date from website
    for j in range(n):
        infoshare_list.append(cities[i])
        print(cities[i])
        beginning_span_position = content.find(beginning_text_to_find, results_position)
        second_beginning_span_position = content.find(second_beginning_text_to_find, second_results_position)
        ending_span_position = content.find(ending_text_to_find, beginning_span_position)
        second_ending_span_position = content.find(second_ending_text_to_find, second_beginning_span_position)
        infoshare_list.append(content[beginning_span_position+len(beginning_text_to_find):ending_span_position])
        print(content[beginning_span_position+len(beginning_text_to_find):ending_span_position])
        infoshare_list.append(content[second_beginning_span_position + len(second_beginning_text_to_find):second_ending_span_position])
        print(content[second_beginning_span_position + len(second_beginning_text_to_find):second_ending_span_position])
        results_position = ending_span_position
        second_results_position = second_ending_span_position

# print(infoshare_list)

# Save output data to output_file.html as a table
with open("output_file.html", "w") as output_file:
    
    # Save data as html table
    def print_table(data, row_length):
        output_file.write('<table style="border: 1px solid black; border-collapse: collapse">\n')
        counter = 0
        output_file.write('<tr style="text-align: left; border-bottom: 1pt solid black">\n')
        output_file.write('<th>City</td>\n')
        output_file.write('<th>Course name</td>\n')
        output_file.write('<th>Course date</td>\n')
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

    print_table(infoshare_list, 3)

print("\n")
print("Output data saved in output_file.html")







