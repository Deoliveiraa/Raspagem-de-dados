import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import subprocess
import json

# Configurações do Selenium
options = Options()
options.headless = True  # Executar em modo headless (sem interface gráfica)

# Use o ChromeDriverManager para instalar o ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URLs das categorias com seus respectivos nomes
urls = {
    "https://www.amazon.com.br/s?k=air+fryer": "Air fryer",
    "https://www.amazon.com.br/s?k=wap": "Wap",
    "https://www.amazon.com.br/s?k=extratora": "Extratora",
    "https://www.amazon.com.br/s?k=lavadora+de+alta+press%C3%A3o": "Lavadora de Alta pressão",
    "https://www.amazon.com.br/s?k=aspirador+de+p%C3%B3+robo": "Robô",
    "https://www.amazon.com.br/s?k=parafusadeira": "Parafusadeira",
    "https://www.amazon.com.br/s?k=aspirador+de+p%C3%B3+vertical": "Aspirador vertical"
}

# Função para extrair informações da página
def extract_info(url):
    driver.get(url)
    time.sleep(7)  # Esperar a página carregar completamente
    
    products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    
    # Extrair informações
    data = []
    for i, product in enumerate(products):
        if i >= 15:  # Limitar para no máximo 15 itens
            break
            
        title = "N/A"
        
        # Tentativa de encontrar o título principal
        try:
            title_span = product.find_element(By.CSS_SELECTOR, "span.a-size-base-plus.a-color-base.a-text-normal")
            title = title_span.text.strip()
        except:
            pass
        
        # Tentativa de encontrar o título alternativo
        if title == "N/A":
            try:
                title_span = product.find_element(By.CSS_SELECTOR, "span.a-truncate-cut")
                title = title_span.text.strip()
            except:
                pass
        
        data.append({
            'title': title
        })
    
    return pd.DataFrame(data)

# Função para enviar arquivos ao GitHub
def push_to_github():
    repo_dir = os.getcwd()  # Diretório do repositório
    try:
        subprocess.run(["git", "add", "."], cwd=repo_dir)
        subprocess.run(["git", "commit", "-m", "Atualização automática dos arquivos CSV"], cwd=repo_dir)
        subprocess.run(["git", "pull", "--rebase"], cwd=repo_dir)
        subprocess.run(["git", "push", "--quiet"], cwd=repo_dir)  # Adicionando --quiet para suprimir logs
    except Exception as e:
        print(f"Erro ao fazer push para o GitHub: {e}")

# Função para converter CSV para JSON e salvar
def convert_csv_to_json():
    for category, df in dataframes.items():
        json_data = df.to_json(orient='records')
        with open(f"{category}.json", 'w', encoding='utf-8') as json_file:
            json.dump(json.loads(json_data), json_file, ensure_ascii=False, indent=4)

# Loop de execução contínua
while True:
    # Extraindo dados e criando dataframes
    dataframes = {}
    for url, name in urls.items():
        print(f"Extraindo dados para a categoria: {name}")
        dataframes[name] = extract_info(url)
        time.sleep(2)  # Atraso de 2 segundos entre as requisições

    # Salvando os DataFrames em arquivos CSV
    for category, df in dataframes.items():
        df.to_csv(f"{category}.csv", index=False)

    # Converter CSV para JSON
    convert_csv_to_json()
    
    # Enviar arquivos ao GitHub
    push_to_github()
    
    # Esperar 5 minutos antes da próxima execução
    time.sleep(300)

# Fechar o driver
driver.quit()
