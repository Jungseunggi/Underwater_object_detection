import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib
from urllib import request

fish_list = ['Giant oarfish']


for keyword in fish_list:
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent', 'Chrome/36.0.1941.0')]
    urllib.request.install_opener(opener)


    # driver path, get url
    driver = webdriver.Chrome('chromedriver_mac64_m1/chromedriver')
    driver.get('https://www.google.co.kr/imghp?hl=ko')

    # input key word
    # keyword = input('Key Word: ')

    elem = driver.find_element(By.NAME, 'q')
    elem.send_keys(keyword)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_SEC = 1

    # 스크롤 높이 가져옴
    last_height = driver.execute_script("return document.body.scrollHeight")

    scroll_count = 1
    while scroll_count < 21:
        # 끝까지 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 1초 대기
        time.sleep(SCROLL_PAUSE_SEC)

        # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            try:
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except:
                break
        last_height = new_height
        scroll_count += 1


    images = driver.find_elements(By.CSS_SELECTOR, '.rg_i.Q4LuWd')

    count = 1
    for image in images:
        count += 1
        print(count)
        
        # 이미지 url
        img = image.get_attribute("data-src")
        if img is None:
            img = image.get_attribute("src")
        print(img)
        
        if not os.path.exists('data'):
            os.mkdir('data')
        if not os.path.exists('data/' + keyword):
            os.mkdir('data/' + keyword)
        succounter = 1
        try:
            raw_img = urllib.request.urlopen(img).read()
            File = open(os.path.join('data/' + keyword, keyword + "_" + str(count) + "." + 'jpg'), "wb")
            File.write(raw_img)
            File.close()
            succounter += 1
        except:
            print('error')

    print(succounter, "succesfully downloaded")
    driver.close()
