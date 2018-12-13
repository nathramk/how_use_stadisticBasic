#from ejer1_f.function_me import myClass
from stadistic_basic.stadisticBasic import StaditicBasic

a = int(input("enter number: ")) # ingresa cantidad de poblacion
		
c = []
for i in range(a): # agrega en una lista los datos de la poblacion
	z = int(input("enter dates: "))
	c.append(z)

suma = StaditicBasic.sums(c)

tamanio = len(c)
calculo = suma/tamanio #calcula el promedio muestral
ss = StaditicBasic.desviacion_estandar(c, calculo, tamanio)

nivel_signi = int(input("ingrese nivel de significacia %: " ))
meida_pobla = int(input("ingrese media poblacional: "))
regla = int(input("canridad de colas para la regla de decicion: "))

signi = StaditicBasic.nivel_significancia(nivel_signi)
regl_decicion = StaditicBasic.regla_decicion(regla, signi)
signisss = signi/2
if regla == 2:
	a=regl_decicion*-1
	b=regl_decicion
if regla == 1:
	a=0
	b=regl_decicion

t = (calculo-meida_pobla)/(ss/(tamanio**0.5))

conlucion = StaditicBasic.validacion_conclucion(t, b, a)

print("\n\nDATOS: \nu: {}, \nn: {}, \nx: {},\ndesviacion estandar(s): {}".format(meida_pobla,tamanio,calculo, ss))
print("\nHIPOTESIS: \nH0: u = {} \nHa: u > {} \n\nNIVEL DE SIGNIFICANCIA: {}  \n\nPRUEVA ESTADISTICA: t=(x-u)/(s/(n**0.5)) \n\nREGLA DE DECICION: {} <:gaus:> {} \nand a/2= {} \n\nCALCULOS: {} \n\nCONCLUCION: {}".format(meida_pobla,meida_pobla,signi,a,b,signisss,t, conlucion))











