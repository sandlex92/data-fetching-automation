import  selenium
import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_position(-10000,0)

url = "#"
username = "#"
password = "#"
driver.get(url)
driver.implicitly_wait(10)
uName = driver.find_element(By.XPATH,"//input[@id='ap_email']")
driver.implicitly_wait(10)
pWord = driver.find_element(By.XPATH,"//input[@id='ap_password']")
uName.send_keys(username)
pWord.send_keys(password)
subButton = driver.find_element(By.XPATH,"//input[@id='signInSubmit']")
subButton.click()
time.sleep(10)

all_page_list = driver.find_elements(By.XPATH,"//ul[@class='awsui-table-pagination-content']/li")
num_of_pages = int(all_page_list[-2].text)

def extract_data(driver,df):
    table_body = driver.find_element(By.XPATH,"//tbody")
    table_rows = table_body.find_elements(By.TAG_NAME,"tr")

    page_data = []

    for row in table_rows:
        table_data = row.find_elements(By.TAG_NAME,"td")
        for data in table_data:
            page_data.append(data.text)

        df.loc[len(df)]=page_data
        page_data=[]
    
    return df

df = pd.DataFrame(columns=['PROJECT ID',	'VENDOR ID',	'COMPANY NAME',	'PRODUCT',	'TEST TYPE',	'COUNTRIES',	'STATUS',	'TESTING LOCATION',	'DAYS IN STATUS',	'INTERNAL TESTER'])
for page_num in range(num_of_pages):
         df = extract_data(driver,df)
         next_page = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/div/div/awsui-app-layout/div/main/div[2]/div/span/div/div/div[2]/div[2]/div[2]/div/awsui-table/div/div[2]/div[1]/div/span/span/awsui-table-pagination/ul/li[11]/button/awsui-icon/span").click()
        
df.to_excel('output.xlsx',index=False)
driver.close()


