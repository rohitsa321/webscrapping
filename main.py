import requests
import csv
from bs4 import BeautifulSoup

#  creating csv file with fields as:
        #                 Blog title 
        #                 Blog date
        #                 Blog image URL
        #                 Blog likes count
file = open('blogs_data.csv', 'w')
csv_obj = csv.writer(file)
fields = ['Blog title', 'Blog date', 'Blog image URL', 'Blog likes count']
csv_obj.writerow(fields)

# for getting data from every page
for i in range(1,46):
        page_url = f"https://rategain.com/blog/page/{i}"
        print("Fetching data from url:- ", page_url)
        
        # connet to rategain.com
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        blog_page = requests.get(page_url, headers=headers)

        # parsing wep page
        soup = BeautifulSoup(blog_page.text, 'html.parser')
        blog_items = soup.find(class_='blog-items').find_all(class_='blog-item')

        # populating data inside the csv file
        for item in blog_items:
            title = item.h6.string
            date = item.find_all(class_='bd-item')[0].find_all('span')[0].string

            # if blog does not contain image
            if item.find(class_='img') is None:
                img_url = 'null'
            else:
                img_url = item.find(class_='img').find('a')['data-bg']

            likes_txt = item.find(class_='zilla-likes').find('span').text
            likes = [int(i) for i in likes_txt.split() if i.isdigit()][0]

            # writing data into csv file
            csv_obj.writerow([title, date, img_url, likes])