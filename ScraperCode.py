from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import json
from selenium.webdriver.common.keys import Keys


def perform():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://summerofcode.withgoogle.com/programs/2022/organizations")

    driver.implicitly_wait(10)
    data = {}
    while True:
        orgs = driver.find_elements(by=By.CLASS_NAME, value="content")
        for org in orgs:
            org_url = org.get_attribute("href")
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(org_url)
            driver.implicitly_wait(10)

            title = driver.find_element(by=By.CLASS_NAME, value="title")
            tech = driver.find_element(by=By.CLASS_NAME, value="tech__content")
            topic = driver.find_element(by=By.CLASS_NAME, value="topics__content")
            desc = driver.find_element(by=By.CLASS_NAME, value="bd")
            data[title.text] = {"tech":tech.text, "topic":topic.text, "desc":desc.text}
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        nxt = driver.find_element(by=By.CLASS_NAME, value="mat-paginator-navigation-next")
        try:
            nxt.send_keys(Keys.RETURN)
        except:
            break

    with open("sample.json", "w", indent =4 ) as outfile:
        json.dump(data, outfile) 
    


perform() 
