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
#print(len(articles))
i = 0
while (i < len(articles)):
    while (i < 10):
        print("#%d" % (i+1))
        info = articles[i]
        date = articles[i]

        date = info.find("p").get_text()
        print("[ " + date.strip() + " ]")

        title = info.find("a").get_text()
        print(title)
        body = info.find(class_="article-body")
        print(body.text)
        
        print("------------------------------------------------------------------------------------------------------------------------------------------")

        i += 1
# html code changes after 10 news items
    print("#%d" % (i+1))
    info = articles[i]
    date = articles[i]

    date = info.find("p").get_text()
    print("[ " + date.strip() + " ]")

    title = info.find("a").get_text()
    print(title)
    body = info.find(class_="article-content content")
    print(body.text)
    
    print("------------------------------------------------------------------------------------------------------------------------------------------")

    i += 1