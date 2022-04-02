import json
import re
import time
import uuid
from selenium import webdriver

class twitterStalker:
    def __init__(self,url):
        self.browser = webdriver.Firefox()
        self.userInfo = {}
        self.startEngine(url)
        self.scrapUserInfo()
        self.saveUserInfo()
        self.stopEngine()
    def scrapUserInfo(self):
        userNameID = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/span').get_attribute('innerHTML')
        userBio = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/div[1]').get_attribute('innerHTML')
        userBio = self.filterUserBio(userBio)
        userLocation = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div/span[1]/span/span').get_attribute('innerHTML')
        userJoinDate = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div/span[2]/span').get_attribute('innerHTML')
        userFollowers = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div[2]/a/span[1]/span').get_attribute('innerHTML')
        userFollowing = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div[1]/a/span[1]/span').get_attribute('innerHTML')
        self.wait(s=3)
        self.userInfo['username id'] = str(userNameID)
        self.userInfo['bio'] = str(userBio)
        self.userInfo['location'] = str(userLocation)
        self.userInfo['join date'] = str(userJoinDate)
        self.userInfo['followers'] = str(userFollowers)
        self.userInfo['following'] = str(userFollowing)
    def filterUserBio(self,userBio):
        pattern = r'>(.+)</'
        userBio = re.findall(pattern,userBio)
        return userBio
    def saveUserInfo(self):
        userID = str(uuid.uuid4())
        with open('userInfo/user_{}.json'.format(userID), 'w') as fp:
            json.dump(self.userInfo, fp)
    def wait(self,h=0,m=0,s=0):
        dura = h*3600+m*60+s
        time.sleep(dura)
    def startEngine(self,url):
        self.browser.get(url)
        self.wait(s=3)
    def stopEngine(self):
        self.browser.close()

url = 'https://twitter.com/WhatsApplD'
engine = twitterStalker(url)

userNameID = engine.userInfo['username id']
userBio = engine.userInfo['bio']
userLocation = engine.userInfo['location']
userJoinDate = engine.userInfo['join date']
userFollowers = engine.userInfo['followers']
userFollowing = engine.userInfo['following']
print('username id : {}\n'.format(userNameID))
print('bio         : {}\n'.format(userBio))
print('location    : {}\n'.format(userLocation))
print('join date   : {}\n'.format(userJoinDate))
print('followers   : {}\n'.format(userFollowers))
print('following   : {}\n'.format(userFollowing))