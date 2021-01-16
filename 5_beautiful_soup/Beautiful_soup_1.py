# jsbeautifier  - convert code into correct spacing

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://someurl'
# oppening connection grabbing the page
uClient = uReq(my_url)
# download all webpage
page_html = uClient.read()
# close connection
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
page_soup.h1
page_soup.body.span

# find all objects on the page
# grab each product
containers = page_soup.findALL("div", {"class":'name_of_the_class'})
# contain = container[0]
# container.div.div.a.img["title"]

# create\open file where we save information

filename = "some_name.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)
for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_cost = container.findAll("li", {"class":'price-ship'})
    shipping = shipping_cost[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping_cost" + shipping_cost)
    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
f.close()