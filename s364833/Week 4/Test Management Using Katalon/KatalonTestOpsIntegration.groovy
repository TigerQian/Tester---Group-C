import com.kms.katalon.core.api.KeywordUtil as KeywordUtil
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.reporting.TestSuiteSummary as TestSuiteSummary

// After executing your tests, call this method
def reportToTestOps() {
    def testSuite = TestSuiteSummary.getTestSuiteContext().getTestSuiteId()
    def testCase = TestSuiteSummary.getTestCaseContext().getTestCaseId()
    def result = TestSuiteSummary.getResult()

    // Sending test results to Katalon TestOps
    def response = sendResultsToTestOps(testSuite, testCase, result)
    if (response.status == 200) {
        KeywordUtil.logInfo("Successfully reported results to Katalon TestOps.")
    } else {
        KeywordUtil.logError("Failed to report results to Katalon TestOps.")
    }
}

def sendResultsToTestOps(String testSuite, String testCase, Map result) {
    // Implement the API call to Katalon TestOps to send the results
    // Example code to send a POST request to Katalon TestOps API
    // return httpClient.post(url, payload)
}
