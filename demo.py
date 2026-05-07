from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import re
import time

# START CHROME
driver = webdriver.Chrome()

# OPEN AMAZON
driver.get("https://www.amazon.in")

# WAIT
wait = WebDriverWait(driver, 10)

# SEARCH PRODUCT
search = wait.until(
    EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
)

search.send_keys("laptop under 200000")
search.send_keys(Keys.RETURN)

# WAIT FOR PAGE
time.sleep(5)

# GET PRODUCT CARDS
cards = driver.find_elements(
    By.XPATH,
    '//div[@data-component-type="s-search-result"]'
)

print("Total Products Found:", len(cards))

# STORE DATA
data = []

for card in cards:

    try:

        # PRODUCT NAME
        product = card.find_element(
            By.CSS_SELECTOR,
            "h2 span"
        ).text.strip()

        if product == "":
            continue

        # PRICE
        try:
            price = card.find_element(
                By.CLASS_NAME,
                "a-price-whole"
            ).text

        except:
            price = "Not Available"

        # RATING
        try:
            rating = card.find_element(
                By.CLASS_NAME,
                "a-icon-alt"
            ).get_attribute("innerHTML")

        except:
            rating = "No Rating"

        # PRODUCT LINK
        # PRODUCT LINK
        try:
            link_element = card.find_element(
                By.XPATH,
                './/a[contains(@class,"a-link-normal")]'
                  )
            link = link_element.get_attribute("href")
        except:
            link = "No Link"
        # BRAND
        brand = product.split()[0]

        # RAM
        ram_match = re.search(
            r'(\d+\s?GB)',
            product,
            re.IGNORECASE
        )

        ram = ram_match.group(1) if ram_match else "Not Mentioned"

        # STORAGE
        storage_match = re.search(
            r'(\d+\s?GB SSD|\d+\s?TB SSD|\d+\s?GB eMMC)',
            product,
            re.IGNORECASE
        )

        storage = (
            storage_match.group(1)
            if storage_match else "Not Mentioned"
        )

        # PROCESSOR
        processor_match = re.search(
            r'(i3|i5|i7|i9|Ryzen\s?\d|Intel Core Ultra \d)',
            product,
            re.IGNORECASE
        )

        processor = (
            processor_match.group(1)
            if processor_match else "Not Mentioned"
        )

        # GPU
        gpu_match = re.search(
            r'(RTX\s?\d+|GTX\s?\d+|Intel Arc|Intel UHD|Radeon)',
            product,
            re.IGNORECASE
        )

        gpu = (
            gpu_match.group(1)
            if gpu_match else "Integrated Graphics"
        )

        # PRINT OUTPUT
        print("-" * 80)
        print("Brand:", brand)
        print("Product:", product)
        print("RAM:", ram)
        print("Storage:", storage)
        print("Processor:", processor)
        print("GPU:", gpu)
        print("Price: ₹", price)
        print("Rating:", rating)

        # SAVE DATA
        data.append([
            brand,
            product,
            ram,
            storage,
            processor,
            gpu,
            price,
            rating,
            link
        ])

    except Exception as e:
        print("Error:", e)

# CREATE DATAFRAME
df = pd.DataFrame(data, columns=[
    "Brand",
    "Product Name",
    "RAM",
    "Storage",
    "Processor",
    "GPU",
    "Price",
    "Rating",
    "Product Link"
])

# SAVE EXCEL
df.to_csv("amazon_Scraping_new.csv", index=False)  # df.to_csv("amazon_laptops_new.xlsx", index=False) 

print("\nExcel File Created Successfully!")

# CLOSE
input("Press Enter to close browser...")

driver.quit()