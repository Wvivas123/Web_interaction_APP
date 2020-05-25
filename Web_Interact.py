from selenium import webdriver
from time import sleep

username = input('[+] Enter your Username [+]')
pw = input('[+] Enter your Password [+]')


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input') \
            .send_keys(username)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input') \
            .send_keys(pw)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button') \
            .click()
        sleep(10)
        self.driver.close()


InstaBot(username, pw)
