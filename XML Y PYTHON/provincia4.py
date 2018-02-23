nombre=input("Introduzca una provincia: ")
from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
municipios=doc.findall("provincia/localidades/localidad")
for localidad in municipios:
	print (localidad.text)