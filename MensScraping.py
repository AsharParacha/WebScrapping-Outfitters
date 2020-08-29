import requests
from bs4 import BeautifulSoup
import html5lib
import csv

EndingPage = 2
Pageurl =[]
Shirt_name=[]
Oprice =[]
Nprice =[]
detail=''
for starting_page in range(EndingPage):
    print("Scraping Page No:", starting_page + 1)
    r = requests.get('https://outfitters.com.pk/collections/men-shirt-sale?page=' + str(starting_page + 1))
    soup = BeautifulSoup(r.content, 'html5lib')
    #print(soup)

    for item in soup.find_all(class_='product-bottom'):
       #print(item)
        for items in item.find_all(class_='product-title'):
           #all links are print
           links= items.get('href')
           CompleteLink = 'https://outfitters.com.pk/' + links
           print(CompleteLink)
           Pageurl.append(CompleteLink)

           # all shirt name are print
           details = detail + items.get_text().strip()
           Shirt_name.append(details)
           print(details)
           #Price
        for prices in item.find_all(class_='price-sale'):
            Price = detail + prices.get_text().strip()
            OldPrice = Price.split()[1]
            print(OldPrice)
            Oprice.append(OldPrice)
            NewPrice = Price.split()[3]
            print(NewPrice)
            Nprice.append(NewPrice)

with open("OutFittersShirts.csv", "w",newline='',encoding="utf-8") as csvFile:
    fieldnames = ['Pageurl','ShirtName','Oprice','Nprice']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    for P,S,O,N in zip(Pageurl,Shirt_name,Oprice,Nprice):
        writer.writerow({'Pageurl':P , 'ShirtName':S, 'Oprice':O,'Nprice':N})











