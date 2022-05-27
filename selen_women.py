from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time



def women():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get("https://damn.ru/")
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[1]/form/div/div/button").click()
    driver.find_element(by=By.CSS_SELECTOR,
                        value="body > div:nth-child(4) > div > div > div.row > div.col-xs-12.col-md-8 > form > div > div > ul > li:nth-child(2) > a").click()
    search = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[1]/form/div/input")
    time.sleep(1)
    search.send_keys("Ты")
    time.sleep(1)
    driver.find_element(by=By.CSS_SELECTOR,
                        value="body > div:nth-child(4) > div > div > div.row > div.col-xs-12.col-md-8 > form > button").click()
    search2 = driver.find_element(by=By.CSS_SELECTOR,
                                  value="body > div:nth-child(4) > div > div > div.row > div.col-xs-12.col-md-8 > div.damn")

    print(search2.text)


    return search2.text

if __name__ == "__main__":
    women()
