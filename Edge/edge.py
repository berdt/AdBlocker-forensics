from adbf import main
from selenium import webdriver
from time import sleep
from time import time
import selenium

edge = webdriver.Edge()

print(selenium.__version__)

Control = True
AdBlock = False
Private = False

if Control:
    mode = 'Control'
    print('Getting control sample')
    timestamps = open('Edge_Control_Timestamps.txt', 'w')

elif AdBlock:
    mode = 'AdBlock'
    print('Getting AdBlock sample, install the adblocker, sleeping for 120')
    edge.get('https://getadblock.com/')
    sleep(120)
    timestamps = open('Edge_AdBlock_Sample.txt', 'w')

elif Private:
    mode = 'Private'
    print('Getting AdBlock sample, install the adblocker, sleeping for 120')
    edge.get('https://getadblock.com/')
    sleep(120)
    print('Getting incognito AdBlock sample')
    timestamps = open('Edge_Private_Sample.txt', 'w')


for site in main.top100sites:
    edge.get(f'http://{site}')
    timestamps.write(f'{site} {str(time())}\n')
    sleep(5)

print('done make a snapshot etc')