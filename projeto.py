from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Configuração do driver
service = Service('C:/Users/paula/OneDrive/Área de Trabalho/chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    # Abrindo a URL
    driver.get('https://account.impacta.edu.br/')

    # Inserindo login
    login = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/form/div[1]/div/input'))
    )
    login.send_keys("2401147")

    # Inserindo senha
    senha = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/form/div[2]/div/input'))
    )
    senha.send_keys("Segredinho3297")

    print("Por favor, resolva o reCAPTCHA manualmente e pressione Enter para continuar...")
    input()  # Pausa até que o usuário pressione Enter

    # Fechar modal se existir
    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.swal2-close'))
        )
        close_button.click()
        print("Modal fechado com sucesso.")
    except TimeoutException:
        print("Nenhum modal foi encontrado.")

    # Confirmar o login
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/form/div[4]/button'))
    )
    
    # Rolando para o botão e clicando
    driver.execute_script("arguments[0].scrollIntoView(true);", confirm_button)
    time.sleep(1)  # Aguardar o botão ficar visível
    confirm_button.click()

    # Verificar redirecionamento ou mudanças após o login
    print("Aguardando redirecionamento ou mudanças na página...")
    try:
        elemento_pos_login = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "sucesso")]'))  # Ajuste para elemento esperado após login
        )
        print("Login bem-sucedido! Página carregada.")
    except TimeoutException:
        print("Nenhuma mudança detectada dentro do tempo especificado. Verifique o login ou o redirecionamento.")
    
    # Fechar pop-up de outro alerta após o login
    try:
        feche_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/button'))  # Ajuste o caminho do botão de fechar se necessário
        )
        feche_button.click()
        print("Pop-up fechado com sucesso.")
    except TimeoutException:
        print("Nenhum pop-up foi encontrado após o login.")
    
    # Tentar acessar o botão "Financeiro Online"
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
    # Tentar acessar o botão de "print_recibo"

    try:
        popup_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/button'))
        )
        print("Botão do pop-up encerrado clicado.")
        popup_button.click()
    except TimeoutException:
        print("Não foi possível encontrar o botão do pop-up.")
    # Tentar acessar o botão de "print_recibo"

    try:
        print_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//img[contains(@src, "print_recibo.png")]'))
        )
        print("Botão 'Print Recibo' encontrado.")
        print_button.click()
    except TimeoutException:
        print("Não foi possível encontrar o botão 'Print Recibo'.")

finally:
    # Esperar alguns segundos antes de encerrar
    time.sleep(5)
    driver.quit()
