# django_doing_includes

Haciendo includes en django

Una forma desconzco que tan segura de hacer include en python-django parecido a php 
en la aplicación db existe un modelo de nombre Person que en el método save llama a 
otro archivo de nombre prueba.py, sobreescribiendo el método save de la clase.

Utiliza la función exec de python https://docs.python.org/3/library/functions.html?highlight=exec#exec.

Lo interesante es que prueba.py puede utilizar las variables en el contexto que se 
encuentra ejecutando.

Gracias por su opinión.
