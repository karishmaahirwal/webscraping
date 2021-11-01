from task1 import scrape_top_list
from task2 import group_by_year
import pprint
import json

list=scrape_top_list()
dec=group_by_year(list)
# dec=group_by_year()
def group_by_decade(movies):
    moviesdic={}
    list1=[]
    for i in movies:
        mod=i%10
        dec=i-mod
        if dec not in list1:
            list1.append(dec)
        list1.sort
    for i in list1:
        moviesdic[i]=[]
    for i in moviesdic:
        dec=i+9
        for x in movies:
            if x<=dec and x>=i:
                for j in movies[x]:
                    moviesdic[i].append(j)
                    with open("task3.json","w")as _data:
                        json.dump(moviesdic,_data,indent=4)
    # return moviesdic
print(group_by_decade(dec))