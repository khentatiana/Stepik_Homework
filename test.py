from selenium import webdriver
import time
import sys

print(sys.version)
print(sys.version_info)


browser = webdriver.Chrome()
link = "www.google.com"
browser.get(link)

time.sleep(10)