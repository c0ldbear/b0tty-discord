import requests
from bs4 import BeautifulSoup

def AllNews(news):
    return news

def LatestTenNews(news):
    return news[1:11]

def FetchNews():
    return parseFetchedNews(fetchNewsDagensNyheter())

def fetchNewsDagensNyheter():
    url = "https://www.dn.se/nyhetsdygnet/" 
    session = requests.Session()
    r = session.get(url)
    return r

def parseFetchedNews(reqs):
    soup = BeautifulSoup(reqs.text, "html.parser")
    news_timeline = soup.find("div", attrs={'class':'timeline-page'})
    news_links = news_timeline.find_all("a", href=True)
    news = []
    for link in news_links:
        topic = str(link.find("h3"))
        cleanedTopic = cleanTopics(topic)
        a_link = link["href"]
        news += [(cleanedTopic, a_link)]
    return news

def cleanTopics(topic):
    removeHtmlTags = topic.replace('<h3>', '').replace('</h3>', '')
    removeNewLine = removeHtmlTags.replace('\n', '')
    removeTabs = removeNewLine.replace('\t', '')
    removeSpaces = removeTabs.replace('  ', '')
    cleanedTopic = removeSpaces
    return cleanedTopic 
