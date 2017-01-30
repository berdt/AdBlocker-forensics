top100sites=  list()

with open(r'C:\Users\user\PycharmProjects\AdBlockerForensics\adbf\top100sites.txt') as sites:
    for site in sites.read().splitlines():
        top100sites.append(site)

print('Loaded the most popular 50 sites of the Netherlands')



