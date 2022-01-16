#! /usr/bin/python

#INTEGRANTES: Jaime Guerrero Carrasco, Jorge Molina Lafuente y Juan Gonzalez Jimenez

from subprocess import call
import sys
import subprocess
import json
import os

#OBTENEMOS EL VALOR DE LA VARIABLE DE ENTORNO
numero_de_grupo = str(os.environ.get('GROUP_NUMBER'))

call(['sudo apt-get update'], shell=True)
call(['sudo apt-get install nano'], shell=True)

#MODIFICA EL TITULO Y ARRANCA LA APLICACION EN EL PUERTO :9999
call(['cp '+cwd+'/practica_creativa2/bookinfo/src/productpage/templates/productpage.html '+cwd+'/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html'], shell=True)
copia = open( cwd + '/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html', 'r')
f = open( cwd + '/practica_creativa2/bookinfo/src/productpage/templates/productpage.html', 'w')
for line in copia:
    if "{% block title %}Simple Bookstore App{% endblock %}" in line:
        f.write("{% block title %}" + numero_de_grupo + "{% endblock %}")
    else:
        f.write(line)
f.close()
copia.close()
call(['rm '+cwd+'/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html'],shell=True)

