from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 
import requests

# target = '%27dirty%27+solar+panel'
# url = 'https://www.google.com/search?q='+ target +'&hl=EN&tbm=isch'

url = 'https://www.google.com/search?q=dust%2Bsolar%2Bpanel+-dirty&tbm=isch&ved=2ahUKEwiWnLK6lbP8AhXMD94KHZhVABAQ2-cCegQIABAA&oq=dust%2Bsolar%2Bpanel+-dirty&gs_lcp=CgNpbWcQA1DvBVijMmDpNGgAcAB4AIABMogBrwKSAQE3mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=5DG4Y5aaHcyf-AaYq4GAAQ&hl=EN'
class Crawler_google_images:
    def __init__(self):
        self.url = url

    def init_browser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-infobars')
        browser = webdriver.Chrome(options = chrome_options)

        browser.get(self.url)
        browser.maximize_window()
        return browser
    
    def download_images(self, browser, round = 10):
        picpath = './Dusty'
        if not os.path.exists(picpath): os.makedirs(picpath)
        img_url_dic = []

        count = 0
        pos = 0

        for i in range(round):
            pos += 500
            js = 'var q=document.documentElement.scrollTop=' + str(pos)
            browser.execute_script(js)
            time.sleep(1)

            img_elements = browser.find_elements(By.CLASS_NAME,'rg_i')

            for img_element in img_elements:
                img_url = img_element.get_attribute('src')

                if isinstance(img_url, str):
                    if len(img_url) <= 200:
                        if 'images' in img_url:
                            if img_url not in img_url_dic:
                                # print(img_url)
                                try:
                                    img_url_dic.append(img_url)
                                    filename = "./Dusty/" + str(count) + ".jpg"
                                    r = requests.get(img_url)
                                    with open(filename, 'wb') as f:
                                        f.write(r.content)
                                    f.close()
                                    count += 1
                                    print('this is ' + str(count) + 'st img')
                                    time.sleep(0.5)
                                except:
                                    print('failure')
    def run(self):
        self.__init__()
        browser = self.init_browser()
        self.download_images(browser, 1000)
        browser.close()
        print('Crawlering Done.')

if __name__ == '__main__':
    craw = Crawler_google_images()
    craw.run()

