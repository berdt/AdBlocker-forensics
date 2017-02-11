import time
import re
from operator import itemgetter
from adbf import main

main.top100sites = [x[1].lower().replace('/', '') for x in main.li]

patternsFileLoc = r'C:\Users\user\PycharmProjects\AdBlockerForensics\adbf\FireFox\AdBlock\adblockplus\patterns.ini'
#patternsFileLoc = r'C:\Users\user\PycharmProjects\AdBlockerForensics\adbf\FireFox\AdBlock5002\adblockplus\patterns.ini'


def process_filter_hits(filterHits):
    hitAmount = 0
    for domain in main.top100sites:
        for filterHit in filterHits:
            if domain in filterHit['filter']:
                hitAmount+=1
                print('May have Visted', domain, 'at', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(filterHit['lastHit']))), 'DETECTED BY FILTER_HIT:', filterHit['filter'])
                break
    print(hitAmount)

hits = list()
with open(patternsFileLoc, encoding='utf8') as file:
    lines = file.read().splitlines()
    for i, line in enumerate(lines):
         if line[:5] == 'text=': #All filter hits start with text=
             filter = line[5:] #the filter
             hitCount = lines[i+1][9:] #the hitcount
             lastHit = lines[i+2][8:18] #10 numbers from epoch time

             hits.append({'filter': filter, 'hitCount':hitCount, 'lastHit':lastHit})

             #print(filter, hitCount, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(lastHit))))

hits = sorted(hits, key=itemgetter('lastHit'))
for hit in hits:
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(hit['lastHit']))), hit['hitCount'], hit['filter'])
print('\n\n\n')
process_filter_hits(hits)



# domainNames = re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', filterHit['filter'])
