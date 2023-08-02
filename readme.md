### DVWA Brute Force Python Example

This repo shows how to use Selenium and Python to perform a brute force attack on the `/brute/` route of the DVWA (PHP web app). 

It is assumed that the DVWA is running locally at http://localhost:4280/ - and that you already have installed Selenium Chrome Driver and configured it correctly. I installed it through `brew install --cask chromedriver`

`passwords.txt` comes from https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt

Once we authN to the site and change the security level to Low, we can then start sending a bunch of GET requests with the Url params, iterating through the passwords.txt list to eventually figure out the password for the admin user account. 

To run the script, run main.py