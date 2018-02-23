from lxml import etree
lista = ['01','03','05','07']
doc = etree.parse('provinciasypoblaciones.xml')
provincias = doc.findall("provincias")
for provincia in provincias:
	if provincia.attrib['id'] in lista:
		print ('provincias:', provincia[0].text)
		# localidades=provincia[1].findall("localidad")
		for localidad in localidades:
				print (localidad.text)