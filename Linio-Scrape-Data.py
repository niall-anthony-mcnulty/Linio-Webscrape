
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import datetime


# ---------------------- loop through website for individual URLS ------------------- #
# ----------------------------------------------------------------------------------- #

#url based off page number
pageno = 1

# list of urls
urls = []
titles = []
delivery_fees = []
degrees = []
prices = []
original_prices = []
coupon_codes = []
user_names = [] 
dates = []

# loop through pages until pages run out
while pageno < 4:


    try:

        baseurl = "https://www.promodescuentos.com/search?q=linio&page=" + str(pageno)
         

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

       

        ## Using requests module ##
        try:
            r = requests.get(baseurl, cookies=cookies, headers=headers, allow_redirects=True)
            # print(r)

        except Exception as e:
            print(f'Error caught for request: {e}')
            

        # request page and soupify
        try:
            soup = BeautifulSoup(r.text.encode('utf-8'), 'lxml')
            # print(soup.original_encoding)
            # print(soup)

        except Exception as e:
            print(f'Error caught for soup: {e}')


        # Check for all the post on the page
        try:
            product_tags = soup.find_all("div", {"class": "threadGrid"}) 
            

        except Exception as e:
            print(f'Error caught for find_all: {e}')

        
        #### Only start from index 1 on page 1 because the top tab is irrelevant. ####
        if pageno == 1:
            
            try:
                # scrape through each items div tag
                for tags in product_tags[1:]:

                     # search for urls
                    try:
                        href = tags.find('a',{'class':'thread-title--list'})['href']
                        urls.append(href)
                    
                    except Exception as e:
                        print(f'issue finding the url: {e}')

                    # search for title
                    try:
                        title = tags.find('a',{'class':'thread-title--list'})['title']
                        titles.append(title)
                    
                    except Exception as e:
                        print(f'issue finding title: {e}')


                    # search for free delivery

                    try:
                        
                        if tags.find('span',{'class' : "cept-shipping-price"}):
                            try:
                                delivery_fee = tags.find('span',{'class' : "cept-shipping-price"})
                                # if there are 2 child spans, the delivery is free
                                children = delivery_fee.findChildren("span", recursive=False)
                                
                                if len(children) > 1:
                                    delivery_fees.append('Free')
                                else:
                                    delivery_fee = re.sub('[^0-9]', '', delivery_fee.string)
                                    delivery_fees.append(delivery_fee)
                            except Exception as e:
                                print(f'issue finding delivery fee tag: {e}')
                        else:
                            # if no span tag is found with the class name, sub None
                            delivery_fees.append(None)

                        
                    except Exception as e:
                        print(f'issues finding delivery fee: {e}')
                        
                    # search for degrees 

                    try:  
                        # find span tags with degree string inside
                        degree = tags.find('span', class_ =['cept-vote-temp','space--h-2 text--b']).string
                        # remove trailing and proceeding whitespace plus degree sign
                        degree = re.sub('[^-?0-9]', '', degree)
                        degrees.append(degree)
                    except Exception as e:
                        print(f'issue finding degrees: {e}')
                        # append None if an issue arises
                        degrees.append(None)
                        continue
                        

                    # search for prices

                    try:
                        if tags.find('span',{'class' : "thread-price"}):
                            try:
                                final_price = tags.find('span',{'class' : "thread-price"}).string
                            except Exception as e:
                                print(f'issue finding final price: {e}')
                            
                            # return only digits (take out special characters to ensure int datatype)
                            final_price = re.sub('[^0-9-?]', '', final_price)
                            negative = '-'
                            if negative in final_price:
                                prices.append('Coupon')
                            else:
                                prices.append(int(final_price))
                        else:
                            prices.append('Coupon')
                    except Exception as e:
                        print(f'issues adding prices')
                        prices.append(None)

                    # search for original prices

                    try:
                        if tags.find('span',{'class' : "cept-next-best-price"}):
                            try:
                                final_original_price = tags.find('span',{'class' : "cept-next-best-price"}).string
                                final_original_price = re.sub('[^0-9-?]', '', final_original_price)
                                original_prices.append(int(final_original_price))
                            except Exception as e:
                                print(f'issue finding final original price: {e}')
                        # if no span tag is found with the class name, then there was no original price
                        else:
                            original_prices.append(None)

                    
                    except Exception as e:
                        print(f'issues adding prices')
                        original_prices.append(None)
                        continue

                    # search for coupon codes

                    try:
                        if tags.find('input',{'class':'cept-voucher-button-code'}):
                            try:
                                voucher = tags.find('input',{'class':'cept-voucher-button-code'})['value']
                            except Exception as e:
                                print(f'issues finding the coupon code: {e}')
                            # append to list
                            coupon_codes.append(voucher)
                        else:
                            coupon_codes.append(None)
                    
                    except Exception as e:
                        print(f'issues searching for the coupon codes: {e}')

                    # search for user_names

                    try: 
                        username = tags.find('span',{'class' : "thread-username"}).string
                        username = re.sub('[\s*$]', '', username)
                        user_names.append(username)

                    except Exception as e:
                        print(f'Issues finding user_names: {e}')
                        user_names.append(None)

                    # search for post dates
                                
                    try:
                
                        
                        # check for the clock or refresh icon and then the next span tag down - get text
                        if tags.find("svg",{"class" :"icon icon--clock text--color-greyShade space--mr-1"}):
                            date_of_pub = tags.find("svg",{"class" :"icon icon--clock text--color-greyShade space--mr-1"})
                            date_of_pub = date_of_pub.find_next("span")
                        
                            # remove unwanted text via regex
                            date_of_pub = re.sub('Actualizado', '', date_of_pub.string)
                            
                        
                        elif tags.find("svg",{"class":"icon icon--refresh text--color-greyShade space--mr-1"}):
                            date_of_pub = tags.find("svg",{"class" :"icon icon--refresh text--color-greyShade space--mr-1"})
                            date_of_pub = date_of_pub.find_next("span")

                            date_of_pub = re.sub('Actualizado', '', date_of_pub.string)
                            
                        # if length is greater than 10, input 'abr 19º - current date in Spanish'
                        if len(date_of_pub) > 10:
                            date_of_pub = 'abr 19º' 

                        #check for string year
                        substring_year = '2021'
                        # current year
                        current_year = str(datetime.datetime.now().year)
                        # if it does have the year, append
                        if substring_year in date_of_pub:
                            date_of_pub = re.sub('^[ \t]+', '', date_of_pub)
                            dates.append(date_of_pub)
                        else:
                            # if it doesn't, concatenate year then append
                            date_of_pub = re.sub('^[ \t]+', '', date_of_pub) + ' ' +  current_year
                            dates.append(date_of_pub)


                    except Exception as e:
                        print(f'issues finding dates')
                        dates.append(None)
        
            
            except Exception as e:
                print(f'Failure to scrape details from div tag: {e}')
        
        #### From page 2 onwards, every tab is consider ####
        else:

            try:
                # scrape through each items div tag
                for tags in product_tags:

                    # search for urls
                    try:
                        href = tags.find('a',{'class':'thread-title--list'})['href']
                        urls.append(href)
                    
                    except Exception as e:
                        print(f'issue finding the url: {e}')

                    # search for title
                    try:
                        title = tags.find('a',{'class':'thread-title--list'})['title']
                        titles.append(title)
                    
                    except Exception as e:
                        print(f'issue finding title: {e}')


                    # search for free delivery

                    try:
                        
                        if tags.find('span',{'class' : "cept-shipping-price"}):
                            try:
                                delivery_fee = tags.find('span',{'class' : "cept-shipping-price"})
                                # if there are 2 child spans, the delivery is free
                                children = delivery_fee.findChildren("span", recursive=False)
                                
                                if len(children) > 1:
                                    delivery_fees.append('Free')
                                else:
                                    delivery_fee = re.sub('[^0-9]', '', delivery_fee.string)
                                    delivery_fees.append(delivery_fee)
                            except Exception as e:
                                print(f'issue finding delivery fee tag: {e}')
                        else:
                            # if no span tag is found with the class name, sub None
                            delivery_fees.append(None)

                        
                    except Exception as e:
                        print(f'issues finding delivery fee: {e}')
                        
                    # search for degrees 

                    try:  
                        # find span tags with degree string inside
                        degree = tags.find('span', class_ =['cept-vote-temp','space--h-2 text--b']).string
                        # remove trailing and proceeding whitespace plus degree sign
                        degree = re.sub('[^-?0-9]', '', degree)
                        degrees.append(degree)
                    except Exception as e:
                        print(f'issue finding degrees: {e}')
                        # append None if an issue arises
                        degrees.append(None)
                        continue
                        

                    # search for prices

                    try:
                        if tags.find('span',{'class' : "thread-price"}):
                            try:
                                final_price = tags.find('span',{'class' : "thread-price"}).string
                            except Exception as e:
                                print(f'issue finding final price: {e}')
                            
                            # return only digits (take out special characters to ensure int datatype)
                            final_price = re.sub('[^0-9-?]', '', final_price)
                            negative = '-'
                            if negative in final_price:
                                prices.append('Coupon')
                            else:
                                prices.append(int(final_price))
                        else:
                            prices.append('Coupon')
                    except Exception as e:
                        print(f'issues adding prices')
                        prices.append(None)

                    # search for original prices

                    try:
                        if tags.find('span',{'class' : "cept-next-best-price"}):
                            try:
                                final_original_price = tags.find('span',{'class' : "cept-next-best-price"}).string
                                final_original_price = re.sub('[^0-9-?]', '', final_original_price)
                                original_prices.append(int(final_original_price))
                            except Exception as e:
                                print(f'issue finding final original price: {e}')
                        # if no span tag is found with the class name, then there was no original price
                        else:
                            original_prices.append(None)

                    
                    except Exception as e:
                        print(f'issues adding prices')
                        original_prices.append(None)
                        continue

                    # search for coupon codes

                    try:
                        if tags.find('input',{'class':'cept-voucher-button-code'}):
                            try:
                                voucher = tags.find('input',{'class':'cept-voucher-button-code'})['value']
                            except Exception as e:
                                print(f'issues finding the coupon code: {e}')
                            # append to list
                            coupon_codes.append(voucher)
                        else:
                            coupon_codes.append(None)
                    
                    except Exception as e:
                        print(f'issues searching for the coupon codes: {e}')

                    # search for user_names

                    try: 
                        username = tags.find('span',{'class' : "thread-username"}).string
                        username = re.sub('[\s*$]', '', username)
                        user_names.append(username)

                    except Exception as e:
                        print(f'Issues finding user_names: {e}')
                        user_names.append(None)

                    # search for post dates
                                
                    try:
                
                        # check for the clock or refresh icon and then the next span tag down - get text
                        if tags.find("svg",{"class" :"icon icon--clock text--color-greyShade space--mr-1"}):
                            date_of_pub = tags.find("svg",{"class" :"icon icon--clock text--color-greyShade space--mr-1"})
                            date_of_pub = date_of_pub.find_next("span")
                            
                            # get rid of unwanted text using regex
                            date_of_pub = re.sub('Actualizado', '', date_of_pub.string)
                            
                        
                        elif tags.find("svg",{"class":"icon icon--refresh text--color-greyShade space--mr-1"}):
                            date_of_pub = tags.find("svg",{"class" :"icon icon--refresh text--color-greyShade space--mr-1"})
                            date_of_pub = date_of_pub.find_next("span")

                            date_of_pub = re.sub('Actualizado', '', date_of_pub.string)
                            
                        # if length is greater than 10, input 'abr 19º - current date in Spanish'
                        if len(date_of_pub) > 10:
                            date_of_pub = 'abr 19º' 

                        #check for string year
                        substring_year = '2021'
                        # current year
                        current_year = str(datetime.datetime.now().year)
                        # if it does have the year, append
                        if substring_year in date_of_pub:
                            date_of_pub = re.sub('^[ \t]+', '', date_of_pub)
                            dates.append(date_of_pub)
                        else:
                            # if it doesn't, concatenate year then append
                            date_of_pub = re.sub('^[ \t]+', '', date_of_pub) + ' ' +  current_year
                            dates.append(date_of_pub)
                        
                       

                    except Exception as e:
                        print(f'issues finding dates')
                        dates.append(None)
            
            except Exception as e:
                print(f'Failure to scrape details from div tag: {e}')


    except Exception as e:
        print(f'Issue running the entire code through multiple pages: {e}')
        continue
    
    pageno += 1  

    
# save to pd.Dataframe

data_dict = {'Titles':titles, 'Degrees':degrees, 'Dates': dates,'Final_Price':prices,'Original_Price':original_prices, 'urls':urls, 'Delivery_Fees':delivery_fees,'Coupon_Codes':coupon_codes, 'Username':user_names}
df_linio_data = pd.DataFrame.from_dict(data_dict)



def date_correction(col):

    # split the string to erase weird symbol
    new_date =  str(col).split("º.")
    # join them back together
    new_date_2 = ",".join(new_date)
    # return without trailing white space
    return new_date_2.rstrip()
                                                    

# ----------------------------------------------------------------------------------- #
# ---------------------------- Translate Month Sring -------------------------------- # 
def month_translation(col):
    if 'ene' in col:
        return col.replace('ene','January')
    elif 'feb' in col:
        return col.replace('feb','February')
    elif 'mar' in col:
        return col.replace('mar','March')
    elif 'abr' in col:
        return col.replace('abr','April')
    elif 'may' in col:
        return col.replace('may', 'May')
    elif 'jun' in col:
        return col.replace('jun','June')
    elif 'jul' in col:
        return col.replace('jul','July')
    elif 'ago' in col:
        return col.replace('ago','August')
    elif 'sep' in col:
        return col.replace('sep','September')
    elif 'oct' in col:
        return col.replace('oct', 'October')
    elif 'nov' in col:
        return col.replace('nov','November')
    elif 'dic' in col:
        return col.replace('dic','December')
    else:
        return col


# ----------------------------------------------------------------------------------- #
# ------------------------ Change String to Datetime -------------------------------- # 
def date_time(col):
    try:
        return datetime.strptime(col, "%B %d, %Y")
    except:
        return pd.NaT

# ----------------------------------------------------------------------------------- #
# ------------------------ Call Functions & Save to Excel --------------------------- # 


# fix date
try:

# remove symbol
    df_linio_data['Dates'] = df_linio_data.apply(lambda x: date_correction(x['Dates']), axis = 1 )

# translate month
    df_linio_data['Dates'] = df_linio_data.apply(lambda x: month_translation(x['Dates']), axis = 1 )

# apply datetime format
    df_linio_data['Dates'] = df_linio_data.apply(lambda x: date_time(x['Dates']), axis = 1 )
except:
    print('could not convert data')


df_linio_data.index += 1

# print(df_linio_data)

# # save to csv

df_linio_data.to_csv('linio_data-oct-date.csv', sep=',', index=False)



# # ----------------------------------------------------------------------------------- #
