import requests
import bs4
from time import sleep
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def get_tiktok_hashtags(entity):
    try:
        url = f"https://tiktokhashtags.com/hashtag/{entity}/"

        data = requests.get(url, headers=headers)
        sleep(3)

        soup = bs4.BeautifulSoup(data.text,'lxml')


        hashtags_1 = soup.find_all("p1")[0].text
        hashtags_2 = soup.find_all("p2")[0].text

        #split string of hastags to have a list of hashtags
        hashtags_1 = hashtags_1.split("#")
        hashtags_2 = hashtags_2.split("#")

        ## attach the # symbol
        hashtags_1 = ["#"+a for a in hashtags_1[1:]]
        hashtags_2 = ["#"+a for a in hashtags_2[1:]]

        ## merge both sections anf strip white spaces
        hashtags = hashtags_1 + hashtags_2
        hashtags = [item.strip() for item in hashtags]
        
    except:
        hashtags = []

    
    return hashtags


