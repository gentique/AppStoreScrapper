from urllib.request import urlopen as uReq
import urllib
from bs4 import BeautifulSoup as soup
import os
import utils
import datetime
import pathlib
from webbrowser import open as openFinderUrl

# Get current date
currentDate = datetime.datetime.now()

my_url = input("Please enter url: ")

# try to load the url
try:
    uClient = uReq(my_url)
except Exception as e:
    print('Couldnt read url')
    print(e)
    exit(1)

page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

appDescription = page_soup.find("div", {"class":"section__description"}).p.getText()

appTitle = page_soup.title.string.replace(" on the App Store", "")

imageContainers = page_soup.findAll("li", {"class": "l-column small-2 medium-3 large-3"})

imagePathsForIG = []
fileCounter = 0
directoryPath = f'/Volumes/GB_SD/todays_app/{currentDate.year}/{currentDate.month}.{utils.returnMonthName(currentDate.month)}/{currentDate.day}/{appTitle}'
pathlib.Path(directoryPath).mkdir(parents=True, exist_ok=True)

for container in imageContainers:
    imageUrl = container.source["srcset"].split(',')[2].replace(" 3x", "")
    imgType = imageUrl[-4:]
    print(directoryPath+'/'+(str(fileCounter)+imgType))

    imagePathToSave = directoryPath + '/' + (str(fileCounter) + imgType)

    urllib.request.urlretrieve(imageUrl, imagePathToSave)
    if fileCounter<4:
        imagePathsForIG.append(imagePathToSave)

    fileCounter += 1
    if fileCounter == 4:
        break
    print(imageUrl)

utils.createImage(imagePathsForIG[0] ,imagePathsForIG[1], directoryPath, '0')
utils.createImage(imagePathsForIG[2] ,imagePathsForIG[3], directoryPath, '1')

print("This is the description: " + appDescription)
print("This is the title: " + appTitle)
outfile = open(directoryPath+'/desc.txt', "w")
outfile.write(appDescription)
outfile.close()

openFinderUrl(f'file://{directoryPath}')
