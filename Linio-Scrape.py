
from quopri import encodestring
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import pprint
from datetime import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import Request, urlopen




# ---------------------- loop through website for individual URLS ------------------- #
# ----------------------------------------------------------------------------------- #

#url based off page number
pageno = 1

# list of urls
arr_url  = []

# loop through pages until pages run out
# while pageno < 2100:
# while pageno < 2:
    

baseurl = "https://www.promodescuentos.com/search?"

     ###------- Local Driver - SELENIUM --------###
    # DRIVER_PATH = '/Users/Niall-McNulty/Desktop/Computer Science Projects:Courses/chromedriver 2'
    # # add headless mode
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Runs Chrome in headless mode.
    # options.add_argument("--disable-gpu")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument('--no-sandbox') # Bypass OS security model
    # driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    # driver.implicitly_wait(0.5)
    # driver.get(baseurl)

    # #find strong element
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cept-tt.thread-link.linkPlain.thread-title--list")))
    # html_source = driver.execute_script("return document.getElementsByClassName('.cept-tt.thread-link.linkPlain.thread-title--list')")
    # print(html_source)
    # # print(html_source)
    # time.sleep(2)

# https://curlconverter.com/ for below

cookies = {
    'view_layout_horizontal': '%221-1%22',
    'show_my_tab': '0',
    'f_v': '%22f30aeb80-be6b-11ec-9c55-0242ac110002%22',
    'ab.storage.deviceId.7af503ae-0c84-478f-98b0-ecfff5d67750': '%7B%22g%22%3A%22e483658a-4c36-5113-5789-e5fef7db37d8%22%2C%22c%22%3A1650212751287%2C%22l%22%3A1650213141423%7D',
    'ab.storage.userId.7af503ae-0c84-478f-98b0-ecfff5d67750': '%7B%22g%22%3A%22browser-1626960373888-6%22%2C%22c%22%3A1650213141417%2C%22l%22%3A1650213141424%7D',
    '_ga': 'GA1.3.1063370061.1650213142',
    '_gid': 'GA1.3.699127627.1650213142',
    '__gads': 'ID=da8f986b5b80ce28:T=1650213149:S=ALNI_MZznS9iFCCGedhCza9AuzZ2RWx8Og',
    '_hjSessionUser_2633550': 'eyJpZCI6IjI3MjgxMzRlLTEzODAtNTNmMC05ZTEwLTkzYjVkZTAzZDYyYiIsImNyZWF0ZWQiOjE2NTAyMTMxNDk5NzQsImV4aXN0aW5nIjp0cnVlfQ==',
    'browser_push_permission_requested': '1650213164',
    'navi': '%7B%22homepage%22%3A%22nuevas%22%7D',
    '__gpi': 'UID=000004e4fdd1d97f:T=1650213149:RT=1650268456:S=ALNI_Mbv6l7NuTOyLT5hgjDgAAFeJfFaFQ',
    'hide_expired': '%220%22',
    'hide_price_comparison': 'false',
    'time_frame': '%220%22',
    'sort_by': '%22new%22',
    'q': '%22linio%22',
    'hide_local': '%220%22',
    'hide_clearance': '%220%22',
    'hide_deleted': 'false',
    'hide_moderated': 'true',
    'pepper_session': '%22NKEv8RxiRnEFhIVGakVg2kMHuscnpaxhKN25EuWf%22',
    'u_l': '0',
    'xsrf_t': '%22zIaDuifmEuoINaxwXiL1s8cfINLrIZ792dRdu5UD%22',
    'ab.storage.sessionId.7af503ae-0c84-478f-98b0-ecfff5d67750': '%7B%22g%22%3A%229fb2a7f2-b95c-d1f5-055c-0a47edd0f8a3%22%2C%22e%22%3A2150273480865%2C%22c%22%3A1650213141421%2C%22l%22%3A1650273480865%7D',
    '_hjIncludedInSessionSample': '0',
    '_hjSession_2633550': 'eyJpZCI6IjYyYWMyNTQ5LWJiNzAtNDFiNy05ODE5LWQyYjRlODRlYWJiYiIsImNyZWF0ZWQiOjE2NTAyNzM0ODM5ODQsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '0',
}

headers = {
    'authority': 'www.promodescuentos.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'view_layout_horizontal=%221-1%22; show_my_tab=0; f_v=%22f30aeb80-be6b-11ec-9c55-0242ac110002%22; ab.storage.deviceId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22e483658a-4c36-5113-5789-e5fef7db37d8%22%2C%22c%22%3A1650212751287%2C%22l%22%3A1650213141423%7D; ab.storage.userId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22browser-1626960373888-6%22%2C%22c%22%3A1650213141417%2C%22l%22%3A1650213141424%7D; _ga=GA1.3.1063370061.1650213142; _gid=GA1.3.699127627.1650213142; __gads=ID=da8f986b5b80ce28:T=1650213149:S=ALNI_MZznS9iFCCGedhCza9AuzZ2RWx8Og; _hjSessionUser_2633550=eyJpZCI6IjI3MjgxMzRlLTEzODAtNTNmMC05ZTEwLTkzYjVkZTAzZDYyYiIsImNyZWF0ZWQiOjE2NTAyMTMxNDk5NzQsImV4aXN0aW5nIjp0cnVlfQ==; browser_push_permission_requested=1650213164; navi=%7B%22homepage%22%3A%22nuevas%22%7D; __gpi=UID=000004e4fdd1d97f:T=1650213149:RT=1650268456:S=ALNI_Mbv6l7NuTOyLT5hgjDgAAFeJfFaFQ; hide_expired=%220%22; hide_price_comparison=false; time_frame=%220%22; sort_by=%22new%22; q=%22linio%22; hide_local=%220%22; hide_clearance=%220%22; hide_deleted=false; hide_moderated=true; pepper_session=%22NKEv8RxiRnEFhIVGakVg2kMHuscnpaxhKN25EuWf%22; u_l=0; xsrf_t=%22zIaDuifmEuoINaxwXiL1s8cfINLrIZ792dRdu5UD%22; ab.storage.sessionId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%229fb2a7f2-b95c-d1f5-055c-0a47edd0f8a3%22%2C%22e%22%3A2150273480865%2C%22c%22%3A1650213141421%2C%22l%22%3A1650273480865%7D; _hjIncludedInSessionSample=0; _hjSession_2633550=eyJpZCI6IjYyYWMyNTQ5LWJiNzAtNDFiNy05ODE5LWQyYjRlODRlYWJiYiIsImNyZWF0ZWQiOjE2NTAyNzM0ODM5ODQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

params = {
    'q': 'linio',
    'page' : '{pageno}'
}

## Using requests module ##
try:
    r = requests.get(baseurl, cookies=cookies, headers=headers, params=params, allow_redirects=True)
    print(r)

except Exception as e:
    print(f'Error caught for request: {e}')
    

# request page and soupify
try:
    soup = BeautifulSoup(r.text.encode('utf-8'), 'html.parser')
    print(soup.original_encoding)
    # print(soup)

except Exception as e:
    print(f'Error caught for soup: {e}')


    # Check all the products for their titles
try:
    link_tags = soup.find_all("a",{"class": "thread-title--list"})
    print(link_tags)  

except Exception as e:
    print(f'Error caught for find_all: {e}')

print(len(link_tags))



list_titles = []
try:
    for products in link_tags:
        try:
            product_title = products.string
            if product_title is None:
                list_titles.append(None)
            else:
                list_titles.append(product_title)
        except Exception as e:
            print(f'Issue with finding text: {e}')
    
    print(list_titles)

except Exception as e:
    print('f Returning text from list of a tags: {e}')

        
        
            
        #     # if the title starts with Linio add the url to the url list
        #     # if product_title.startswith("Linio:"):
        #     #     print('Yes')
        #     product_url = products.find("a", {"class": "thread-link"},href=True)
        #     print(product_url)
        #     arr_url.append(product_url['href'])
        
            

#     except:
#         continue
    
#     # increment pageno by 1
#     pageno += 1

# print(all_products)
# # store urls
# df = pd.DataFrame(arr_url, columns = ['urls'])


# save to csv - Save to your own directory

# df.to_csv("/Users/Niall-McNulty/Desktop/Linio\ Webscrape/linio_urls-oct21-date.csv", index = False)


# ----------------------------------------------------------------------------------- #
