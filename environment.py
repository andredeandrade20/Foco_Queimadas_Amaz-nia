from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import solve_captchas_with_model as solvecap
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys

## Carrega a planilha de Excel com os cnpjs
def loadData():
    chunks = []
    for chunk in pd.read_csv('C:/Users/Ygoor/Desktop/Freelas/FreeWeb/solver/dados.csv', encoding = 'UTF-8', sep = ',', low_memory = True, chunksize=1000):
        chunks.append(chunk)
    df = pd.concat(chunks)
    return df

## Abre o navegador no site da prefeitura
navegador = webdriver.Chrome(executable_path = 'C:/Users/Ygoor/Desktop/Freelas/FreeWeb/solver/chromedriver')
navegador.get('https://ccm.prefeitura.sp.gov.br/login/contribuinte?tipo=F')


## Função para inserir os valores do cnpj pelo banco de dados fornecido
def InputCNPJ(cnpj):
    find_cnpj = navegador.find_element(By.ID, "input-usuario")
    find_cnpj.click()
    return find_cnpj.send_keys(cnpj)

## Função para inserir os valores do captcha pela rede neural
def InputCaptcha():
    captcha = navegador.find_element(By.ID, "input-captcha")
    captcha.click()
    break_captcha = solvecap.SolveCaptcha()
    break_captcha = break_captcha.lower()
    return(captcha.send_keys(break_captcha))

def EnterValues():
    enter = navegador.find_element(By.ID, 'btnEntrar')
    enter.click()
    try:
        WebDriverWait(navegador, 3).until(EC.alert_is_present(),"Alerta demorou muito, ocorreu algum erro")
        alert = navegador.switch_to.alert
        alert.accept()

    except TimeoutException:
        print("no alert")

def RunHack():
    df = loadData()
    cnpj = df.iloc[0,1]
    x = navegador.get('https://ccm.prefeitura.sp.gov.br/login/contribuinte?tipo=F')
    for x in range (sys.maxsize**100):
        try:
            InputCNPJ(cnpj)
            InputCaptcha()
            EnterValues()
        except :
            break
