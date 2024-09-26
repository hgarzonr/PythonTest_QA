# As a user
#Given que existe un usuario con credenciales válidas
#When selecciona el botón "Login"
#Then el usuario es autenticado satisfactoriamente
#And el usuario visualiza el siguiente mensaje de confirmación "You logged into a secure area!"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(5)
# Encontrar el campo de nombre de usuario e ingresar el valor
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

# Encontrar el campo de contraseña e ingresar el valor
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

# Emular el clic en el botón de inicio de sesión
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Confirmar que el usuario se autenticó satisfactoriamente
success_message = driver.find_element(By.ID, "flash-messages")
assert "You logged into a secure area!" in success_message.text

# Esperar unos segundos para observar el resultado
time.sleep(5)

# Cerrar el navegador
driver.quit()