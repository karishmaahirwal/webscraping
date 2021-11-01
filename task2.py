from task1 import scrape_top_list
import json

list=scrape_top_list()                                                                 
def group_by_year(movies):
    years=[]
    for i in movies:
        if i["Year"] not in years:
            years.append(i["Year"])
    movies_dict={i:[] for i in  years}
    for index2 in movies:
        year=index2["Year"]
        for update_year in movies_dict:
            if (update_year)==(year):
                movies_dict[update_year].append(index2)
    with open ("task2.json","w")as files:
        json.dump(movies_dict,files,indent=5)
    return movies_dict
group_by_year(list)
       