# RANSOMWARE

Script de ransomware escrito en `python` 

# Requisitos

* Python
* Pip

# Instrucciones 

1. Instalar el modulo de `cryptography`

~~~console
$ pip install cryptography

Requirement already satisfied: cryptography in /home/metricka/.local/lib/python3.9/site-packages (38.0.1)
Requirement already satisfied: cffi>=1.12 in /home/metricka/.local/lib/python3.9/site-packages (from cryptography) (1.15.1)
Requirement already satisfied: pycparser in /home/metricka/.local/lib/python3.9/site-packages (from cffi>=1.12->cryptography) (2.21)
~~~

2. Ejecutar el archivo `main.py`

~~~console
$ python3 main.py
~~~

3. Al ejecutar aparecera un apartado para ingresar la ruta de archivos a encriptar o desencriptar, usted debera de ingresar la ruta como se muestra a continuación

~~~console
[*] RANSOMWARE [*]

[!] Ctrl + c to exit...

[+] Enter the path of the files to damage or restore them: /home/user/files
~~~

4. Seguido de esto, usted puede desencriptar o encriptar los archivos mediante el menu de opciones

~~~console
[*] OPTIONS [*]

[1] Encrypt files

[2] Decrypt files

[3] Exit

[?] Choose your option:
~~~

5. Despues de ingresar a la opción para encriptar los archivos, debera de proporcionar un mensaje para la victima

~~~console
[+] Enter a message for the victim: Bromita

[*] Encrypting files...

[+] Files encrypted successfully!
~~~

6. Al desencriptar, solamente debera de elegir la opcion para que se desencripten los archivos

~~~console
[*] Decrypting files...

[+] Files decrypted successfully!
~~~

# **METR1CKA**

> [Visitanos en DevBlogs](https://metr1cka.github.io "Pagina web")

> [Mas repositorios](https://github.com/METR1CKA?tab=repositories "Mi perfil")