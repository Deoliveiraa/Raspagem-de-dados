import schedule
import time
from datetime import datetime
from pywinauto import application
from pywinauto.keyboard import send_keys
import os

def atualizar_query_excel():
    # Caminho para o arquivo Excel
    arquivo_excel = r'C:\Users\joao.victor\\OneDrive - FRESNOMAQ IND DE MAQUINAS SA\\1. SQUAD DTM\\4. INSIGHTS\\João\\Projeto Loja Wap\\Base Loja Wap.xlsx'

    # Abrir o Excel usando pywinauto
    app = application.Application().start(r'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE "{}"'.format(arquivo_excel))

    try:
        # Conectar-se à janela do Excel
        window = app.window(title="Base Loja Wap.xlsx - Excel")

        # Esperar um curto período para garantir que a interface do usuário esteja totalmente carregada
        time.sleep(20)

        # Pressionar o atalho para acessar a guia "Dados"
        send_keys('%s')  # Alt + s para acessar a guia "Dados"

        # Esperar um curto período para garantir que a interface do usuário esteja totalmente carregada
        time.sleep(7)

        # Pressionar o atalho para atualizar tudo
        send_keys('%g')  # Alt + g para "Atualizar Tudo"

        # Esperar um curto período para garantir que a interface do usuário esteja totalmente carregada
        time.sleep(3)

        # Pressionar o atalho para atualizar tudo
        send_keys('%z')  # Alt + z para "Atualizar Tudo"

        # Esperar um curto período para garantir que a interface do usuário esteja totalmente carregada
        time.sleep(60)

        print("Query atualizada com sucesso em", datetime.now())

    except Exception as e:
        print("Ocorreu um erro ao atualizar a query:", e)
    

# Agendar a tarefa para ser executada todos os dias às 9h da manhã
schedule.every().day.at("09:00").do(atualizar_query_excel)

# Loop principal para verificar se há tarefas agendadas
while True:
    schedule.run_pending()
    time.sleep(60)  # Verificar a cada minuto se há tarefas agendadas para serem executadas
