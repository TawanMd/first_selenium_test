from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("selenium_test.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

logger.info("Iniciando teste de automação")

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
logger.info("Driver do Chrome inicializado")

# Open the website
driver.get("https://automationexercise.com/")
logger.info("Site aberto: https://automationexercise.com/")

# Print the page title
print(f"Page Title: {driver.title}")
logger.info(f"Título da página: {driver.title}")

login_button = driver.find_element(By.CLASS_NAME, "fa-lock")
login_button.click()
logger.info("Botão de login clicado")

sign_up = driver.find_element(By.CLASS_NAME, "signup-form")
print(f"New user page acessed.")
logger.info("Página de novo usuário acessada")
sleep(1)

username = driver.find_element(By.NAME, "name")
username.click()
username.send_keys("Teste123")
logger.info("Nome de usuário preenchido: Teste123")

print("Clicked the name slot and typed into the name slot.")
sleep(1)

print("Searching for email adress box")
logger.info("Procurando campo de email")

useremail = driver.find_element(By.CSS_SELECTOR, ".signup-form input[name='email']")
useremail.click()

sleep(1)

useremail.send_keys("emailteste@gmail.com")
logger.info("Email preenchido: emailteste@gmail.com")

sleep(1)

sign_in_button = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > button")

sign_in_button.click()
logger.info("Botão de cadastro clicado")

sleep(1)

print(f"Page Title: {driver.title}")
logger.info(f"Título da página após cadastro: {driver.title}")

title_gender = driver.find_element(By.CSS_SELECTOR, "#id_gender1")
title_gender.click()
logger.info("Gênero selecionado: Masculino")

password_button_EAINF = driver.find_element(By.CSS_SELECTOR, "#password")
password_button_EAINF.click()
password_button_EAINF.send_keys("test123")
logger.info("Senha preenchida")

sleep(1)

#clica no seletor de data e usando o teclado pula para as outras "Colunas"
#dias
date_of_birth_days = driver.find_element(By.CSS_SELECTOR, "#days")
date_of_birth_days.click()
date_of_birth_days.send_keys("3")
sleep(1)
date_of_birth_days.send_keys(Keys.ENTER)
logger.info("Dia de nascimento selecionado: 3")

#meses
date_of_birth_month = driver.find_element(By.CSS_SELECTOR, "#months")
date_of_birth_month.send_keys("MAY")
date_of_birth_month.send_keys(Keys.ENTER)
logger.info("Mês de nascimento selecionado: Maio")
sleep(1)

#Anos
date_of_birth_years = driver.find_element(By.CSS_SELECTOR, "#years")
date_of_birth_years.send_keys("2003")
date_of_birth_years.send_keys(Keys.ENTER)
logger.info("Ano de nascimento selecionado: 2003")

sleep(1)

newsletter = driver.find_element(By.CSS_SELECTOR, "#newsletter")
newsletter.click()
logger.info("Checkbox de newsletter marcado")

receive = driver.find_element(By.CSS_SELECTOR, "#optin")
receive.click()
logger.info("Checkbox de ofertas especiais marcado")

first_name = driver.find_element(By.CSS_SELECTOR, "#first_name")
first_name.click()
first_name.send_keys("test")
logger.info("Primeiro nome preenchido: test")

last_name = driver.find_element(By.CSS_SELECTOR, "#last_name")
last_name.click()
last_name.send_keys("test")
logger.info("Sobrenome preenchido: test")

company = driver.find_element(By.CSS_SELECTOR, "#company")
company.click()
company.send_keys("test")
logger.info("Empresa preenchida: test")

adress = driver.find_element(By.CSS_SELECTOR, "#address1")
adress.click()
adress.send_keys("test")
logger.info("Endereço preenchido: test")

country = driver.find_element(By.CSS_SELECTOR, "#country")
country.click()
country.send_keys("US")
country.send_keys(Keys.ENTER)
logger.info("País selecionado: US")

state = driver.find_element(By.CSS_SELECTOR, "#state")
state.click()
state.send_keys("teste123")
logger.info("Estado preenchido: teste123")

city = driver.find_element(By.CSS_SELECTOR, "#city")
city.click()
city.send_keys("teste123")
logger.info("Cidade preenchida: teste123")

zipcode = driver.find_element(By.CSS_SELECTOR, "#zipcode")
zipcode.click()
zipcode.send_keys("testa")
logger.info("CEP preenchido: testa")

mobile_num = driver.find_element(By.CSS_SELECTOR, "#mobile_number")
mobile_num.click()
mobile_num.send_keys("12312312312")
logger.info("Número de celular preenchido: 12312312312")

create_account = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div > div > form > button")
create_account.click()
logger.info("Botão de criar conta clicado")

try:
    message = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div > h2 > b")
    message_text = message.text
    logger.info(f"Mensagem recebida: {message_text}")
    
    if message_text == "Congratulations!":
        logger.info("Teste bem-sucedido: conta criada com sucesso")
        print("Teste deu certo, conseguiu cadastrar a conta")
    else:
        logger.warning("Teste não foi bem-sucedido: mensagem diferente do esperado")
        print("Teste não deu certo, não deu certo. Possivelmente conta já existe.")
except Exception as e:
    logger.error(f"Erro ao verificar mensagem de confirmação: {str(e)}")
    print("Erro ao verificar mensagem de confirmação")

try:
    logout_button = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a")
    logout_button.click()
    logger.info("Botão de logout clicado")
except Exception as e:
    logger.error(f"Erro ao clicar no botão de logout: {str(e)}")

sleep(2)

try:
    login_sign_in_button = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a")
    login_sign_in_button.click()
    logger.info("Botão de login/sign in clicado")
except Exception as e:
    logger.error(f"Erro ao clicar no botão de login: {str(e)}")

sleep(3)

try:
    email_login = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=email]:nth-child(2)")
    email_login.click()
    email_login.send_keys("emailteste@gmail.com")
    logger.info("Email de login preenchido: emailteste@gmail.com")
except Exception as e:
    logger.error(f"Erro ao preencher email de login: {str(e)}")

try:
    password_login = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=password]:nth-child(3)")
    password_login.click()
    password_login.send_keys("test123")
    logger.info("Senha de login preenchida")
except Exception as e:
    logger.error(f"Erro ao preencher senha de login: {str(e)}")

try:
    login_button_mainpage = driver.find_element(By.CSS_SELECTOR,"#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > button")
    login_button_mainpage.click()
    logger.info("Botão de login na página principal clicado")
except Exception as e:
    logger.error(f"Erro ao clicar no botão de login na página principal: {str(e)}")

sleep(1)

try:
    delete_account = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(5) > a")
    delete_account.click()
    logger.info("Botão de deletar conta clicado")
except Exception as e:
    logger.error(f"Erro ao clicar no botão de deletar conta: {str(e)}")

logger.info("Teste finalizado, aguardando 100 segundos antes de fechar o navegador")
sleep(100)
driver.quit()
logger.info("Navegador fechado, teste concluído")