print("\n"*500)

import requests

page = requests.get("https://basketball.realgm.com/nba/teams/New-York-Knicks/20/news/wiretap")

#print(page.status_code)


from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, "html5lib")
#print(soup.prettify())

site = soup.find(id="site-takeover")
#print(site.prettify())

main1 = site.find(class_="main-container")
#print(main1.prettify())

main2 = main1.find(class_="main wrapper clearfix container")
#print(main2.prettify())

column = main2.find(class_="large-column-left news-column")
#print(column.prettify())

#----------------------------------------------------
#Finally within news 

#Article clearfix is the list of div tags that has the info needed
articles = column.find_all(class_="article clearfix")

info = articles[0]
date = articles[0]

date = info.find("p").get_text()
print("[ " + date.strip() + " ]")

title = info.find("a").get_text()
print(title)
body = info.find(class_="article-body")
print(body.text)