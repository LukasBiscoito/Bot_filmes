import os
from ajudinha import Ajudinha
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

Ajudinha.limpar_tela()

filme = input('Oque deseja baixar ?  ')

options = webdriver.ChromeOptions()
options.add_argument(
    "--user-data-dir=C:\\Users\\Lukas\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument('--profile-directory=Default')
options.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"

Ajudinha.limpar_tela()
print(f'Buscando por {filme.upper()}')

driver = webdriver.Chrome(options=options)
driver.maximize_window()
Ajudinha.limpar_tela()
driver.get('https://ondebaixa.com')

Ajudinha.limpar_tela()
Ajudinha.propaganda(driver)
Ajudinha.pesquisa(driver, filme)

# lista os filmes
filmes = driver.find_elements(By.CSS_SELECTOR, '[class="info_capa"]')
# Encontra o HREF do filme
links = driver.find_elements(By.CSS_SELECTOR, '[class="info_capa"] > h3 > a')

Ajudinha.limpar_tela()

while len(filmes) == 0:
    print('Não encontramos nada com esse nome.')
    print('Vamos tentar novamente.')
    filme = input('Oque deseja baixar ?  ')
    Ajudinha.pesquisa(driver, filme)
    filmes = driver.find_elements(By.CSS_SELECTOR, '[class="info_capa"]')
    links = driver.find_elements(
        By.CSS_SELECTOR, '[class="info_capa"] > h3 > a')

for i in range(len(filmes)):
    print('═' * os.get_terminal_size().columns)
    print(f'=-=-=-=- {i + 1} -=-=-=-=')
    print(filmes[i].text)
    href = {f'{i}': {links[i]}}
    print('═' * os.get_terminal_size().columns)

opc = Ajudinha.opção(driver, 0, filmes)

print(links[opc].text)
driver.get(links[opc].get_attribute('href'))

Ajudinha.limpar_tela()

qualidades = Ajudinha.qualidades(driver)

opcs = ['DUBLADO', 'LEGENDADO']
if len(qualidades[0]) and len(qualidades[1]) != 0:
    print()
    print(f'1. {opcs[0]}')
    print(f'2. {opcs[1]}')

    lingua = int(input('Opção para a língua: '))
    while 1 < lingua > 2:
        print('Essa opção não existe. Digite outra opção.')
        lingua = int(input('Opção para a língua: '))
    lingua -= 1
elif len(qualidades[0]) >= 1:
    lingua = 0
else:
    lingua = 1

# Verifica se existe apenas uma opção para a língua escolhida
if len(qualidades[lingua]) == 1:
    print('Selecionamos a única opção para a língua escolhida:')
    print(f'    {qualidades[lingua][0].get_attribute("title")}')
    qualidades[lingua][0].click()

# Verifica se existe apenas a linguagem escolhida
elif len(qualidades[lingua]) >= 2:
    qualidade = int(input('Opção para qualidade: '))
    while qualidade < 1 or qualidade > len(qualidades[lingua]):
        print('Essa opção não existe. Digite outra opção.')
        qualidade = int(input('Opção para qualidade: '))
    qualidade -= 1
    print(f'    {qualidades[lingua][qualidade].get_attribute("title")}')
    qualidades[lingua][qualidade].click()
else:
    print()
    qualidade = int(input('Opção para qualidade: '))
    while qualidade < 1 or qualidade > len(qualidades[lingua]):
        print('Essa opção não existe. Digite outra opção.')
        qualidade = int(input('Opção para qualidade: '))
    qualidade -= 1

    if lingua == 0:
        print(f'    {qualidades[0][qualidade].get_attribute("title")}')
    else:
        print(f'    {qualidades[1][qualidade].get_attribute("title")}')

    qualidades[lingua][qualidade].click()

Ajudinha.propaganda(driver)
Ajudinha.close_tab(driver)
driver.quit()
print('Navegador fechado.')
print('uTorrent aberto.')
