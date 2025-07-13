import requests
from bs4 import BeautifulSoup
import time
import csv
base_url = 'https://books.toscrape.com/catalogue/'



books_info = []

for page in range(1, 51):
    
    response = requests.get(base_url + 'page-' + str(page) + '.html')
    soup = BeautifulSoup(response.content, 'html.parser')
    

    books = soup.find_all('article', class_ = 'product_pod')
    for book in books:
        title= book.h3.a.get('title').strip()
        product_info = book.find('div', class_ = 'product_price')
        price = product_info.p.text.strip()
        instock = product_info.find('p', class_ = 'instock availability').text.strip()
        books_info.append([title, price, instock])
        if not book:
            break
    print(f'scrapped page {page}')
    time.sleep(1)
    

with open('books.csv', 'w', newline = '', encoding = 'utf-8') as file:
    writer= csv.writer(file)
    writer.writerows(books_info)







    


