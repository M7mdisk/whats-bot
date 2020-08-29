# SETUP
import traceback
import func
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random as rn
PATH = './chromedriver'
options = webdriver.ChromeOptions()
# options.add_argument('--user-data-dir=./User_Data') Uncomment If you would like to save the session
driver = webdriver.Chrome(executable_path=PATH, options=options)
wait = WebDriverWait(driver, 10)
wait5 = WebDriverWait(
    driver, 5)

driver.get("https://web.whatsapp.com/")
print("Please scan the QR Code from the number you would like the bot to be on")
sleep(5)

def choose():
    sleep(0.1)
    nums_xpath = '//*[@id="main"]/header/div[2]/div[2]/span'
    a = driver.find_elements_by_xpath(nums_xpath)[0].text
    a.lstrip()
    ls = a.split(',')
    for s in ls:
        s.lstrip()
    del ls[-1]
    return '@' + rn.choice(ls).strip() + Keys.ENTER + ', I choose you! \n'


while True:
    # The green dot tells us that the message is new
    unread = driver.find_elements_by_class_name("OUeyt")
    name, message = '', ''
    if len(unread) > 0:
        ele = unread[-1]
        action = webdriver.common.action_chains.ActionChains(driver)
        # move a bit to the left from the green dot
        action.move_to_element_with_offset(ele, 0, -20)

        try:
            action.click()
            action.perform()
            action.click()
            action.perform()
        except Exception as e:
            pass
        try:
            # TODO: Find Contact name without using class
            name = driver.find_element_by_class_name(
                "_3XrHh").text  # Contact name
            # TODO: Find Message name without using class
            message = driver.find_elements_by_class_name(
                "_3FXB1")[-1]  # the message content
            inp_xpath = "(//div[@contenteditable='true'])[2]"
            text_box = wait.until(
                EC.presence_of_element_located((By.XPATH, inp_xpath)))

            message_content = message.text.lower()
            if message_content == '$choose':
                text_box.send_keys(choose() + '\n')
            if message_content[0] == "$":
                response = func.fcommand(message_content)
                text_box.send_keys(response)
        except Exception as e:
            traceback.print_exc()
            pass

        # Go To Empty Chat so that there are unread messages
        x_arg = '//span[contains(@title,' + '"ASDFGHJKL"' + ')]'
        driver.find_element_by_xpath(x_arg).click()
    sleep(1)
