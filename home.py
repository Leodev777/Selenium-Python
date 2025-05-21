import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Iniciar el navegador
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


# Esperar hasta que el campo de usuario esté presente y visible
wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))

# Asegurarse de que el campo sea interactuable antes de escribir
time.sleep(3)  # Pequeña pausa extra para evitar problemas de carga
username_field.click()  # Hacer clic para asegurarse de que el campo tiene foco
username_field.send_keys("Admin")  # Escribir usuario

# Buscar el campo de contraseña y escribir
password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys("admin123")  

# Hacer clic en el botón de Login
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.send_keys(Keys.ENTER)

# Esperar un poco para ver el resultado antes de cerrar
time.sleep(3)

# Ingresar al item Admin del menú
admin_menu = driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(1) > a > span")
admin_menu.click()
add_button = driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div.orangehrm-header-container > button")
add_button.click()

time.sleep(45)

print("Sin errores")
