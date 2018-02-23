from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
provincia=doc.findall('provincia/nombre')
for nombre in provincia:
	print (nombre.text)