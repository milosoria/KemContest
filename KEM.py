from selenium import webdriver
import os
import time
from bs4 import BeautifulSoup as BS
import winsound
duration = 10000  # milliseconds
freq = 440  # Hz
driver = webdriver.Chrome(os.getcwd()+"\\chromedriver.exe")
driver.get("https://www.kemxtreme.cl/")
explorando = True
c = 0
c_1 = 0
while explorando:
    encontrado = False
    c += 1
    element = driver.find_element_by_xpath('//*[@id="generado"]')
    time.sleep(1)
    element = element.get_attribute('value')
    input_1 = driver.find_element_by_xpath('//*[@id="form"]/fieldset/input')
    input_1.send_keys(element)
    send_button = driver.find_element_by_xpath('//*[@id="enviar"]')
    send_button.click()
    time.sleep(1)
    soup = BS(driver.page_source, features = "html.parser")
    c_1 = 0
    for c_1, item in enumerate(soup.find_all(['div', 'h1']), 1):
        if c_1 == 5:
            if item.text.strip().find("sigue participando :( ¡hay millones de oportunidades!") != -1:
                print("No ganaste")
                print(str(c) + "-" + str(element))
                driver.find_element_by_xpath('//*[@id="principal"]/div[2]/div[3]/a').click()
                encontrado = True
                break
    if not encontrado:
        explorando = False
        winsound.Beep(freq, duration)
        print("GANASTE!")
        print(element)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/fieldset[1]/input').send_keys('camilo pascal soria aranguiz')
        options = driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/fieldset[2]')
        for j, option in enumerate(options.find_element_by_tag_name('option'), 0):
            if j == 3:
                option.click()
        driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/fieldset[3]/input').send_keys(
            '202857442')
        driver.find_element_by_xpath('//*[@id="form"]/div/div[4]/fieldset/input').send_keys(
            '20')
        driver.find_element_by_xpath('//*[@id="form"]/div/div[5]/fieldset/input').send_keys(
            'carmen tellez 4472')
        driver.find_element_by_xpath('//*[@id="form"]/div/div[7]/fieldset[2]/input').send_keys(
            'camilo.soria@uc.cl')
        driver.find_element_by_xpath('//*[@id="enviar"]').click()
        print("SE ENVIO EL FORM")

