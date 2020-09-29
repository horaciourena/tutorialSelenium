from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://youtube.com/")
search = driver.find_element_by_name("search_query")
search.send_keys("Horacio Urena")
search.send_keys(Keys.RETURN)

try:
    contenido = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "contents"))
    )
    videos = contenido.find_elements_by_tag_name("ytd-video-renderer")
    for video in videos:
        titulo = video.find_element_by_id("title-wrapper")
        print(titulo.text)
finally:
    driver.quit()