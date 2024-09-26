#As a user load Test
#Given un grupo de 200 usuarios concurrentes 
#And el usuario ingresa a la página de inicio
#And el usuario se autentica con credenciales válidas
#And el usuario accede a la sección File Download y realiza una descarga
#When la prueba concurrente es ejecutada por un periodo de 10 minutos con una espera de 5 segundos entre usuarios concurrentes
#Then se evidencia un informe de prueba de carga (capacidad) del sistema

from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    @task
    def Home_site(self):
        self.client.get("")
    
    def login(self):
        self.client.post("/authenticate", {
            "username": "tomsmith",
            "password": "SuperSecretPassword!"
            
        })
     
    @task
    def download_file(self):
        with self.client.get("/download/LD.png", stream=True) as response:
            if response.status_code == 200:
                with open("LD", "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
        
