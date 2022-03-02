from distutils.command.build_scripts import build_scripts
from sys import builtin_module_names
import vehiculos

bus_escolar = vehiculos.Bus('Bus escolar',80,100_000)
print(bus_escolar)