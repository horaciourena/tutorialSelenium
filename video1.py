from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://youtube.com/horaciourena")
# print(driver.title) id, class, name, tag
driver.close()