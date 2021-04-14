import bs4 as bs
import urllib.request

website = urllib.request.urlopen('https://www.espn.com/mens-college-basketball/team/stats/_/id/2250').read()

soup = bs.BeautifulSoup(website, 'html.parser')