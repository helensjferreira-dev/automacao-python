#Passo a passo para cadastrar produtos
# Entrar no site 
# Fazer login
# Importar base de dados
# Cadastrar 1 Produto
# Repetir o processo para todos os produtos

#pyautogui - controlar o mouse e o teclado do computador atraves do python. Não vem instalado no python
# Instalação via terminal: pip install pyautogui
# Iniciando pyautogui
import pyautogui
import time, subprocess, os
import pandas as pd

pyautogui.PAUSE = 1.5

#Opção usando subprocess ou os
# chrome_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# abrir o chrome no python
# subprocess.Popen(chrome_path)

#Outra forma de abrir o chrome diretamente usando os

#time.sleep(5)
#Precisamos incluir o tempo de carregamento da pagina


#pyautogui.write("site")
os.startfile("https://helensjferreira-dev.github.io/automacao-python/templates/index.html")
time.sleep(20)
#Usando foco na barra de url e tab
#pyautogui.hotkey("ctrl","l")
#pyautogui.press("tab")
#Usando as coordenadas do campo a ser preenchido
#Pega as coordenadas usando auxiliar.py
pyautogui.click(x=515, y=281)
#Dessa forma,se o navegador abrir algum popup, ele foca no campo que precisa ser preenchido
#pyautogui.press("tab")
pyautogui.write("email@email.com")
time.sleep(3)
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("tab")

#Importar base de dados
df_products_final = pd.read_csv("./data/products_sample.csv")
# Para cada linha da tabela: 
# Se fossem colunas, seria: for coluna in df_products.columns:

print(df_products_final)

for linha in df_products_final.index: #indice
    #Posicionar click primeiro campo
    pyautogui.click(x=521, y=279)
    codigo = df_products_final.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = df_products_final.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = df_products_final.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(df_products_final.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(df_products_final.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(df_products_final.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(df_products_final.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    #rolar a pagina ao topo usando o scroll
    #numero positivo up / negativo down
    pyautogui.scroll(10000)
    pyautogui.click(x=521, y=279)

#Pausar automação (FAILSAFE) - trava de segurança: mouse parado no canto superior esquerdo
    