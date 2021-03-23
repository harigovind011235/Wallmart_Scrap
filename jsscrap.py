from bs4 import BeautifulSoup
from selenium import webdriver
import json

chromedriver_path= "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chromedriver_path)
url_list = []
for i in range(1,10):
    url_list.append('https://www.walmart.com/browse/personal-care/hand-soap/1005862_1001719?page=' + str(i))

# print(url_list)

for url in url_list:

    driver.get(url)
    page_source = driver.page_source

    myhtml = BeautifulSoup(page_source, 'lxml')
    # print(myhtml)
    finallist = []
    productsdiv = myhtml.select('.u-size-1-5-xl')

    for data in productsdiv:
        product_title = [x.text for x in data.select('.truncate-title span')]
        delivery_time = [x.text for x in data.select('.font-normal')]
        product_price = [x.text for x in data.select('.enable-2price-2')]
        product_imglink = [x.attrs['src'] for x in data.select('#searchProductResult img')]
        product_category = [x.text for x in myhtml.select('.breadcrumb-list')]
        product_link = [x.attrs['href'] for x in myhtml.select('.product-title-link')]

        walmartdict = {'producttitle':product_title,
                       'deliverytime':delivery_time,
                       'productprice':product_price,
                       'productimglink':product_imglink,
                       'productcategory':product_category,
                       }
        finallist.append(walmartdict)



        json_text = json.dumps(finallist,indent=4)
        with open('wallmartdata.json', 'w') as json_file:
            json_file.write(json_text)











