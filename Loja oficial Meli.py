from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Caminho do perfil do Chrome onde você está logado
profile_path = r'C:\Users\lucas.oliveira\AppData\Local\Google\Chrome\User Data'

# Configurar as opções do Chrome para usar o perfil
chrome_options = Options()
chrome_options.add_argument('--user-data-dir=' + profile_path)

# Inicializar o WebDriver do Chrome com as opções configuradas
driver = webdriver.Chrome(options=chrome_options)

# Abrir a página do Mercado Livre
driver.get('https://myaccount.mercadolivre.com.br/profile?view=profile&source=rules')

# Esperar até que a página esteja completamente carregada
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Aguardar até que o URL da página seja igual ao esperado
WebDriverWait(driver, 10).until(EC.url_to_be('https://myaccount.mercadolivre.com.br/profile?view=profile&source=rules'))

# Exibir o URL atual para confirmar
print("URL atual:", driver.current_url)
