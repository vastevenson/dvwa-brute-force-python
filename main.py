from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("http://localhost:4280/")

username = 'admin'
password = 'password'

# Find the username and password input fields on the login page using various locators
username_field = driver.find_element('name', 'username')  # Replace 'username' with the actual name attribute of the username field
password_field = driver.find_element('name', 'password')  # Replace 'password' with the actual name attribute of the password field

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

# now we go to the bruteforce page
driver.get("http://localhost:4280/vulnerabilities/brute/")
print()