from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
provincias = doc.xpath("/lista/provincia")
for provincia in provincias:
	num_loc = provincia.xpath("count(localidades/localidad)")
	nombre_prov = provincia.find("nombre")
	print (" %s: %d localidades" % (nombre_prov.text,num_loc))