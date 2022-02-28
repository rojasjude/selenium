from selenium import webdriver # import selenium to the file
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By


# moodle Test Automation plan
# Launch Moodle App Website - validate we are on the home page
# navigate to Login Screen - Validate we are on the login pGE
# Login with admin account - validate we are on the dashbord page
# navigate to add new user page -validate



# create a Chrome driver instance, specify path to chromedriver file
s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome( service=s)



def setup():
    print(f'Lauch Moodle App')
    print('...............')

    # Make browser full screen
    driver.maximize_window()

    # Give browser up to 30 seconds to respond
    driver.implicitly_wait(30)

    # Navigate to Moodle app website
    driver.get('http://52.39.5.126/')

    # Check that Moodle URL and the home page title are displayed
    if driver.current_url == 'http://52.39.5.126/' and driver.title == 'Software Quality Assurance Testing':
        print('Yey! Moodle Launched Successfully')
        print(f'Moodle homepage URL: {driver.current_url}, Home Page Title: {driver.title}')
        sleep(5)

    else:
        print(f'Mooodle did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page Title: {driver.title}')


def teardown():
    if driver is not None:
        print('...................................a.................')
        print(f'The test completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


#  login to Moodle
def log_in():
    if driver.current_url == 'http://52.39.5.126/':
        driver.find_element(By.LINK_TEXT, 'Log In').click()
        if driver.current_url == 'http://52.39.5.126/login/index.php':
            print('Moodle App Login Page is display!')
            sleep(0.25)
            driver.find_element(By.ID, 'username').send_keys('judemichael')
            sleep(0.25)
            driver.find_element(By.ID, 'Password').send_keys('Moodle!123')
            sleep(0.25)
            driver.find_element(By.ID, 'Login').click()



setup()
log_in()
teardown()