import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class youtubeWatcher :
    def __init__(self,url,duration):
        self.browser = webdriver.Firefox()
        self.startEngine(url,duration)
        self.printNumber()
        self.wait(s=10)
        self.stopEngine()
    def printNumber(self):
        timeNow = str(datetime.datetime.now())
        numberOfViews = self.browser.find_element_by_xpath('//*[@id="count"]/ytd-video-view-count-renderer/span[1]').get_attribute('innerHTML')
        print(timeNow+': ',numberOfViews)
    def wait(self,h=0,m=0,s=0):
        dura = h*3600+m*60+s
        time.sleep(dura)
    def startEngine(self,url,duration):
        url = url
        self.browser.get(url)
        self.wait(s=3)
        element = self.browser.find_element_by_xpath('//body')
        element.send_keys(Keys.SPACE)
        self.wait(s=duration)
    def stopEngine(self):
        self.browser.close()

# url = 'https://youtu.be/wR28-gGxeWU'
# duration = 53 

url = 'https://youtu.be/ibnbTcjTsw4'
duration = 8*60+14

for i in range(100):
    engine = youtubeWatcher(url,duration)
    engine.wait(m=1)
