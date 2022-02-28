from typing import List, Union, Any

from faker import Faker
fake = Faker(locale='en_CA')

#------------------ locators section-------------------------------
app = 'Moodle'
admin_username = 'JudeMichaelRojas'
admin_password = 'Moodle!123'
moodle_url = 'http://52.39.5.126/'
moodle_home_page_title = 'Software Quality Assurance Testing'
moodle_login_page_url = 'http://52.39.5.126/login/index.php'
moodle_login_page_title = 'Software Quality Assurance Testing: Log in to the site'
moodle_dashboard_url = 'http://52.39.5.126/my/'
moodle_dashboard_page_title = 'Dashboard'
moodle_add_new_user_page_title = 'SQA: Administration: Users: Accounts: Add a new user'
moodle_users_main_page = 'http://52.39.5.126/admin/user.php'
moodle_users_main_page_title = 'SQA: Administration: User: Accounts: Browse list of users'

# -------------------- data section ---------------------------------
first_name = fake.first_name()
last_name = fake.last_name()
middle_name = fake.first_name()
full_name = f'{first_name} {last_name}'

new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password()
email = f'{new_username}@{fake.free_email_domain()}'
email1 = fake.email()

moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
country = fake.current_country()
description = f'User added by {admin_username} via Python Selenium Automated Script' #fake.sentence(nb_words=100) #
pic_desc = f'pic submited by {full_name}'
list_of_interest = [fake.job(), fake.job(), fake.job(), fake.job(), fake.job()]



Web_page = fake.url()
icq_num = fake.pyint(1111,9999)
skype_id = new_username
ain_id = f'{last_name.lower()}{fake.pyint(111,999)}'
yahoo_id = new_username
msn_id = f'{last_name.lower()}{fake.pyint(11,99)}{country}'
id_num = fake.pyint(111,999)
institution = fake.company()
department = fake.catch_phrase()
phone = fake.phone_number()
mobile_phone = fake.phone_number()
address = fake.address().replace("/n","")

list_opt = ['web page', 'ICQ number', 'Sykpe ID', 'ATM ID', 'YAHOO ID', 'MSN ID',
            'ID number', 'Institution', 'Department',
            'Phone', 'Mobile phone', 'Address']


list_opt = ['id_url', 'id_icq', 'id_skype', 'id_yahoo', 'id_msn',
            'id_idnumber', 'id_institution', 'id_department',
            'id_phone1', 'id_phone2', 'id_address']

list_val = (web_page, ICQ_number, Sykpe_ID, ATM_ID, YAHOO_ID, MSN_ID,
            ID_number, Institution, Department,
            Phone, Mobile_phone, Address )

print(list_val)
print(list_of_interest)


print(first_name, last_name, middle_name, new_username, new_password, email, email1)