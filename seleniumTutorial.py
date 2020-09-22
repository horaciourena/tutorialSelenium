# from selenium import webdriver

# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)

# # driver.get("https://google.com")
# # driver.close() // It will close the active Window Tap
# # driver.quit() # This will close the entire browser with all its windows taps

# # Second Video // Obteniendo Elementos de HTML

# from selenium.webdriver.common.keys import Keys
# import time

# driver.get("https://youtube.com")

# search = driver.find_element_by_name("search_query")
# search.send_keys("Horacio Urena")
# search.send_keys(Keys.RETURN)
# content = driver.find_elements_by_class_name("style-scope ytd-page-manager")
# # print(driver.page_source)

# # time.sleep(5)

# driver.quit()