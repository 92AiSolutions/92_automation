from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Setup WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver.get('https://example.com/products')

# Extract data
products = driver.find_elements(By.CLASS_NAME, 'product')
product_list = []
for product in products:
    name = product.find_element(By.CLASS_NAME, 'product-name').text
    price = product.find_element(By.CLASS_NAME, 'product-price').text
    product_list.append({'Name': name, 'Price': price})

# Save to CSV
df = pd.DataFrame(product_list)
df.to_csv('data/products.csv', index=False)

driver.quit()

