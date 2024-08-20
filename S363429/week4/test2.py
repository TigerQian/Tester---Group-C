from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

# Initialize WebDriver (Chrome in this case)
driver = webdriver.Chrome()

try:
    # Step 1: Open the Google homepage
    driver.get("https://www.google.com")
    
    # Ensure the page title contains 'Google'
    assert "Google" in driver.title
    
    # Step 2: Find the search input box, enter the search keyword, and submit
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the search results page to load
    time.sleep(3)
    
    # Print the title of the search results page
    print("Search results title:", driver.title)
    
    # Step 3: Navigate to a new page by clicking on a link, select the first link containing "Selenium"
    link = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium")
    link.click()
    
    # Step 4: Wait for the new page to load and confirm the title has changed
    WebDriverWait(driver, 10).until(EC.title_contains("Selenium"))
    print("New page title:", driver.title)
    
    # Step 5: Verify specific content on the page
    assert "Selenium" in driver.page_source
    
    # Step 6: Capture a screenshot of the current page
    screenshot_path = "/Users/linhaizhong/Desktop/google_screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")
    
    # Step 7: Measure the page load time of an action
    start_time = time.time()
    driver.get("https://www.google.com")
    load_time = time.time() - start_time
    print(f"Page load time is {load_time} seconds")

finally:
    # Close the browser
    driver.quit()
