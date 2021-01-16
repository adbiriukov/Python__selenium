from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

my_url = 'https://www.newegg.com/p/pl?d=ryzen+5+3600'
# oppening connection grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
# grab each product
containers = page_soup.findAll("div", {"class":'item-cell'})


# create\open file where we save information
filename = "beautiful_soup_2_3.csv"
f = open(filename, "a")

# headers = "brand, product_name, shipping\n"
# f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-img"})
    product_name = title_container[0].text

    price = container.findAll("li", {"class": "price-current"})
    final_price = re.sub('\D', '', price[0].text)


    # print("brand: " + brand)
    # print("product_name: " + product_name)
    # print("shipping_cost" + final_price)
    f.write(brand + "," + product_name.replace(",", "|") + "," + final_price + "\n")
f.close()

# Cut all no diggits from string
##
# import re
# re.sub('\D', '', price[0].text)