# Another Method To Download imgs 

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import requests
from webdriver_manager.chrome import ChromeDriverManager

path = r"C:\Users\hp\AppData\Local\Programs\Python\Python311\python web scraping\selenium\chromedriver-win64\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get(f"https://mangapanda.in/?page=5")

search = driver.find_element(By.NAME, "q")
search.clear()
search.send_keys("one piece")
search.send_keys(Keys.RETURN)

driver.implicitly_wait(5) 

element = driver.find_elements(By.TAG_NAME, "img")

imgs_link = []

for i in range(1, 6) : 
  for img in element : 

    img_link = img.get_attribute("src")
    # print(img_link)

    file_name = f"0{i:02d}_{element.index(img):03d}.jpg"

    response = requests.get(img_link)

    if response.status_code == 200 : 

      with open(file_name, "wb") as file_img : 
        file_img.write(response.content)

      # imgs_link.append(img_link)

    else:
      print(f"Failed to download: {img_link}")

driver.close()
