import pygetwindow as gw

def encontrar_janela_excel():
    for window in gw.getAllTitles():
        if "Excel" in window:
            print(window)

# Chamar a função para encontrar a janela do Excel
encontrar_janela_excel()
