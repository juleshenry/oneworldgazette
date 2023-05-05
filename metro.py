from _1dg import _1DG
from bs4 import BeautifulSoup
import requests

def find_mx():
    # parse the HTML content using BeautifulSoup
    url =  "https://jalopnik.com"
    # Fetch the HTML content of the URL
    response = requests.get(url)
    html = response.text

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all HTML elements
    elements = soup.find_all()

    # elements = soup.select('[style*="font-size"]')
    for o in elements:
        if str(o.css.tag.name) in 'h1h2h3h4h5':
            print(o.css.tag)
            print(o.parent.attrs['href'])
            1/0
            for a,b in (vars(o.parent).items()):
                print('@',a)
                print(b)
            1/0
        # print(o.css.tag.attrs['style'])
        # for a,b in vars(o.css.tag).items():
        #     print('@',a)
        #     print(str(b)[:40])
        # 1/0
        # print(*dir(o),sep='\n');1/0
    1/0
    # Initialize a dictionary to store font sizes and associated elements
    font_sizes = {}

    # Iterate through all elements and store their font sizes in the dictionary
    for element in elements:
        print(dir(element))
        try:
            font_size = int(element['style'].split('font-size:')[1].split(';')[0].strip().replace('px', ''))
            font_sizes[element] = font_size
        except KeyError as ke:
            print(ke)
        except IndexError:
            pass

    # Find the largest font size
    max_size = max(font_sizes.values())

    # Return the elements with the largest font size
    largest_font_elements = [element for element, size in font_sizes.items() if size == max_size]
    return largest_font_elements

	# # make a request to the URL and get the HTML content
	# response = requests.get(url)
	# html_content = response.content
	# soup = BeautifulSoup(html_content , 'html.parser')

	# # find all the elements on the page
	# all_elements = soup.find_all()

	# # initialize variables to hold the max font size and the element(s) with the max font size
	# max_font_size = 0
	# max_font_size_elements = []

	# # loop through all the elements and find the one(s) with the largest font size
	# for element in all_elements:
	#     # get the computed style of the element
	#     print(dir(soup));1/0
	#     computed_style = soup._style_for_tag(element)

	#     # get the font size from the computed style
	#     font_size = int(computed_style.get('font-size', '').split('px')[0])

	#     # if the font size is larger than the current max, update the max and the elements
	#     if font_size > max_font_size:
	#         max_font_size = font_size
	#         max_font_size_elements = [element]
	#     elif font_size == max_font_size:
	#         max_font_size_elements.append(element)

	# # print the element(s) with the max font size
	# for element in max_font_size_elements:
	#     print(element)


if __name__=='__main__':
	print("NEWS")
	print(find_mx())
