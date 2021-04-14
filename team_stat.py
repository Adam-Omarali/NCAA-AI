import bs4 as bs
import urllib.request
import pandas as pd


website = urllib.request.urlopen('https://www.espn.com/mens-college-basketball/team/stats/_/id/2250').read()

soup = bs.BeautifulSoup(website, 'html.parser')

metrics = []
for stat in soup.find_all('th', class_='tar stats-cell Table__TH'):
    metrics.append(stat.text)
    metrics = " ".join(metrics)
    metrics = metrics.split('\n')

metrics = metrics[0].split()
season_metrics = metrics[metrics.index('3P%') + 1:]
metrics = metrics[:metrics.index('3P%') + 1]


stats = []
test = soup.find_all("td")

for stat in test:
    if len(stat.span.text) < 5:
        stats.append(stat.span.text)

leader_stats = []
leader_metrics = []
unique_leaders = []
for stat in soup.find_all('div', class_= 'clr-gray-01 pr3 hs2'):
    leader_stats.append(stat.text)

for metric in soup.find_all('h2', class_='h8 mb2 clr-gray-03'):
    leader_metrics.append(metric.text)

for leader in soup.find_all("h3", class_="di n8"):
    unique_leaders.append(leader.text)

unique_leaders = len(set(unique_leaders))
print(unique_leaders)
print(leader_metrics)
print(leader_stats)

test2 = soup.find("tbody", class_='Table__TBODY').span.text
placeholder = stats[stats.index('') + 1 :]

print(metrics)
print(stats[stats.index('') + 1 :stats.index('') + len(metrics) - 1])
print(season_metrics)
print(placeholder[placeholder.index('') + 1 : placeholder.index('') + len(season_metrics)])

#soup.find("td", {'class':"Table__TD", "id": "id_name"}) <- returns only one matching tag
