
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import undetected_chromedriver as uc
import time
from random import randint


reddit_url = "https://www.reddit.com/login/"
subreddit_url = "subreddit url"     #replace with subreddit url you want to post to.
reddit_password = "password"        #replace password with your actual reddit password.
reddit_username = "username"        #replace username with your actual reddit username.


class Reddit():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument(
            '--user-data-dir=/Users/macintosh/Library/Application Support/Google/Chrome/Default')  
        #replace this with your own browser profile. type-> chrome://version in the address bar and copy 
        #the profile path and paste it afer --user-data-dir=
        self.driver = uc.Chrome()
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get(reddit_url)
        time.sleep(2)

    def login(self):
        login_field = self.driver.find_element(By.ID, "loginUsername")
        login_field.send_keys(reddit_username)
        password_field = self.driver.find_element(By.ID, "loginPassword")
        password_field.send_keys(reddit_password)
        time.sleep(1)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)

    def post(self, title, message):
        self.driver.get(f"{subreddit_url}/submit")
        time.sleep(randint(5, 10))
        try:
            self.title_field = self.driver.find_element(
                By.XPATH, '//textarea[@placeholder="Title"]')
            self.title_field.send_keys(title)
            time.sleep(2)
        except ElementNotInteractableException:
            self.text_field = self.driver.find_element(
                By.CSS_SELECTOR, 'div.public-DraftEditor-content')
            self.text_field.send_keys(message, Keys.PAGE_UP)
            time.sleep(5)
            self.title_field = self.driver.find_element(
                By.XPATH, '//textarea[@placeholder="Title"]')
            self.title_field.send_keys(title)
            time.sleep(2)
        else:
            self.text_field = self.driver.find_element(
                By.CSS_SELECTOR, 'div.public-DraftEditor-content')
            self.text_field.send_keys(message)
            time.sleep(5)
            self.post_button = self.driver.find_element(
                By.XPATH, '//button[contains(text(),"Post")][@tabindex="0"]')
            hover = ActionChains(
                driver=self.driver).move_to_element(self.post_button)
            hover.click()
            hover.perform()
            time.sleep(randint(5, 15))
            self.driver.get(subreddit_url)
            time.sleep(randint(2700, 3600))
