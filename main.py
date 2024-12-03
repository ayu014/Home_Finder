import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Zillow = "https://appbrewery.github.io/Zillow-Clone/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-blink-features = AutomationControlled")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US;q=0.9,en,q=0.8"
}

class Property:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.Max_Amount = 3000
        
    
    def find_home(self):
        with requests.get(url=Zillow,headers=header) as response:
            # print(response.status_code)
            content = response.text
            soup = BeautifulSoup(content,"html.parser")
            soup.prettify()
            # print(content)
            all_address_elements = soup.select(".StyledPropertyCardDataWrapper a")
            all_address = [address.text.replace("|"," ").strip() for address in all_address_elements]
            # print(all_address)

            all_price_elements = soup.select(".PropertyCardWrapper span")
            all_price = [price.text.replace("/mo","").split("+")[0].strip() for price in all_price_elements]
            # print(all_price)

            all_link_elements = soup.select(".StyledPropertyCardPhotoBody a")
            all_link = [link["href"].strip() for link in all_link_elements]
            print(all_link)

            

    

search_property = Property()
search_property.find_home()
search_property.driver.quit()





    





