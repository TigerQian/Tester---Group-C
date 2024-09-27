import static com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI

// Open the browser
WebUI.openBrowser('https://example.com/login')

// Maximize the browser
WebUI.maximizeWindow()

// Set username
WebUI.setText(findTestObject('Page_Login/input_username'), 'your_username')

// Set password
WebUI.setText(findTestObject('Page_Login/input_password'), 'your_password')

// Click the login button
WebUI.click(findTestObject('Page_Login/button_login'))

// Verify login success
WebUI.verifyElementVisible(findTestObject('Page_Home/label_welcome'))

// Close the browser
WebUI.closeBrowser()
