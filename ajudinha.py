class Ajudinha:

    def qualidades(driver):
        from colorama import Fore
        from selenium.webdriver.common.by import By
        qualidades_dublado = driver.find_elements(
            By.CSS_SELECTOR, 'div > p > strong ~ [class="text-center newdawn btn btn-success"]')
        qualidades_legendado = driver.find_elements(
            By.CSS_SELECTOR, 'div > p > strong ~ [class="text-center newdawn btn btn-danger"]')

        print()
        ## Verifica se existe mais de uma opção dublada e as mostra, se não, mostra a única opção existente
        if len(qualidades_dublado) >= 2:
            print(f'{Fore.LIGHTGREEN_EX}DUBLADO{Fore.RESET}')
            for i in range(len(qualidades_dublado)):
                print(f'    {qualidades_dublado[i].get_attribute("title")}')
        else:
            if len(qualidades_dublado) != 0:
                print(f'{Fore.LIGHTGREEN_EX}DUBLADO{Fore.RESET}')
                print(f'    {qualidades_dublado[0].get_attribute("title")}')
            else:
                print(f'{Fore.RED}Esse filme/série não possui a opção de download dublado.{Fore.RESET}')

        print()
        ## Verifica se existe mais de uma opção legendada e as mostra, se não, mostra a única opção existente
        if len(qualidades_legendado) >= 2:
            print(f'{Fore.LIGHTGREEN_EX}LEGENDADO{Fore.RESET}')
            for i in range(len(qualidades_legendado)):
                print(f'    {qualidades_legendado[i].get_attribute("title")}')
        else:
            if len(qualidades_legendado) != 0:
                print(f'{Fore.LIGHTGREEN_EX}LEGENDADO{Fore.RESET}')
                print(f'    {qualidades_legendado[0].get_attribute("title")}')
            else:
                print(f'{Fore.RED}Esse filme/série não possui a opção de download legendado.{Fore.RESET}')

        return qualidades_dublado, qualidades_legendado


    def download(driver):
        from selenium.webdriver.support.expected_conditions import visibility_of_element_located
        from selenium.webdriver.support.ui import WebDriverWait
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 30).until(visibility_of_element_located(
            ('xpath', '//*[@id="carregado"]')), 'Cansei de esperar.').click()
        print('uTorrent aberto.')
        driver.quit()
        print('Navegador fechado.')


    def limpar_tela():
        import os
        """
        Limpa a tela
        """
        os.system('cls')


    def close_tab(driver):
        """
        Fecha as guias abertas indesejadas
        """
        try:
            driver.window_handles[1]
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except:
            pass


    def propaganda(driver):
        from selenium.webdriver.common.by import By
        try:
            propaganda = driver.find_elements(By.CSS_SELECTOR, 'body > div')[2]

            if propaganda:
                propaganda.click()
                Ajudinha.close_tab(driver)
        except:
            pass


    def pesquisa(driver, filme):
        from selenium.webdriver.common.by import By
        try:
            try:
                Ajudinha.propaganda(driver)
                Ajudinha.close_tab(driver)
            except:
                pass
            pesquisa = driver.find_element(By.CSS_SELECTOR, '#palavraPesquisa')
            pesquisa.click()
            pesquisa.send_keys(filme)
            driver.find_element(By.CSS_SELECTOR, '[class="btn btn-dark ml-1"]').click()
        except:
            print('Não consegui pesquisar pelo filme.')


    def opção(driver, n1 ,n2):
        opc = int(input('Opção: '))
        while opc < n1 or opc > len(n2):
            print('Essa opção não existe. Digite outra opção.')
            opc = int(input('Opção: '))
        opc -= 1
        return opc