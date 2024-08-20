import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class GoogleSearchTest(unittest.TestCase):
    
    def setUp(self):
        # 初始化Chrome WebDriver
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        # 测试结束后关闭浏览器
        self.driver.quit()
    
    def test_google_search(self):
        driver = self.driver
        # Step 1: 打开Google首页
        driver.get("https://www.google.com")
        
        # 验证页面标题中包含 'Google'
        self.assertIn("Google", driver.title, "Google页面标题不正确")
        
        # Step 2: 查找搜索框并输入关键词进行搜索
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium Python")
        search_box.send_keys(Keys.RETURN)
        
        # 等待搜索结果页面加载
        time.sleep(3)
        
        # Step 3: 验证搜索结果页面的标题包含关键词
        self.assertIn("Selenium", driver.title, "搜索结果标题不包含'Selenium'")
        
        # Step 4: 验证页面是否有结果 (可以进一步验证搜索结果的存在)
        results = driver.find_elements(By.CSS_SELECTOR, "div.g")
        self.assertGreater(len(results), 0, "未找到任何搜索结果")

if __name__ == "__main__":
    unittest.main()
