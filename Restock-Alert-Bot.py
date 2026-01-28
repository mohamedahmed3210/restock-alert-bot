# Restock Alert Bot
# Author: Mohamed Ahmed, (GitHub: @mohamedahmed3210)
# This checks whether a specific product and size is available on a website

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = input("Enter the product link: ").strip()
size = input("Enter the size you want: ").strip()

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get(link)

wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

print("Page loaded:", driver.title)

labels = driver.find_elements(By.CLASS_NAME, "c-pwa-radio-boxes__label")

found = False

for label in labels:
    if label.text.strip() == size:
        found = True
        label.click()

        try:
            add_to_cart = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[contains(., 'Add to Cart')]")
                )
            )

            if add_to_cart.is_enabled():
                print(f"Size {size} is available!")
            else:
                print(f"Size {size} is out of stock.")

        except:
            print(f"Size {size} is out of stock.")

        break

if not found:
    print(f"Size {size} was not found on this page.")

driver.quit()