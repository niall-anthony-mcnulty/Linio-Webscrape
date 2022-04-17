
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




# ---------------------- loop through website for individual URLS ------------------- #
# ----------------------------------------------------------------------------------- #

#url based off page number
pageno = 1

# list of urls
arr_url  = []

# loop through pages until pages run out
# while pageno < 2100:
while pageno < 2:
    

    baseurl = "https://www.promodescuentos.com/nuevas?page=" + str(pageno)

     ###------- Local Driver --------###
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

    cookies = {
    'f_v': '%2277923700-bda4-11ec-bc7c-0242ac110002%22',
    '_ga': 'GA1.3.2004119577.1650127509',
    '_gid': 'GA1.3.661803659.1650127509',
    '_hjid': 'ae0f1ed2-2d92-4f09-bf43-c7bc66931033',
    '_hjSessionUser_2633550': 'eyJpZCI6IjQ1OTZkNzZkLTAzODItNTQ0ZC05N2ZlLTI1OGMxNjQ3NzIxYyIsImNyZWF0ZWQiOjE2NTAxMjc1MTEzNDcsImV4aXN0aW5nIjp0cnVlfQ==',
    'browser_push_permission_requested': '1650127629',
    'remember_6fc0f483e7f442dc50848060ae780d66': '%22778370%7CXrIutHkF0kW4HvN6kagIuDIqsQmOzP4HwyizQpKc3jl642wfYMc55YZfHmph%7C%242y%2410%24UCA2KfcAHkp28h5luvz69eim1o4ljCHTkbPNiE.Gm%5C%2FdRld.JuV4ei%22',
    'show_my_tab': '0',
    '__gads': 'ID=67fc807648eb07a2:T=1650128435:S=ALNI_MZRDyw778Xbe6t4jAm1aIQRRTAeDQ',
    'hide_price_comparison': 'false',
    'sort_by': '%22relevance%22',
    'q': '%22linio%22',
    'hide_local': 'true',
    'hide_deleted': 'false',
    'hide_moderated': 'true',
    'hide_admin_tools_on_list_view': '0',
    'view_layout_horizontal': '%221-1%22',
    'hide_expired': '%221%22',
    'time_frame': '%220%22',
    'hide_clearance': '%220%22',
    'hide_nsfw': '%220%22',
    'pepper_session': '%220cZRBfki3lY1gaNa2Z18lQG1KrlsVF0Rur4yt6s8%22',
    'xsrf_t': '%22tGzXKYeskT6DKV1mIBMpDI4e8XlOnh5oFZVnAxMq%22',
    '__gpi': 'UID=00000434c390f13f:T=1650128435:RT=1650183326:S=ALNI_MY3xoVKqiN7mGjrdIS1jkd8wY7ijg',
    '_hjSession_2633550': 'eyJpZCI6IjE1NjRhNjA4LTQ4NTQtNDg4MS05MzVjLTMyODZhNDI4M2YwOCIsImNyZWF0ZWQiOjE2NTAxODMzMjY5MTgsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjAbsoluteSessionInProgress': '1',
    'u_l': '1',
    '_gat': '1',
    '_hjIncludedInSessionSample': '0',
    'navi': '%7B%22homepage%22%3A%22nuevas%22%7D',
    'ab.storage.sessionId.7af503ae-0c84-478f-98b0-ecfff5d67750': '%7B%22g%22%3A%226b6610eb-9a5d-5719-499c-6571b7fa98c8%22%2C%22e%22%3A2150186346322%2C%22c%22%3A1634794497601%2C%22l%22%3A1650186346322%7D',
    }

    headers = {
    'authority': 'www.promodescuentos.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'f_v=%2277923700-bda4-11ec-bc7c-0242ac110002%22; _ga=GA1.3.2004119577.1650127509; _gid=GA1.3.661803659.1650127509; _hjid=ae0f1ed2-2d92-4f09-bf43-c7bc66931033; _hjSessionUser_2633550=eyJpZCI6IjQ1OTZkNzZkLTAzODItNTQ0ZC05N2ZlLTI1OGMxNjQ3NzIxYyIsImNyZWF0ZWQiOjE2NTAxMjc1MTEzNDcsImV4aXN0aW5nIjp0cnVlfQ==; browser_push_permission_requested=1650127629; remember_6fc0f483e7f442dc50848060ae780d66=%22778370%7CXrIutHkF0kW4HvN6kagIuDIqsQmOzP4HwyizQpKc3jl642wfYMc55YZfHmph%7C%242y%2410%24UCA2KfcAHkp28h5luvz69eim1o4ljCHTkbPNiE.Gm%5C%2FdRld.JuV4ei%22; show_my_tab=0; __gads=ID=67fc807648eb07a2:T=1650128435:S=ALNI_MZRDyw778Xbe6t4jAm1aIQRRTAeDQ; hide_price_comparison=false; sort_by=%22relevance%22; q=%22linio%22; hide_local=true; hide_deleted=false; hide_moderated=true; hide_admin_tools_on_list_view=0; view_layout_horizontal=%221-1%22; hide_expired=%221%22; time_frame=%220%22; hide_clearance=%220%22; hide_nsfw=%220%22; pepper_session=%220cZRBfki3lY1gaNa2Z18lQG1KrlsVF0Rur4yt6s8%22; xsrf_t=%22tGzXKYeskT6DKV1mIBMpDI4e8XlOnh5oFZVnAxMq%22; __gpi=UID=00000434c390f13f:T=1650128435:RT=1650183326:S=ALNI_MY3xoVKqiN7mGjrdIS1jkd8wY7ijg; _hjSession_2633550=eyJpZCI6IjE1NjRhNjA4LTQ4NTQtNDg4MS05MzVjLTMyODZhNDI4M2YwOCIsImNyZWF0ZWQiOjE2NTAxODMzMjY5MTgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; u_l=1; _gat=1; _hjIncludedInSessionSample=0; navi=%7B%22homepage%22%3A%22nuevas%22%7D; ab.storage.sessionId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%226b6610eb-9a5d-5719-499c-6571b7fa98c8%22%2C%22e%22%3A2150186346322%2C%22c%22%3A1634794497601%2C%22l%22%3A1650186346322%7D',
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

    r = requests.get(baseurl, headers=headers).text
    # request page and soupify
    soup = BeautifulSoup(r, 'html.parser')
    print(soup)
    
    
    
    try:
        # Check all the products for their titles
        all_products = soup.find_all("a",{"class": "thread-link"})
        print(all_products)
        

        for products in all_products[:]:
            # product_title = products.find("a").text
            # 
            print(products)
            
        
            
        #     # if the title starts with Linio add the url to the url list
        #     # if product_title.startswith("Linio:"):
        #     #     print('Yes')
        #     product_url = products.find("a", {"class": "thread-link"},href=True)
        #     print(product_url)
        #     arr_url.append(product_url['href'])
        
            

    except:
        continue
    
    # increment pageno by 1
    pageno += 1

print(all_products)
# store urls
df = pd.DataFrame(arr_url, columns = ['urls'])


# save to csv - Save to your own directory

# df.to_csv("/Users/Niall-McNulty/Desktop/Linio\ Webscrape/linio_urls-oct21-date.csv", index = False)


# ----------------------------------------------------------------------------------- #
