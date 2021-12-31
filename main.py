from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import autoit
import random
chromeoption = webdriver.ChromeOptions()
chromeoption.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path="C://facebook//chromedriver.exe" ,options=chromeoption)

driver.get('https://business.facebook.com/business_locations/?business_id=461017628986189')
driver.implicitly_wait(2)
driver.find_element_by_id('email').send_keys('user')
driver.find_element_by_id('pass').send_keys('pass')
driver.find_element_by_id('pass').send_keys(Keys.ENTER)
print("Login Facebook")
file = open('diachi.txt', 'r', encoding = 'utf-8')

for i in range(20):
    
    diachi = file.readline()
    print(f"đã đọc file trích xuất ra địa chỉ{diachi}")
    duoisdt = str(random.randint(1111,9999))
    sdt = "036859" + duoisdt
    
    driver.implicitly_wait(30)
    driver.find_element_by_class_name('_43rm').click()
    driver.implicitly_wait(30)
    tieptuc = driver.execute_script('document.querySelector("body > div._10._d2i.uiLayer._4-hy._3qw > div._59s7._9l2g > div > div > div > div > div > div > div._4iyh._2pia._2pi4 > span._4iyi > div > div:nth-child(2) > button > div > div").click()')
    driver.implicitly_wait(30)
    driver.find_element_by_css_selector('input[value="ADD_MANUALLY"]').click()
    driver.implicitly_wait(5)
    next = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div._4iyh._2pia._2pi4 span._4iyi div div button._271k._271m._1qjd._7tvm._7tv3._7tv4[style='max-width: 100%; letter-spacing: normal; color: rgb(255, 255, 255); font-size: 14px; font-weight: bold; font-family: Roboto, Arial, sans-serif; line-height: 36px; text-align: center; background-color: rgb(24, 119, 242); border-color: rgb(24, 119, 242); height: 36px; padding-left: 16px; padding-right: 16px; border-radius: 6px; border-width: 0px;']")))
    next.click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[4]/div/div[2]/span/input').send_keys('huhu')
    driver.implicitly_wait(5)
    print("Đã nhập xong địa chỉ 1")
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[5]/span/span/label/input').send_keys(diachi)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[5]/span/span/label/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[5]/span/span/label/input').send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    print(f"Đã nhập xong địa chỉ {diachi}")
    zipcode = int(random.randint(33333,88888))
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[6]/div/div[2]/span/input').send_keys(zipcode)
    print('Đã nhập xong zipcode')
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[7]/div/div[2]/span/input').send_keys(sdt)
    time.sleep(2)
    print(f"đã nhập xong{sdt}")
    ok = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span._4iyi div div button._271k._271m._1qjd._7tvm._7tv3._7tv4[style='max-width: 100%; letter-spacing: normal; color: rgb(255, 255, 255); font-size: 14px; font-weight: bold; font-family: Roboto, Arial, sans-serif; line-height: 36px; text-align: center; background-color: rgb(24, 119, 242); border-color: rgb(24, 119, 242); height: 36px; padding-left: 16px; padding-right: 16px; border-radius: 6px; border-width: 0px;']")))
    ok.click()
    time.sleep(random.randint(5,10))
    driver.refresh()
    print("đã xong page "+ str(i))
    deplay = int(random.randint(50,90))
    print(f"Thời gian nghỉ:{deplay}s")
    time.sleep(deplay)
