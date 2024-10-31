from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from time import sleep

class DemoBlaze:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait       = WebDriverWait(self.driver, 10)
        self.base_url = "https://www.demoblaze.com/index.html"
        self.driver.maximize_window()
        
    def open(self):
        self.driver.get(self.base_url)
        
    def close(self):
        sleep(5)
        self.driver.quit()
    
    # Untuk menambahkan produk ke keranjang ?
    def add_product_to_cart(self, productName):
        # Menunggu hingga produk dapat diklik
        product = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Samsung galaxy s6']")))
        product.click()
        
        # Tunggu tombol 'Add to cart' dan klik
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Add to cart']")))
        add_to_cart_button.click()

        # Menunggu peringatan untuk diterima
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        
    # Untuk Melakukan Pemayaran produk
    def checkout(self):
        # Klik pada icon keranjang
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='cartur']")))
        cart_icon.click()
        sleep(2)
        
        # Lanjutkan ke pembayaran
        # //button[normalize-space()='Place Order']
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Place Order')]")))
        checkout_button.click()
        sleep(2)
        
        # Isi Form Checkout
        name        = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).send_keys("John Doe")
        country     = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='country']"))).send_keys("Indonesia")
        city        = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='city']"))).send_keys("Jakarta")
        creditCard  = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='card']"))).send_keys("1234567890123456")
        month       = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='month']"))).send_keys("12")
        year        = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='year']"))).send_keys("2024")
        
        # Klik pada tombol pembelian
        purchaseButton = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Purchase']")))
        purchaseButton.click()


# Sekarang, saya akan membuat fungsi utama untuk memanfaatkan kelas dan melakukan tindakan.
if __name__ == "__main__":
    automation = DemoBlaze()
    try:
        automation.open()
        automation.add_product_to_cart("Samsung galaxy s6")
        automation.checkout()
    finally:
        automation.close()
        print("Successfully")
        
        