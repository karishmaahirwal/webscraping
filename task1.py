# from bs4 import BeautifulSoup, BeautifulStoneSoup
# import requests
# import pprint


# def top_movie_list(position_l,name_l,year_l,rating_l,url_l):
#     url="https://www.imdb.com/india/top-rated-indian-movies/"
#     req=requests.get(url)
#     soup=BeautifulSoup(req.text,"html.parser")
#     print(soup.prettify)

#     top_movie=[]
#     div=soup.find("div",class_="lister")
#     body=div.find("tbody",class_="lister-list")
#     title=body.find_all("tr")

#     details={'position':'','name':'','year':',','rating':'','url':''}
#     for i in range(0,len(position_l)):
#         details['position']=int(position_l[i])
#         details['name']=str(name_l[i])
#         year_l[i]=year_l[i][1:5]
#         details['year']=int(year_l[i])
#         details['rating']=float(rating_l[i])
#         details['url']=url_l[i]
#         top_movie.append(details.copy)

#         with open("my_task1.json","w")as _data:
#             json.dump(list,_data,indent=4)

#     return(top_movie)
# top_movie_list()


from bs4 import BeautifulSoup
import requests
import json


def scrape_top_list():   
    res="https://www.imdb.com/india/top-rated-indian-movies/"
    link2=requests.get(res)
    # print(link2)
    soup=BeautifulSoup(link2.text,"html.parser")
    
    list=[]
    div=soup.find("div",class_="lister")
    body=div.find("tbody",class_="lister-list")
    title=body.find_all("tr")
    no=0
    for i in title:
        no=no+1 
        movie_name=i.find("td",class_="titleColumn").a.get_text()
        name=movie_name
        year=i.find("td",class_="titleColumn").span.get_text()[1:5]
        year_m=int(year)
        rating=i.find("td",class_="ratingColumn").strong.get_text()
        ratting_float=float(rating)
        url=i.find("td",class_="titleColumn").a["href"]
        link=("https://www.imdb.com")+str(url)
        
        link1=link
        # list.append(dict)
        dict={"position":no,"name":name,"Year":year_m,"rating":ratting_float,"url":link1}
        list.append(dict)
        with open("my_file.json","w")as _data:
            json.dump(list,_data,indent=4)

    return (list)
scrape_top_list()






