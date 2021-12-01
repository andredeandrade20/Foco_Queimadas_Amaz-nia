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
    return captcha.click()
