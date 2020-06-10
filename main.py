from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

username="" # Username Here
pw="" # Password Here

class instagramBot():
    def __init__(self, username, pw):
        self.username = username
        self.password = pw
        self.bot = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver.exe') #Webdriver executable path - chromedriver.exe for chrome, geckodriver.exe for firefox
    
    def login(self):
        bot = self.bot
        bot.get("https://instagram.com")
        sleep(2)
        usernameElement = bot.find_element_by_name('username')
        pwElement = bot.find_element_by_name('password')
        usernameElement.clear()
        pwElement.clear()

        usernameElement.send_keys(self.username)
        pwElement.send_keys(self.password)
        pwElement.send_keys(Keys.RETURN)
        sleep(5)
        bot.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(1)
        bot.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        

instagramBot(username, pw).login()