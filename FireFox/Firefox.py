from adbf import main
import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import shutil
import os
from time import time

print(selenium.__version__)

Control = True
AdBlock = False
Private = False

if Control:
    mode = 'Control'

    b = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
    ff = webdriver.Firefox(firefox_binary=b)

    dataDir = ff.firefox_profile.path
    print('Getting control sample')
    timestamps = open('FireFox_Control_Timestamps.txt', 'w')

elif AdBlock:
    mode = 'AdBlock'

    profile = webdriver.FirefoxProfile()
    profile.add_extension(extension='AdBlockPlus.xpi')

    b = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
    ff = webdriver.Firefox(profile, firefox_binary=b)

    dataDir = ff.firefox_profile.path
    print('Getting AdBlock sample')
    timestamps = open('Firefox_AdBlock_Sample2.txt', 'w')

elif Private:
    mode = 'Private'

    profile = webdriver.FirefoxProfile()
    profile.add_extension(extension='AdBlockPlus.xpi')

    b = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
    b.add_command_line_options("-private")
    ff = webdriver.Firefox(profile, firefox_binary=b)

    dataDir = ff.firefox_profile.path
    print('Getting incognito AdBlock sample')
    timestamps = open('Firefox_Private_Sample.txt', 'w')

for site in main.top100sites:
    ff.get(f'http://{site[1]}')
    timestamps.write(f'{site} {str(time())}\n')
    sleep(5)

timestamps.close()

#using ff.quit() will delete the data so use close.
ff.close()

#without sleeping there will still be a lock on some files at time of copying.
sleep(5)

#copy dir over
shutil.copytree(dataDir, f'{os.getcwd()}/{mode}2')

print('done')