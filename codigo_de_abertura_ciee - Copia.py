from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

opera_driver_path = r"SEU_CAMINHO_OPERADRIVER"

opera_gx_path = r"SEU_CAMINHO_OPERA_GX"

# Função para calcular o tempo até 23:41
def aguardar_ate_2341():
    agora = datetime.now()
    # Defina a hora de abertura como 23:41
    alvo = agora.replace(hour=23, minute=41, second=0, microsecond=0)
    
    # Se já passou das 23:41, aguarda até o próximo dia
    if agora > alvo:
        alvo = alvo.replace(day=agora.day + 1)
    
    # Calcula a diferença de tempo
    tempo_restante = (alvo - agora).total_seconds()
    print(f"Aguardando até {alvo.strftime('%H:%M')} para abrir o site...")
    
    # Espera até o horário desejado
    time.sleep(tempo_restante)

# Aguarda até 23:41
aguardar_ate_2341()

# Configuração do Opera GX com OperaDriver
options = webdriver.ChromeOptions()
options.binary_location = opera_gx_path  # Usar Opera GX

# Inicializa o navegador Opera GX com OperaDriver
driver = webdriver.Opera(executable_path=opera_driver_path, options=options)

# Abre o site
print("Abrindo o site...")
driver.get("https://cieeaprendiz.ciee.org.br")

# Aguarda o site carregar
time.sleep(3)

# Encontrar os campos de login e senha usando os IDs corretos
campo_usuario = driver.find_element(By.ID, "login") 
campo_senha = driver.find_element(By.ID, "password") 

# Preenche os campos de login e senha
campo_usuario.send_keys("SEU_LOGIN") 
campo_senha.send_keys("SUA_SENHA") 

# Envia o formulário (pressiona Enter)
campo_senha.send_keys(Keys.RETURN)

# Aguarda o login ser realizado
time.sleep(5)

# O navegador ficará aberto até você fechá-lo manualmente.
input("Pressione Enter para finalizar o script. O navegador continuará aberto até lá.")
