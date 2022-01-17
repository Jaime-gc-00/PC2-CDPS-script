#! /usr/bin/python

#INTEGRANTES: Jaime Guerrero Carrasco, Jorge Molina Lafuente y Juan Gonzalez Jimenez

from subprocess import call
import sys
import subprocess
import json
import os

cwd = str(os.getcwd())
#puerto_de_arranque = str(2022)

#CREAMOS LA VARIABLE DE ENTORNO
#os.environ['GROUP_NUMBER']="Equipo 40"
#OBTENEMOS EL VALOR DE LA VARIABLE DE ENTORNO
#numero_de_grupo = str(os.environ.get('GROUP_NUMBER'))

#Descarga de la aplicacion 
call(['sudo git clone https://github.com/CDPS-ETSIT/practica_creativa2.git'], shell=True)

#INSTALACION DE REQUIRMENTS CON PIP
call(['pip3 install -r '+cwd+'/practica_creativa2/bookinfo/src/productpage/requirements.txt'], shell=True)

#MODIFICA EL TITULO
#call(['cp '+cwd+'/practica_creativa2/bookinfo/src/productpage/templates/productpage.html '+cwd+'/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html'], shell=True)
#copia = open( cwd + '/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html', 'r')
#f = open( cwd + '/practica_creativa2/bookinfo/src/productpage/templates/productpage.html', 'w')
#for line in copia:
#    if "{% block title %}Simple Bookstore App{% endblock %}" in line:
#        f.write("{% block title %}" + numero_de_grupo + "{% endblock %}")
#    else:
#        f.write(line)
#f.close()
#copia.close()
#call(['rm '+cwd+'/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html'],shell=True)


