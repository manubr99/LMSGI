from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
poblacion = input("Seleccione un municipio: ")
provincias=doc.findall("provincia")
for provincia in provincias:
	localidades=provincia[1].findall("localidad")
	for localidad in localidades:
		if localidad.text == poblacion:
			print (provincia[0].text)