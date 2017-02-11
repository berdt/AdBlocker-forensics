import time
import re
from operator import itemgetter

"""This script prints all filter hits including their lastHit parameter in human readable format.
The function process_filter_hits was a short attempt to parse this file realibly in such a way to classify
between definitly visited and maybe visited but due too time constraints it is not finished.
"""

patternsFileLoc = r'C:\Users\user\PycharmProjects\AdBlockerForensics\adbf\FireFox\AdBlock\adblockplus\patterns.ini'

def process_filter_hits(filterHits):
    for filterHit in filterHits:
        if 'third-party' in filterHit['filter']:
            if '~third-party' in filterHit['filter']:
                pass
            else:
                continue

        if filterHit['filter'][:4] == '@@||': #Rules starting like this are exceptions, they will override blocking rules.
            if 'domain=' in filterHit['filter']:
                domain = filterHit['filter'].split('domain=')[1]
                domains = domain.split('|')
                for d in domains:
                    if '~' in d:
                        domains.remove(d)
                print(domains)

        else: #Blocking rule
            if 'domain=' in filterHit['filter']:
                pass

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
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(hit['lastHit']))), hit['hitCount'], hit['filter']) #printing all filter
print('\n\n\n')

process_filter_hits(hits)

#domainNames = re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', filterHit['filter'])