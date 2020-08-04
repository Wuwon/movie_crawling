import csv
import requests
from bs4 import BeautifulSoup

url="https://movie.naver.com/movie/running/current.nhn"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

final_data=[]
movie_list = soup.select(
    '#content > .article > .obj_section > .lst_wrap > ul > li ')

for movie in movie_list:
    a_tag = movie.select_one('dl > dt > a')
    movie_code = a_tag['href'].split("code=")[1]
    movie_name = a_tag.contents[0]
    
    movie_data={
        "code" : movie_code,
        "name" : movie_name
    }
    final_data.append(movie_data)
# print(final_data[0])
    with open('./movie_data.csv','a', encoding='utf-8') as csvfile:
        fieldnames = ['code','name']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writerow(movie_data)

    print(movie_data,'\n')