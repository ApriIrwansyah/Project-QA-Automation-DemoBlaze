from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from time import sleep

class DemoBlaze:
    def __init__(self):
        self.driver     = webdriver.Chrome()
        self.wait       = WebDriverWait(self.driver, 10)
        self.base_url   = "https://www.demoblaze.com/index.html"
        self.driver.maximize_window()
        
    def open(self):
        self.driver.get(self.base_url)
        
    def close(self):
        sleep(5)
        self.driver.quit()

    def getContact(self,contactEmail, contactName, message):
        self.open()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Contact']").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='recipient-email']").send_keys(contactEmail)
        sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='recipient-name']").send_keys(contactName)
        sleep(2)
        self.driver.find_element(By.XPATH, "//textarea[@id='message-text']").send_keys(message)
        sleep(2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Send message']").click()
    
    # Untuk verifikasi jika berhasil ditambahkan
    

    # success_message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "sweet-alert"))).text
    #     assert "Alert Text: Thanks for the message!!" in success_message

if __name__ == "__main__":
    automation = DemoBlaze()
    try:
        automation.open()
        automation.getContact("ahmadsatria@gmail.com", "ahmad satria", "Hallo")
        # automation.verifySuccess()
    finally:
        automation.close()
        print("Successfully")