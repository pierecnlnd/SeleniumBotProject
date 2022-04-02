import time
import uuid
from selenium import webdriver

class instagramDownloader:
    def __init__(self,url):
        self.browser = webdriver.Firefox()
        self.startEngine(url)
        self.goToPicture()
        self.takeScreenShoot()
        self.stopEngine()
    def goToPicture(self):
        pictureUrl = self.browser.find_element_by_tag_name('img').get_attribute('src')
        self.wait(s=3)
        self.browser.get(pictureUrl)
        self.wait(s=3)
    def takeScreenShoot(self):
        self.browser.save_screenshot('picture/{}.png'.format(str(uuid.uuid4())))
        self.wait(s=3)
    def wait(self,h=0,m=0,s=0):
        dura = h*3600+m*60+s
        time.sleep(dura)
    def startEngine(self,url):
        self.browser.get(url)
        self.wait(s=3)
    def stopEngine(self):
        self.browser.close()

url = 'https://www.instagram.com/p/Cbz2iXlpduz/?utm_source=ig_web_copy_link'
engine = instagramDownloader(url)