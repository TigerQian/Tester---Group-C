// Configuration for Katalon TestOps
String testOpsUrl = 'https://testops.katalon.com/api/v1/test-results'
String apiToken = 'YOUR_API_TOKEN'

// Define a method to report test results
def reportResults() {
    // Construct the payload for the API request
    def payload = [
        'projectId': 'YOUR_PROJECT_ID',
        'results': [
            [
                'testCaseId': 'YOUR_TEST_CASE_ID',
                'status': 'PASSED', // or 'FAILED', depending on the result
                'duration': 1234 // Duration in milliseconds
            ]
        ]
    ]
    // Call the API to send results
    // Example: httpClient.post(testOpsUrl, payload, apiToken)
}
