# Importing modules
import requests
from bs4 import BeautifulSoup
from install_packages import install_packages
from logo import logo

# calling ASCII logo
print(logo)
print("########################################")
print("### Installing requirements packages ###")
print("########################################")

# Calling function installing requirements packages
install_packages()

# variable urls
root_page = 'https://quotes.toscrape.com/'
urls = 'https://quotes.toscrape.com/page/'
# variable to manage the multiple web pages
# If you need to do web scraping to all packages you can update this variable
number_page = 2

print("")
print("#################################################################")
print(f'### Starting web scraping on web {root_page} ###')
print("#################################################################")
print("")


# function web scraping
def web_scraping():
    # for loop over pages
    for pages in range(1, number_page):

        html = requests.get(urls + str(pages))

        soup = BeautifulSoup(html.text, 'html.parser')

        # for loop over class quotes
        for i in soup.findAll("div", {"class": "quote"}):
            print((i.find("span", {"class": "text"})).text)

            export_quotes = (i.find("span", {"class": "text"})).text

            # storing data
            with open("export_quotes.txt", "a") as f:
                f.write(export_quotes)

        # function remove tags
        def remove_tags():

            for data in soup(['style', 'script']):
                # Remove tags
                data.decompose()

            # return data by retrieving the tag content
            return ' '.join(soup.stripped_strings)

        export_remove_tags = remove_tags()

        # storing data
        with open("export_remove_tags.txt", "a") as f:
            f.write(export_remove_tags)

        # Print the extracted data
        print("")
        print(remove_tags())
        print("")

# calling the function web_scraping
web_scraping()
