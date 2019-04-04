import re

text1 = '56500 km'
text2 = '2400 cm³'
text3 = '140 KM'

pattern = '\d+'
# pattern = '[0-9]+'

match = re.search(pattern, text1)
start_pos = match.start()
end_pos = match.end()
print(text1[start_pos:end_pos])

match = re.search(pattern, text2)
start_pos = match.start()
end_pos = match.end()
print(text2[start_pos:end_pos])

match = re.search(pattern, text3)
start_pos = match.start()
end_pos = match.end()
print(text3[start_pos:end_pos])



