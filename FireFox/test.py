from adbf import main
import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import shutil
import os
from time import time

print(selenium.__version__)




profile = webdriver.FirefoxProfile()
profile.add_extension(extension='AdBlockPlus.xpi')

b = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
ff = webdriver.Firefox(profile, firefox_binary=b)


