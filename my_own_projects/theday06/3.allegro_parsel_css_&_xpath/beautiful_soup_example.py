from bs4 import BeautifulSoup
import requests
import os

# Function to get page from url if file does not exist, if file exists open the file
def get_page(url, filename):
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8') as input_data:
            content = input_data.read()
    else:
        response = requests.get(url)
        content = response.text
        with open(filename, 'w', encoding='utf-8') as output_data:
            output_data.write(content)
    return content

# Function to get all searched instances from the content of the file
def find_all_links(content, soup_instance):
    return soup_instance.find_all('a')
    # return soup_instance.find_all('img')

# Get page from url and get all searched instances from the content of the file
if __name__ == '__main__':
    url = 'https://www.wakacyjnipiraci.pl/'
    filename = 'wakacyjnipiraci.html'
    html_content = get_page(url, filename)
    soup = BeautifulSoup(html_content, 'html.parser')
    print(find_all_links(html_content, soup))

