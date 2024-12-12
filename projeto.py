from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


service = Service('C:/Users/paula/OneDrive/Área de Trabalho/chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    
    driver.get('https://account.impacta.edu.br/')


    login = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/form/div[1]/div/input'))
    )
    login.send_keys("****")

    
    senha = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/form/div[2]/div/input'))
    )
    senha.send_keys("*****")

    print("Por favor, resolva o reCAPTCHA manualmente e pressione Enter para continuar...")
    input()  
    
    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.swal2-close'))
        )
        close_button.click()
        print("Modal fechado com sucesso.")
    except TimeoutException:
        print("Nenhum modal foi encontrado.")


    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/form/div[4]/button'))
    )
    
  
    driver.execute_script("arguments[0].scrollIntoView(true);", confirm_button)
    time.sleep(1)
    confirm_button.click()

    print("Aguardando redirecionamento ou mudanças na página...")
    try:
        elemento_pos_login = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "sucesso")]'))  # Ajuste para elemento esperado após login
        )
        print("Login bem-sucedido! Página carregada.")
    except TimeoutException:
        print("Nenhuma mudança detectada dentro do tempo especificado. Verifique o login ou o redirecionamento.")

    try:
        feche_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/button'))  # Ajuste o caminho do botão de fechar se necessário
        )
        feche_button.click()
        print("Pop-up fechado com sucesso.")
    except TimeoutException:
        print("Nenhum pop-up foi encontrado após o login.")
    
    try:
        financeiro_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/ul[1]/li[5]/a'))
        )
        print("Botão 'Financeiro Online' encontrado e clicado.")
        financeiro_button.click()
    except TimeoutException:
        print("Não foi possível encontrar o botão 'Financeiro Online'.")

    try:
        financeiro2_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/ul[1]/li[5]/ul/li[1]/a'))
        )
        print("Botão 'Financeiro Online' encontrado e clicado.")
        financeiro2_button.click()
    except TimeoutException:
        print("Não foi possível encontrar o botão 'Financeiro Online'.")


    try:
        popup_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/button'))
        )
        print("Botão do pop-up encerrado clicado.")
        popup_button.click()
    except TimeoutException:
        print("Não foi possível encontrar o botão do pop-up.")


    try:
        print_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//img[contains(@src, "print_recibo.png")]'))
        )
        print("Botão 'Print Recibo' encontrado.")
        print_button.click()
    except TimeoutException:
        print("Não foi possível encontrar o botão 'Print Recibo'.")

finally:
    time.sleep(5)
    driver.quit()
