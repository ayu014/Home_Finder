import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Zillow = "https://appbrewery.github.io/Zillow-Clone/"
g_form ="https://forms.gle/FcNoH74S7sE3rokq6"


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
        
    
    def find_home(self):
        with requests.get(url=Zillow,headers=header) as response:
            # print(response.status_code)
            content = response.text
            soup = BeautifulSoup(content,"html.parser")
            soup.prettify()
            # print(content)
            global all_address
            all_address_elements = soup.select(".StyledPropertyCardDataWrapper a")
            all_address = [address.text.replace("|"," ").strip() for address in all_address_elements]
            # print(all_address)

            global all_price
            all_price_elements = soup.select(".PropertyCardWrapper span")
            all_price = [price.text.replace("/mo","").split("+")[0].strip() for price in all_price_elements]
            # print(all_price)

            global all_link
            all_link_elements = soup.select(".StyledPropertyCardPhotoBody a")
            all_link = [link["href"].strip() for link in all_link_elements]
            # print(all_link)


    def fill_form(self):
        self.driver.get(g_form)
        time.sleep(2)
        # address_element = self.driver.find_element(By.class,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_element = self.driver.find_element(by=By.CLASS_NAME,value="whsOnd zHQkBf")
        price_element = self.driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_element = self.driver.find_element(by=By.XPATH,value='<input type="text" class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="off" tabindex="0" aria-labelledby="i11 i14" aria-describedby="i12 i13" aria-disabled="false" required="" dir="auto" data-initial-dir="auto" data-initial-value="">')
        submit_button = self.driver.find_element(by=By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

        
        for n in range(len(all_address)):
            address_element.click()
            address_element.send_keys(all_address[n])
            time.sleep(1)
            price_element.click()
            price_element.send_keys(all_price[n])
            time.sleep(1)
            link_element.click()
            link_element.send_keys(all_link[n])
            time.sleep(1)
            submit_button.click()
            

  

search_property = Property()
search_property.find_home()
search_property.fill_form()
time.sleep(2)
search_property.driver.quit()





    





