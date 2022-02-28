from selenium import webdriver # import selenium to the file
from moodle import moodle_locators as locators
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # <-- add this import for drop down lists
import sys
# Moodle Test Automation Plan
# launch Moodle App website - validate we are on the home page
# navigate to Login Screen - validate we are on the login page
# login with admin acount - validate we are on the Dashboard page
# navigate to Add New User page - validate we are on the Add New User page
# populate the new user form using Faker fake data
# submit the form - validate we are on the Browse List of Users page
# search for new user - validate new user is found
# logout from admin account
# login with new user credentials - validate new user can login
# logout from new user account
# login with admin acount
# search for a new user
# delete new user

# This method solves the "DeprecateWarning" error that occurs in Selenium 4 and above.
# 1. Comment out, or remove the previous method which was: driver = webdriver.Chrome('chromedriver.exe path')
# 2. Add following code
#


from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# ----------------------------------------------------------
def setUp():
    print(f'Launch {locators.app} App')
    print('--------------------~*~--------------------')
    # Make browser full screen
    driver.maximize_window()
    # Give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # Navigate to Moodle app website
    driver.get(locators.moodle_url)
    # Check that Moodle URL and the home page title are displayed
    if driver.current_url == locators.moodle_url and driver.title == locators.moodle_home_page_title:
        print(f'Yey! {locators.app} Launched Successfully')
        print(f'{locators.app} homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app}  did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page Title: {driver.title}')
        tearDown()


def tearDown(): #
    if driver is not None:
        print('--------------------~*~--------------------')
        print(f'The test Completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


# login to Moodle
def log_in(username, password):
    if driver.current_url == locators.moodle_url: # check we are on the home page
        print(f'Login Link is displayed: {driver.find_element(By.LINK_TEXT, "Log in").is_displayed()}')
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.moodle_login_page_url: # check we are on the login page
            print(f'--- {locators.app} App Login Page is displayed!')
            sleep(0.25)
            driver.find_element(By.ID, 'username').send_keys(locators.admin_username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(locators.admin_password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click() # method 1 using ID
            # locators XPATH practice --------------------------------------
            # driver.find_element(By.XPATH, '//button[contains(.,"Log in")]').click()  # method 2, by XPATH using anything with the text Log in
            # driver.find_element(By.XPATH, '//button[contains(@id, "loginbtn")]').click()  # method 3, by XPATH using specific id
            # driver.find_element(By.XPATH, '//button[@id="loginbtn"]').click()  # method 4, by XPATH, without contains
            # driver.find_element(By.XPATH, '//*[@id="loginbtn"]').click()  # method 5, by XPATH without button * means any element
            # driver.find_element(By.CSS_SELECTOR, 'button[id="loginbtn"]').click() # method 1 CSS_SELECTOR
            # driver.find_element(By.CSS_SELECTOR, 'button#loginbtn').click()  # method 2 CSS_SELECTOR
            # -----------------------------------------------------------------------------------------------
            # validate we are at the Dashboard
            if driver.title == locators.moodle_dashboard_page_title and driver.current_url == locators.moodle_dashboard_url:
                assert driver.current_url == locators.moodle_dashboard_url
                assert driver.title == locators.moodle_dashboard_page_title
                print(f'--- Login Successful. {locators.app} Dashboard is displayed - Page title: {driver.title}')
            else:
                print(f'Dashboard is not displayed. Check your code and try again.')


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    # validate logout successful
    if driver.current_url == locators.moodle_url:
        print(f'--- Logout Successful! at {datetime.datetime.now()}')


def create_new_user():
    # navigate to Site Admin
    driver.find_element(By.XPATH,'//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    # validate we are on 'Add a new user page'
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    assert driver.title == locators.moodle_add_new_user_page_title
    print(f'--- Navigate to Add a New user Page - Page Title: {driver.title}')
    sleep(0.25)
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(0.25)
    # select an options 'Allow everyone to see my email address'
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    # select an options 'Canada'
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text(locators.country)
    sleep(0.25)
    # select an options 'America/Vancouver'
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(0.25)
    # upload picture
    # click arow element
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(0.25)
    # ----------------------------------------------------
    # navigate to image selection
    # driver.find_element(By.LINK_TEXT, 'Server files').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT, 'sl_Frozen').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT, 'sl_How to build a snowman').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT, 'Course image').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT, 'gieEd4R5T.png').click()
    # sleep(0.25)
    # ----------------------------------------------------
    # Replace previous code for selecting an image with the loop below
    img_path = ['Server files','sl_Frozen', 'sl_How to build a snowman', 'Course image', 'gieEd4R5T.png']
    for p in img_path:
        driver.find_element(By.LINK_TEXT, p).click()
        sleep(0.25)

    # select radio button
    # driver.find_element(By.XPATH, '//input[@value="4"]').click()  # method 1
    driver.find_element(By.XPATH, '//label[contains(.,"Create an alias/shortcut to the file")]').click()  # method 2
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(.,"Select this file")]').click()
    sleep(0.25)

    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_desc)
    sleep(0.25)
    # populate Additional Name
    driver.find_element(By.LINK_TEXT, 'Additional names').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.middle_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.first_name)
    sleep(0.25)

    #papulate interests
    driver.find_element(By.LINK_TEXT, 'Interest').click()


    for tag in locators.list_of_interest:
        # methods1
        # driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplte_input"])').send_keys(tag)
        # driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplte_input"])').send_keys(Key)

        driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplte_input"])').send_keys(tag + tag.Enter)
        sleep(0.25)
        driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplte_input"])').send_keys(tag + ",")

        sleep(0.25)

    #populate Optional fields
    driver.find_element(By.LINK_TEXT, 'Optional').click()


    for i in range(len(locators.list_opt)):
        opt,ids,val = locators.list_opt[i], locators.list_id[i], locators.list_val[i]
        print(f'Populate{opt} field')
        driver.find_element(By.ID,ids).send_keys(val)
        sleep(0.25)

     ###################################################    ----------------------
     # press submit button
    driver.find_element(By.ID, 'id_submitbuttom').click()
    sleep(0.25)
    print(f'--------New User "{locators.new_username}/{locators.new_password}" is added---------------')
    ######################################################


def search_user():
   # Check we are on the user's MAin PAge
    if driver.current_urlb == locators.moodle_users_main_page and driver.title == locators.moodle_userd_main_page_tittle:
        assert driver.find_element(By.LINK_TEXT, 'Browse list of uders').is_displayed()
        print('/''Browse list of users page/''is displayed')
        sleep(0.25)
        # check we can search user by email
        print(f'----------Search for user by email address: {locators.email}-----------')
        driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()

        if driver.find_element(By.XPATH, f'//td[contains(.,"{locators.email}")]'):
            print(f'-----User: {locators.email} found!-----------------')


    #breakpoint()
def check_new_user_can_login():
    if driver.title == locators.moodle_dashboard_page_title and driver.current_url == locators.moodle_dashboard_url:
        if driver.find_element(By.XPATH, f'//span[contains(.,"{locators.full_name}")]').is_displayed():
            print(f'----------------------User with full name: {locators.full_name} is displayed,-------------')


def delete_user():
    # navigate to Site Admin
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Brows list of user').click()
    sleep(0.25)

    search_user()
    breakpoint()
    #

#logger:
def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.new_username}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()



##setUp()
        # ------------------CREATE NEW USER---------------------
        #log_in(locators.admin_username, locators.admin_password)
        #create_new_user()
        #search_user()
        #log_out()
        # -------------------------------------------------------
        # -------------LOGIN AS NEW USER------------------------------
        #log_in(locators.new_username, locators.new_password)
        # delete new user function call goes here
        #delete_user()
        #log_out()
        # --------------------------------------------------------
        # --------------DELETE NEW USER--------------------------
        # -------------------------------------------------------
        #delete_user()
        #log_out()
        #-------------------------------------------
        #tearDown()