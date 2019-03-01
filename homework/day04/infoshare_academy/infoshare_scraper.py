import requests

cities = ['Gdansk', 'Krakow', 'Lublin', 'Poznan', 'Szczecin', 'Warszawa', 'Wrocław']
infoshare_list = []

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

     text_to_find = '--date">'

     n = content.count(text_to_find)
     print("\n")
     infoshare_list.append(cities[i])
     print(cities[i])

     for j in range(n):
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

print("\n")
print(infoshare_list)





