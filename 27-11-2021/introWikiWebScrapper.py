from bs4 import BeautifulSoup
import requests
import re

def hasTOC(e):
    role = e.attrs.get("role")
    if role != None and "navigation" in role:
        return True

    children = e.find_all('div', {"role": "navigation"})
    hasTocChild = len(children) > 0
    return hasTocChild

def getIntro(soup):
    contentDiv = soup.find("div", {"class": "mw-parser-output"})

    introParaf = ""
    for child in contentDiv.children:

        if child.name == None:
            continue #skip weird no-name tags

        if hasTOC(child):
            break #parse until TOC

        if child.name != "p":
            continue #parse only p elements

        p = re.sub("\[\d+\]", "", child.text) #remove footnotes
        p = re.sub("\n", "", p) #remove new lines
        introParaf += " " + p

    return introParaf


#url = "https://en.wikipedia.org/wiki/Computer_vision"
#url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
#url = "https://en.wikipedia.org/wiki/Sardinal"
#url = "https://hr.wikipedia.org/wiki/Ra%C4%8Dunalni_vid"
#url = "https://en.wikipedia.org/wiki/Kona_Lanes"
#url = "https://en.wikipedia.org/wiki/LeVar_Woods"
url = "https://en.wikipedia.org/wiki/Gigi_Galli"

response = requests.request("GET", url)
soup = BeautifulSoup(response.content, features="html.parser")

introParaf = getIntro(soup)
print("Intro: " + introParaf)