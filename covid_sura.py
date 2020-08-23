from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json

driver = webdriver.Firefox(executable_path="C:/firefox_webdriver/geckodriver.exe")

with open("employees.json") as json_file:
    data = json.load(json_file)

    for p in data["employees"]:

        print(p["name"] + " is loading!")

        driver.get("https://www.segurossura.com.co/covid-19/encuestas/paginas/sintomas.aspx")

        time.sleep(3)

        nextPageBtn = driver.find_element_by_name("data[page3SiAutorizo]")
        nextPageBtn.click()

        userId = driver.find_element_by_name("data[identificacion_usuario]")
        userId.send_keys(p["id"])

        userName = driver.find_element_by_name("data[nombre_usuario]")
        userName.send_keys(p["name"])

        nextPage2Btn = driver.find_element_by_name("data[page1Siguiente]")
        nextPage2Btn.click()

        submitBtn = driver.find_element_by_name("data[page2Finalizar]")
        submitBtn.click()

        print(p["name"] + " is done!")

        time.sleep(3)

driver.close()