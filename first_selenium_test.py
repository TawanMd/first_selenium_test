from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://automationexercise.com/")

# Print the page title
print(f"Page Title: {driver.title}")

login_button = driver.find_element(By.CLASS_NAME, "fa-lock")
login_button.click()

sign_up = driver.find_element(By.CLASS_NAME, "signup-form")
print(f"New user page acessed.")
sleep(1)

username = driver.find_element(By.NAME, "name")
username.click()
username.send_keys("Teste123")

print("Clicked the name slot and typed into the name slot.")
sleep(1)

print("Searching for email adress box")

useremail = driver.find_element(By.CSS_SELECTOR, ".signup-form input[name='email']")
useremail.click()

sleep(1)

useremail.send_keys("emailteste@gmail.com")

sleep(1)

sign_in_button = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > button")

sign_in_button.click()

sleep(1)

print(f"Page Title: {driver.title}")

title_gender = driver.find_element(By.CSS_SELECTOR, "#id_gender1")
title_gender.click()

password_button_EAINF = driver.find_element(By.CSS_SELECTOR, "#password")
password_button_EAINF.click()
password_button_EAINF.send_keys("test123")

sleep(1)

#clica no seletor de data e usando o teclado pula para as outras "Colunas"
#dias
date_of_birth_days = driver.find_element(By.CSS_SELECTOR, "#days")
date_of_birth_days.click()
date_of_birth_days.send_keys("3")
sleep(1)
date_of_birth_days.send_keys(Keys.ENTER)

#meses
date_of_birth_month = driver.find_element(By.CSS_SELECTOR, "#months")
date_of_birth_month.send_keys("MAY")
date_of_birth_month.send_keys(Keys.ENTER)
sleep(1)

#Anos
date_of_birth_years = driver.find_element(By.CSS_SELECTOR, "#years")
date_of_birth_years.send_keys("2003")
date_of_birth_years.send_keys(Keys.ENTER)

sleep(1)

newsletter = driver.find_element(By.CSS_SELECTOR, "#newsletter")
newsletter.click()

receive = driver.find_element(By.CSS_SELECTOR, "#optin")
receive.click()

first_name = driver.find_element(By.CSS_SELECTOR, "#first_name")
first_name.click()
first_name.send_keys("test")

last_name = driver.find_element(By.CSS_SELECTOR, "#last_name")
last_name.click()
last_name.send_keys("test")

company = driver.find_element(By.CSS_SELECTOR, "#company")
company.click()
company.send_keys("test")

adress = driver.find_element(By.CSS_SELECTOR, "#address1")
adress.click()
adress.send_keys("test")

country = driver.find_element(By.CSS_SELECTOR, "#country")
country.click()
country.send_keys("US")
country.send_keys(Keys.ENTER)

state = driver.find_element(By.CSS_SELECTOR, "#state")
state.click()
state.send_keys("teste123")

city = driver.find_element(By.CSS_SELECTOR, "#city")
city.click()
city.send_keys("teste123")

zipcode = driver.find_element(By.CSS_SELECTOR, "#zipcode")
zipcode.click()
zipcode.send_keys("testa")

mobile_num = driver.find_element(By.CSS_SELECTOR, "#mobile_number")
mobile_num.click()
mobile_num.send_keys("12312312312")

create_account = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div > div > form > button")
create_account.click()

message = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div > h2 > b")
if message == "Congratulations!":
    print("Teste deu certo, conseguiu cadastrar a conta")
else:
    print("Teste não deu certo, não deu certo. Possivelmente conta já existe.")

logout_button = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a")
logout_button.click()

sleep(2)

login_sign_in_button = message = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a")
login_sign_in_button.click()

sleep(3)

email_login = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=email]:nth-child(2)")
email_login.click()
email_login.send_keys("emailteste@gmail.com")


password_login = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=password]:nth-child(3)")
password_login.click()
password_login.send_keys("test123")

login_button_mainpage = driver.find_element(By.CSS_SELECTOR,"#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > button")
login_button_mainpage.click()

sleep(1)

delete_account = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(5) > a")
delete_account.click()

sleep(100)
driver.quit()