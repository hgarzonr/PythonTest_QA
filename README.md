Steps python
-Download webDriver del navegador edge msedgedriver de selenium en directorio C:\Users\User\AppData\Local\Programs\Python\Python312\Scripts
-Los scripts se ubican en C:\Users\User\AppData\Local\Programs\Python\Python312\Scripts
-ejecución en visual studio code de los scripts:
   automationLoginTest2.py
   automationLoginTestFailed.py
   automationTestUpload.py

Steps Locust
1.Instalar Python 3.12
2.Instalar locust 
  pip install locust
3.Ejecutar locust en terminal ubicada en C:\Users\User\AppData\Local\Programs\Python\Python312\Scripts
  esto abre en http://localhost:8089/ interfaz Web el script de python para locust es locustfile.py
     Configurar el Number of users (200)
     Configurar Ramp up (5)
     Configurar Host (https://the-internet.herokuapp.com)
4.El reporte generado con los requerimientos solicitados (Tiempo de respuesta promedio de las solicitudes,
Tasa de éxito y fallos en las peticiones, Rendimiento general del sitio bajo carga concurrente) es el html report_TestLoadLocust_25092024.html
  
