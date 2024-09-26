# As a user
#Given que existe un usuario con un archivo válido para cargar
#And el usuario carga un archivo válido en el botón de carga
#When selecciona el botón "Upload"
#Then el usuario carga satisfactoriamente su archivo
#And el usuario visualiza el siguiente mensaje "File Uploaded!"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()

# Abrir la página de carga de archivos
driver.get("https://the-internet.herokuapp.com/upload")

# Esperar a que la página cargue completamente
time.sleep(3)

# Encontrar el campo de carga de archivos e ingresar la ruta del archivo
upload_field = driver.find_element(By.ID, "file-upload")
upload_field.send_keys("C:\Users\ingha\Downloads\LD.png")

# Emular el clic en el botón de subir
upload_button = driver.find_element(By.XPATH, "//button[@type='submit']")
upload_button.click()

# Esperar a que el mensaje de éxito aparezca
time.sleep(3)

# Confirmar que el mensaje de éxito está presente
success_message = driver.find_element(By.ID, "uploaded-files")
assert "File Uploaded!" in success_message.text

# Cerrar el navegador
driver.quit()
