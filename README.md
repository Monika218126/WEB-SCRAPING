# WEB-SCRAPING
Beginner Python web scraping project using Selenium to scrape Amazon laptop data and export structured datasets.
# Amazon Laptop Scraper using Selenium

A beginner-friendly real-world web scraping project built using Python and Selenium to scrape Amazon laptop data and export structured datasets into CSV/Excel files.

---

# 📌 Project Overview

This project automates Amazon India using Selenium WebDriver.

The scraper automatically:

- Opens Amazon India
- Searches for laptops
- Extracts product details
- Extracts prices
- Extracts ratings
- Extracts product links
- Saves data into CSV/Excel format

This project demonstrates:

- Browser Automation
- Dynamic Web Scraping
- Data Cleaning
- Regex Extraction
- CSV/Excel Automation

---

# 🚀 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main Programming Language |
| Selenium | Browser Automation & Web Scraping |
| Pandas | Data Handling |
| OpenPyXL | Excel File Creation |
| Regex (`re`) | Pattern Matching |

---

# 📂 Project Structure

amazon-laptop-scraper/

│

├── demo.py

├── README.md

├── amazon_laptops.csv

└── amazon_laptops.xlsx


# ⚙️ Installation Guide

## ✅ Step 1 — Install Python

Download Python:

https://www.python.org/downloads/

IMPORTANT:

While installing Python:

✅ Tick:

```text
Add Python to PATH
```

---

## ✅ Step 2 — Clone Repository

```bash
git clone https://github.com/your-username/amazon-laptop-scraper.git
```

---

## ✅ Step 3 — Open Project Folder

cd amazon-laptop-scraper


## ✅ Step 4 — Install Required Libraries

pip install selenium pandas openpyxl

# ▶️ Run the Project

Open terminal inside VS Code:   python demo.py

# 📊 Expected Output

## Terminal Output Example

```text
Brand: ASUS
RAM: 16GB
Storage: 512GB SSD
Processor: Ryzen 7
GPU: RTX 3050
Price: ₹ 79,990
```

---

# 📁 Output Files

Generated Files:

```text
amazon_laptops.csv
amazon_laptops.xlsx
```

# 📋 Extracted Data

The scraper extracts:

- Brand
- Product Name
- RAM
- Storage
- Processor
- GPU
- Price
- Rating
- Product Link


# 🧠 Concepts Used

## 🔹 Selenium WebDriver

Used to automate browser actions.

Example:

```python
driver = webdriver.Chrome()
```


# 🔥 Features

✅ Real-world scraping  
✅ Dynamic website automation  
✅ Excel export    
✅ Beginner Data Engineering  


# 🎯 Learning Outcomes
After completing this project, you will understand:
- Selenium Automation
- Web Scraping
- Dynamic Website Handling
- CSV/Excel Automation
- Data Cleaning
- Beginner Data Engineering

---

# ✅ Conclusion

This project demonstrates how Python and Selenium can automate browsers, scrape dynamic e-commerce websites, extract structured product data, and generate datasets for analysis.

Developed using Python and Selenium for educational purposes.
