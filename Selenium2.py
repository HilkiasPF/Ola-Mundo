from selenium import webdriver as wbd
from selenium.webdriver.common.by import By
count = 0
for c in range(3):
    driver = wbd.Chrome()
    driver.get('http://secure-retreat-92358.herokuapp.com/')
    p = driver.find_element(By.XPATH, '/html/body/form/input[1]')
    p.send_keys(f'Lucas{count}')
    h = driver.find_element(By.XPATH, '//html/body/form/input[2]')
    h.send_keys(f'Moral{count}')
    h1 = driver.find_element(By.XPATH, '/html/body/form/input[3]')
    h1.send_keys(f'{count}Lucasm1221@gmail.com')
    h2 = driver.find_element(By.XPATH, '/html/body/form/button')
    h2.click()
    driver.close()
    count += 1