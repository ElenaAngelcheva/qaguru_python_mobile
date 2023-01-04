import os

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

load_dotenv()
app = os.getenv('APP')
remote_url = os.getenv('REMOTE_URL')
userName = os.getenv('USER_NAME')
accessKey = os.getenv('ACCESS_KEY')
projectName = os.getenv('PROJECT_NAME')
buildName = os.getenv('BUILD_NAME')
sessionName = os.getenv('SESSION_NAME')




options = UiAutomator2Options().load_capabilities({
    # Specify device and os_version for testing
    "platformName": "android",
    "platformVersion": "9.0",
    "deviceName": "Google Pixel 3",

    # Set URL of the application under test
    "app": app,

    # Set other BrowserStack capabilities
    'bstack:options': {
        "projectName":  projectName,
        "buildName": buildName,
        "sessionName": sessionName,

        # Set your access credentials
        "userName": userName,
        "accessKey": accessKey
    }
})