# restock-alert-bot
Restock Alert Bot

This is a Python script that uses Selenium WebDriver to check whether a specific product size is available on an e-commerce product page.

This project was created to practice browser automation, DOM interaction, and explicit waits using Selenium.

Tools used:
- Python 3
- Selenium WebDriver
- ChromeDriver

How it works:
- Opens a product page in Chrome
- Finds available size options
- Selects a user-specified size
- Checks if the “Add to Cart” button is enabled
- Prints the availability status in the terminal

How to use: 
1. 	Install dependencies: pip install selenium
2. 	Run the script: python restock_alert.py
3. 	Enter the product link and desired size when prompted

Notes:
- The script is site-specific and depends on the page’s HTML structure
- Changes to class names or button text may require updates
- Alert notifications are not implemented

This project is under active development, with planned improvements to reliability, scalability, and alert functionality.

Author: Mohamed Ahmed
GitHub: @mohamedahmed3210
