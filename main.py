from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Firefox()
driver.get("https://www.mshca.com/directory/")


locations = driver.find_elements(By.CLASS_NAME, "ill_directory_list_city")
urls = []
data = []

for location in locations:
    outlink = location.find_element(By.TAG_NAME , 'li')
    link = outlink.find_element(By.TAG_NAME, 'a')
    urls.append(link.get_attribute('href'))

for url in urls:
    driver.get(url)
    information = driver.find_elements(By.ID, "main")
    rawData = []
    

    for info in information:
        text = (info.text).split("\n")
        rawData.append(text)
    data.append(rawData[0])

df1 = pd.DataFrame(data)
df1.to_csv("output.csv", encoding='utf-8', index=False)
# address = driver.find_elements(By.CSS_SELECTOR, "p")

# for info in address:
#      print(info.text)

# contact_info = driver.find_element(By.CLASS_NAME, "ill_directory_item_contact_info").text
# print("Contact Info:", contact_info)


# beds = driver.find_element(By.CLASS_NAME, "nfbeds").text
# print(beds)



#data["County": rawData[0], ]

