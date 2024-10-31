from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

# Dalam Pengujian ini saya mengimplementasikan untuk menguji fitur login dan registrasi

class DemoBlaze:
    def __init__(self):
        self.driver     = webdriver.Chrome()
        self.base_url   = "https://www.demoblaze.com/index.html"
        self.driver.maximize_window()
        
    def open(self):
        self.driver.get(self.base_url)
        
    def close(self):
        sleep(5)
        self.driver.quit()
    
    def register(self, username, password):
        self.open()
        self.driver.find_element(By.XPATH, "//a[@id='signin2']").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='sign-username']").send_keys(username)
        sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='sign-password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign up']").click()
        sleep(2)
        
    def check_error_message(self):
        try:
            error_message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'This username already exists')]") 
            # This user already exist.
            return error_message.is_displayed()
        except:
            return False
        
    def login(self, username, password):
        self.open()
        self.driver.find_element(By.ID, "login2").click()
        sleep(2) # Tunggu modal login muncul
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        sleep(2)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        sleep(2)
    
    # Fungsi untuk memeriksa status login
    def check_login_status(self):
        try:
            self.driver.find_element(By.ID, "logout2")
            return True 
        except:
            return False
        
        
def main():
    driver_path = "QA_Engineer\PROJECT_SELENIUM_PYEST_CUCUMBER_APPIUM\Project_Blazedemo.com_selenium\chromedriver.exe"
    
    demoblaze       = DemoBlaze()
    
    # =================================================================
    # Uji Login Valid
    print()
    print("Mengujikan login valid")
    demoblaze.login("ahmadsatria@gmail.com", "ThisIsMyPass.123")
    if demoblaze.check_login_status():
        print("Uji Login valid berhasil")
    else:
        print("Uji login valid gagal")
    
    # Logout setelah login valid
    demoblaze.driver.find_element(By.ID, "logout2").click()
    sleep(2)
    # =================================================================
    
    # =================================================================
    # Uji Login Invalid
    print()
    print("Mengujikan login invalid")
    demoblaze.login("ahmadsatria@gmaaaaaail.com", "ThisIsMyPass.123")
    if not demoblaze.check_login_status():
        print("Uji Login invalid berhasil")
    else:
        print("Uji login invalid gagal")
    # =================================================================
    
    # =================================================================
    # Uji registrasi valid
    print()
    print("Mengujikan regtister valid")
    demoblaze.register("ajissatria@gmail", "ThisIsMyPass.123")
    if demoblaze.check_login_status():
        print("Uji registrasi valid berhasil.")
    else:
        print("Uji registrasi valid gagal.")
    # =================================================================
    
    # =================================================================
    # Uji registrasi invalid
    print()
    print("Mengujikan register invalid")
    demoblaze.register("ajissatria@gmail", "ThisIsMyPass.123")
    if demoblaze.check_error_message():
        print("Uji registrasi invalid berhasil.")
    else:
        print("Uji registrasi invalid gagal.")
    # =================================================================
    
    # Tutup Browser
    demoblaze.close()
    
if __name__ == "__main__":
    main()
        
