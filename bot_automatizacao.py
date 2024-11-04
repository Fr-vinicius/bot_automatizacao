import pyautogui
import pandas as pd
import time

Tabela = pd.read_csv('produtos.csv')

Link = 'dlp.hashtagtreinamentos.com/python/intensivao/login'
Email = 'ederson@email.com'
Senha = 'edersonsenha123'

pyautogui.PAUSE = .3

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(1)

pyautogui.write(Link)
pyautogui.press('enter')

time.sleep(2)

pyautogui.click(x=443, y=382)
pyautogui.write(Email)
pyautogui.press('tab')
pyautogui.write(Senha)
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(.5)

for linha in Tabela.index:
    pyautogui.click(x=428, y=274)

    pyautogui.write(Tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')
    pyautogui.write(Tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    pyautogui.write(Tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    pyautogui.write(str(Tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(Tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(Tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    if not pd.isna(Tabela.loc[linha, 'obs']):
        pyautogui.write(Tabela.loc[linha, 'obs'])

    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(450)
