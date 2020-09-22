# Operaciones con Mouse y Teclado
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.get("https://correotemporal.org/")
act = ActionChains(driver)
# driver.find_element_by_class_name("open-message btn btn-sm btn-info d-inline-block").click()
# act.send_keys(Keys.) mmohrv_d764h@ludxc.com
driver.get("https://correotemporal.org/")
time.sleep(8)
# print("Trying to click")
correo = driver.find_element_by_id("botoncopiar")
correo.click()
time.sleep(5)

driver.get("https://www.facebook.com/")
# driver.execute_script("window.open('https://www.facebook.com/','new window')")
time.sleep(5)

driver.find_element_by_id("u_0_2").click()
time.sleep(5)
driver.find_element_by_name("firstname").send_keys("Ricardo")
driver.find_element_by_name("lastname").send_keys("Montaner")
time.sleep(3)

# correo = driver.find_element_by_id("botoncopiar")
# correo.click()
# time.sleep(3)
# handles = driver.window_handles
# driver.switch_to.window(handles[0])

email = driver.find_element_by_id("u_1_g")
email.send_keys("email")
email.send_keys(Keys.CONTROL, 'a') #highlight all in box
# email.send_keys(Keys.CONTROL, 'c') #copy
email.send_keys(Keys.CONTROL, 'v') #paste
driver.find_element_by_xpath("//*[@id='password_step_input']").send_keys("VideoAutomation092020@")
mes = driver.find_element_by_xpath("//*[@id='month']")
mes.click()
mes.send_keys("a")
mes.send_keys(Keys.RETURN)
mes.send_keys(Keys.TAB)
emailValidation = email = driver.find_element_by_id("u_1_j")
emailValidation.send_keys("email")
emailValidation.send_keys(Keys.CONTROL, 'a') #highlight all in box
# emailValidation.send_keys(Keys.CONTROL, 'c') #copy
emailValidation.send_keys(Keys.CONTROL, 'v') #paste
year = driver.find_element_by_id("year")
year.click()
year.send_keys("1")
year.send_keys(Keys.RETURN)
year.send_keys(Keys.TAB)
try:
    sexo = driver.find_element_by_id("u_1h_5")
    sexo.click()
except:
    print("No encontre el primer ID, tratando con el segundo.")
try:
    sexo = driver.find_element_by_id("u_1_5")
    sexo.click()
except:
    print("No encontre el segundo ID, tratando con el tercero.")
    sexo = driver.find_element_by_id("u_1_3")
    sexo.click()
signUp = driver.find_element_by_id("u_1_s")
signUp.click()