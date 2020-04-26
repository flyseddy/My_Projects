import requests
from bs4 import BeautifulSoup
from csv import writer

url = 'https://www.newegg.com/Gaming-Monitors/SubCategory/ID-3743?Tid=898493&cm_sp=CAT_Monitors_2-_-VisNav-_-Gaming-Monitors_2'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

containers = soup.find_all(class_='item-container')

with open('monitors.csv', 'w') as f:
    csv_writer = writer(f)
    headers = ['Title', 'Price']
    csv_writer.writerow(headers)

    for container in containers:
        title = container.find(class_='item-title').get_text().replace('\n', '')
        price = container.find(class_='price-current').get_text().replace('\n', '')
        csv_writer.writerow([title, price])

# print(f"{title} - ${price}")
