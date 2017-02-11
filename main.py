import csv

top100sites=  list()

with open(r'C:\Users\user\PycharmProjects\AdBlockerForensics\adbf\top100sites.txt') as sites:
    for site in sites.read().splitlines():
        top100sites.append(site)

with open(r'C:\Users\user\PycharmProjects\AdBlockerForensics\adbf\top500.domains.01.17.csv') as mozsites:
    rows = csv.reader(mozsites)
    li = list(rows)
    li = li[1:]





