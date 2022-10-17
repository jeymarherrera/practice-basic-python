# TIPO DE MODULOS
# modulos escritos por uno mismo
import jmath

jmath.add(1,2)


from jmath import add, substract

substract(4,3)
add(5,6)

# modulos descargados PYPI

#from colorama import Fore, Style, init
#init(convert=True)
#print(Fore.BLUE + "Hello World")

# modulos de bibliotecas de python #python modules index #pip modules
import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes=70))


from datetime import timezone, date

print(date.today())