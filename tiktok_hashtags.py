from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--headless')


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def start_browser():
    '''This connects to the chromedriver path and opens the search url'''

    ## change this to the ubuntu path
    PATH = '/Users/hp/Desktop/Chrome Driver/chromedriver.exe'
    driver = webdriver.Chrome(PATH, options=options)

    site_url = "https://tiktokhashtags.com/"
    driver.get(site_url)
    sleep(3)
    
    return driver


def get_tiktok_hashtags(entity):
    
    try:

        driver = start_browser()
        search = driver.find_element_by_name("h")
        search.send_keys(entity)
        search.send_keys(Keys.RETURN)
        sleep(3)

        ##finds first hastags section
        hashtags_1 = driver.find_element_by_tag_name('p1').text

        ##finds second hastags section
        hashtags_2 = driver.find_element_by_tag_name('p2').text

        #split string of hastags to have a list of hashtags
        hashtags_1 = hashtags_1.split("#")
        hashtags_2 = hashtags_2.split("#")

        ## attach the # symbol
        hashtags_1 = ["#"+a for a in hashtags_1[1:]]
        hashtags_2 = ["#"+a for a in hashtags_2[1:]]

        ## merge both sections anf strip white spaces
        hashtags = hashtags_1 + hashtags_2
        hashtags = [item.strip() for item in hashtags]

        driver.quit()
    except:
        hashtags = []
    
    return hashtags


entity = "#ball"
a = get_tiktok_hashtags(entity)
print(a)