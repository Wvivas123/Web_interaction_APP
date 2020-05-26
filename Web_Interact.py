from selenium import webdriver
from time import sleep
from getpass import getpass


username = input('[+] Enter your Username [+]')
pw = getpass('[+] Enter your Password [+]')


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
        sleep(7)
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[3]/button[1]') \
            .click()
        sleep(5)

        self.driver.get("https://www.instagram.com/explore/tags/openframeworks/")
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]").click()
        sleep(10)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
        sleep(40)




InstaBot(username, pw)
