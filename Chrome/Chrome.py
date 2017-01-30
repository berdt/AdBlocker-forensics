from adbf import main
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from time import time

Control = False
AdBlock = True
Private = False

if Control:

    chrome_options = Options()
    chrome_options.add_argument(r"user-data-dir=C:\Users\user\PycharmProjects\AdBlockerForensics\adbf\Chrome\Chrome_Control_Sample2")
    cd = webdriver.Chrome(chrome_options=chrome_options)
    print('Getting control sample')
    timestamps = open('Chrome_Control_Timestamps.txt', 'w')

elif AdBlock:

    chrome_options = Options()
    chrome_options.add_argument(r"user-data-dir=C:\Users\user\PycharmProjects\AdBlockerForensics\adbf\Chrome\Chrome_Adblock_Sample")
    chrome_options.add_extension('AdBlock_3_8_4.crx')
    cd = webdriver.Chrome(chrome_options=chrome_options)
    print('Getting AdBlock sample')
    timestamps = open('Chrome_AdBlock_Sample.txt', 'w')

elif Private:

    chrome_options = Options()
    chrome_options.add_argument(r"user-data-dir=C:\Users\user\PycharmProjects\AdBlockerForensics\adbf\Chrome\Chrome_Incognito_Sample")
    chrome_options.add_argument("--incognito")
    chrome_options.add_extension('AdBlock_3_8_4.crx')
    cd = webdriver.Chrome(chrome_options=chrome_options)
    print('Getting incognito AdBlock sample')
    timestamps = open('Chrome_Incognito_Sample.txt', 'w')


for site in main.top100sites:
    cd.get(f'http://{site}')
    timestamps.write(f'{site} {str(time())}\n')
    sleep(5)

print('done')
timestamps.close()
cd.quit()

