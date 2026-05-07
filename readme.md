## WEB SCRAPING

# Amazon Laptop Scraper using Selenium

# 📌 Project Overview

This project is a real-world web scraping application built using Python and Selenium.

The scraper automatically:

- Opens Amazon India
- Searches for laptops
- Extracts product details
- Extracts prices
- Extracts ratings
- Extracts product links
- Saves data into an Excel file

This project demonstrates:

- Browser Automation
- Dynamic Web Scraping
- Data Cleaning
- Regex Extraction
- Excel Automation

# 🚀 Technologies Used
-------------------------------------------
| Technology   | Purpose                  |
|______________| _________________________|
| Python       | Main Programming Language|
| Selenium     | Browser Automation       |
| Pandas       | Data Handling            |
| OpenPyXL     | Excel File Creation      |
| Regex (`re`) | Pattern Matching         |
|______________|__________________________|

# 📂 Project Structure   

AmazonScraper/
│
├── demo.py
├── README.md
└── amazon_laptops.xlsx


# ⚙️ Installation Guide

**Step 1 — Install Python**

- Download Python: https://www.python.org/downloads/
- IMPORTANT: While installing Python:
✅ Tick: Add Python to PATH

**Step 2 — Verify Python Installation**

- Open terminal / PowerShell: python --version

**Step 3 — Install Required Libraries**

- Open terminal:  pip install selenium pandas openpyxl
- This installs: selenium - pandas - openpyxl

📝 Create Python File : demo.py
Paste your Selenium scraper code inside it.

▶️ Run the Project: Open terminal inside VS Code:  python demo.py

**📊 Expected Output**

📁Terminal Output:   Brand: ASUS
                      RAM: 16GB
                      Storage: 512GB SSD
                      Processor: Ryzen 7
                      GPU: RTX 3050
                      Price: ₹ 79,990
📁Excel Output :     amazon_laptops.xlsx


# 🧠 Concepts Used:
                    # Selenium WebDriver:
                     - Used to automate browser actions. Example: driver = webdriver.Chrome()

                    # Dynamic Web Scraping:
                     - Amazon loads content dynamically using JavaScript.
                     - Selenium waits for elements before scraping. Example:  WebDriverWait(driver, 10)
                                                                              Regex Extraction
                    # Regex :
                     - used to extract : RAM , Storage , GPU
                       Example: re.search(r'(\\d+GB)', product)


⚠️ COMMON ERRORS & FIXES:

1. # ModuleNotFoundError

-Error: No module named 'openpyxl'
-Solution: pip install openpyxl

2. # PermissionError

-Error: Permission denied: amazon_laptops.xlsx
-Cause: Excel file already open.
-Solution: Close Excel before rerunning script.

3. # Chrome Driver Errors

-Solution: Update Chrome browser.

# Features of This Project

✅ Real-world scraping
✅ Dynamic website automation
✅ Excel export
✅ Product link extraction
✅ Data cleaning
✅ Regex parsing
✅ Beginner Data Engineering

# 📈 Future Improvements

- Multi-page scraping
- Price tracking
- Telegram alerts
- Streamlit dashboard
- AI recommendation system
- Database storage
- Data visualization

# 🎯 Learning Outcomes

- Selenium Automation
- Web Scraping
- Dynamic Website Handling
- Regex Pattern Matching
- Excel Automation
- Data Cleaning
- Beginner Data Engineering

✅ Conclusion

## This project demonstrates how Python and Selenium can automate browsers, scrape dynamic e-commerce websites, extract structured product data, and generate Excel datasets for analysis.
