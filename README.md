# AppStoreScrapper

A web scrapper for Apple's App Store. It fetched screenshots from the store listing and combined two at a time into one post. 

The idea behind this was to automate the repetitive task of manually downloading the screenshots and combining them via photoshop.

It's main usage was for https://www.instagram.com/todays.app/ .

## Dependencies
It has dependencies on [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Pillow](https://pillow.readthedocs.io/en/stable/). 
Install via the following commands:

`python3 -m pip install bs4`

`python3 -m pip install Pillow`

## Usage
Open the root folder via terminal and run `python3 app.py` You will be prompted for a URL, this needs to be of an app store listing.
