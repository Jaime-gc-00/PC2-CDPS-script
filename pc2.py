#! /usr/bin/python

#INTEGRANTES: Jaime Guerrero Carrasco, Jorge Molina Lafuente y Juan Gonzalez Jimenez

from subprocess import call
import sys
import subprocess
import json
import os

cwd = str(os.getcwd())

#CREAMOS LA VARIABLE DE ENTORNO
numero_de_grupo = str(os.environ.get('GROUP_NUMBER'))

#Descarga de la aplicacion 
call(['git clone https://github.com/CDPS-ETSIT/practica_creativa2.git'], shell=True)

#INSTALACION DE REQUIRMENTS CON PIP
call(['pip3 install -r /practica_creativa2/bookinfo/src/productpage/requirements.txt'], shell=True)

#MODIFICA EL TITULO
call(['cp /practica_creativa2/bookinfo/src/productpage/templates/productpage.html '+cwd+'/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html'], shell=True)
copia = open('/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html', 'r')
f = open('/practica_creativa2/bookinfo/src/productpage/templates/productpage.html', 'w')
for line in copia:
    if "{% block title %}Simple Bookstore App{% endblock %}" in line:
        f.write("{% block title %}" + numero_de_grupo + "{% endblock %}")
    else:
        f.write(line)
f.close()
copia.close()
call(['rm /practica_creativa2/bookinfo/src/productpage/templates/productpage2.html'],shell=True)


