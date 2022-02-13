import cProfile

import Practica_3

print("Profiling de la funccion 'PuntoX' ")
cProfile.run('Practica_3.PuntoX()')

print("Profiling de la funccion 'PuntoY' ")
cProfile.run('Practica_3.PuntoY(1)')

print("Profiling de la funccion 'Quadrant' ")
cProfile.run('Practica_3.Quadrant(9, -7)')