import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the URL
    driver.get("https://www.saucedemo.com/")
    
    # Step 2: Login
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    
    time.sleep(2)  # Wait for the page to load
    
    # Step 3: Select the highest price item (without using "Sort By")
    item_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    max_price = 0
    max_price_element = None
    
    for price_element in item_prices:
        price = float(price_element.text.replace("$", ""))
        if price > max_price:
            max_price = price
            max_price_element = price_element
    
    # Find the add to cart button corresponding to the highest price item
    highest_price_item_container = max_price_element.find_element(By.XPATH, "..//..")
    add_to_cart_button = highest_price_item_container.find_element(By.CLASS_NAME, "btn_inventory")
    
    # Step 4: Add the selected highest price item to the cart
    add_to_cart_button.click()
    
    print("Test completed successfully.")
finally:
    # Close the browser
    driver.quit()
