from _1dg import _1DG
from bs4 import BeautifulSoup
import requests

def find_mx():
	# parse the HTML content using BeautifulSoup
	url =  "https://jalopnik.com"

	# make a request to the URL and get the HTML content
	response = requests.get(url)
	html_content = response.content
	soup = BeautifulSoup(html_content , 'html.parser')

	# find all the elements on the page
	all_elements = soup.find_all()

	# initialize variables to hold the max font size and the element(s) with the max font size
	max_font_size = 0
	max_font_size_elements = []

	# loop through all the elements and find the one(s) with the largest font size
	for element in all_elements:
	    # get the computed style of the element
	    computed_style = soup._style_for_tag(element)

	    # get the font size from the computed style
	    font_size = int(computed_style.get('font-size', '').split('px')[0])

	    # if the font size is larger than the current max, update the max and the elements
	    if font_size > max_font_size:
	        max_font_size = font_size
	        max_font_size_elements = [element]
	    elif font_size == max_font_size:
	        max_font_size_elements.append(element)

	# print the element(s) with the max font size
	for element in max_font_size_elements:
	    print(element)


if __name__=='__main__':
	print("NEWS")
	print(find_mx())
