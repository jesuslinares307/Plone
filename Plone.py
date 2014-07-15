
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
# -*- coding: utf8 -*-

'''
    Un conjunto, es una colección no ordenada y sin elementos repetidos. 
    Los usos básicos de éstos incluyen verificación de pertenencia y 
    eliminación de entradas duplicadas.
'''

# crea un conjunto sin repetidos
plato = ['pastel', 'tequeno', 'papa', 'empanada', 'mandoca', 'queso']
print plato
print type(plato)
bebida = ['refresco', 'malta', 'jugo', 'cafe']
print bebida
print type(bebida)

# establece un conjunto a una variable
para_comer = set(plato)
print para_comer
print type(para_comer)

para_tomar = set(bebida)
print para_tomar
print type(para_tomar)

# Ejemplo practico de los condicionales
hay_tequeno = 'tequeno' in para_comer
hay_fresco = 'refresco' in para_tomar

print "\nTostadas A que Pipo!"
print "===================="

# valida si un elemento esta en el conjunto
print "Teneis tequeno?: ", 'tequeno' in para_comer

# valida si un elemento esta en el conjunto
print "Teneis pa tomar fresco?: ", 'refresco' in para_tomar

if (hay_tequeno and hay_fresco):
	print "Desayuno vergatario"
else:
    print "Desayuno ligero"