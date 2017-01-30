from adbf import main
from selenium import webdriver
from time import sleep
from time import time
import selenium

ie = webdriver.Ie()

print(selenium.__version__)

Control = True
AdBlock = False
Private = False

if Control:
    mode = 'Control'
    print('Getting control sample')
    timestamps = open('IE_Control_Timestamps.txt', 'w')

elif AdBlock:
    mode = 'AdBlock'
    print('Getting AdBlock sample, install the adblocker, sleeping for 120')
    ie.get('https://adblockplus.org/nl/')
    sleep(120)
    timestamps = open('IE_AdBlockPlus_Sample.txt', 'w')

elif Private:
    mode = 'Private'

    print('Getting incognito AdBlock sample')
    timestamps = open('IE_Private_Sample.txt', 'w')


for site in main.top100sites:
    ie.get(f'http://{site}')
    timestamps.write(f'{site} {str(time())}\n')
    sleep(5)

print('done make a snapshot etc')



# DesiredCapabilities capabilities = DesiredCapabilities.internetExplorer();
# capabilities.setCapability(InternetExplorerDriver.FORCE_CREATE_PROCESS, true);
# capabilities.setCapability(InternetExplorerDriver.IE_SWITCHES, "-private");