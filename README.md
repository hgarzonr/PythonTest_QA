<div class="markdown-heading" dir="auto">
<h2 class="heading-element" dir="auto" tabindex="-1"><strong>Steps Automation python</strong></h2>
<a id="user-content-instalaci&oacute;n" class="anchor" href="https://github.com/joseluisgs/testing-js-cypress#instalaci%C3%B3n" aria-label="Permalink: Instalaci&oacute;n"></a></div>
<p dir="auto">Download webDriver del navegador edge msedgedriver de selenium en directorio C:\Users\User\AppData\Local\Programs\Python\Python312\Scripts.</p>
<p dir="auto">Los scripts se ubican en C:\Users\User\AppData\Local\Programs\Python\Python312\Scripts<br />La ejecuci&oacute;n se recomienda hacerla en visual studio code de los scripts:</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto">
<pre>  automationLoginTest2.py<br />&nbsp; automationLoginTestFailed.py<br />&nbsp; automationTestUpload.py</pre>
</div>
<p dir="auto">&nbsp;</p>
<div class="markdown-heading" dir="auto">
<h2 class="heading-element" dir="auto" tabindex="-1"><strong>Steps Test Load Locust</strong></h2>
<a id="user-content-ejecutando-cypress" class="anchor" href="https://github.com/joseluisgs/testing-js-cypress#ejecutando-cypress" aria-label="Permalink: Ejecutando Cypress"></a></div>
<p dir="auto">1.Instalar Python 3.12<br />2.Instalar locust</p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto">
<div class="zeroclipboard-container">&nbsp;</div>
</div>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto">
<pre>&nbsp;pip install locust</pre>
<p>3.Ejecutar locust en terminal ubicada en C:\Users\User\AppData\Local\Programs\Python\Python312\Scripts con el comando locust<br />esto despliega la interfaz web en http://localhost:8089/ interfaz Web el script de python para locust es</p>
<p>locustfile.py</p>
<p>&nbsp;*Configurar el Number of users (200)<br />&nbsp;*Configurar Ramp up (5)<br />&nbsp;*Configurar Host (<a href="https://the-internet.herokuapp.com/" rel="nofollow">https://the-internet.herokuapp.com</a>)<br />4.El reporte generado con los requerimientos solicitados (Tiempo de respuesta promedio de las solicitudes,<br />Tasa de &eacute;xito y fallos en las peticiones, Rendimiento general del sitio bajo carga concurrente) es el html report_TestLoadLocust_25092024.html que se encuentra en el presente repositorio.</p>
<p dir="auto">&nbsp;</p>
</div>
