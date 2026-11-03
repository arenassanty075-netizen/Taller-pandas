from carga import cargar_datos
from limpieza import limpiar_clientes

clientes, ventas = cargar_datos()
"""
print("\n--- TAMAÑO DE LAS TABLAS ---")
print("Clientes:", clientes.shape)
print("Ventas:", ventas.shape)

print("\n--- INFORMACIÓN DE CLIENTES ---")
clientes.info()

print("\n--- INFORMACIÓN DE VENTAS ---")
ventas.info()

print("\n--- RESUMEN DE CLIENTES ---")
print(clientes.describe())

print("\n--- RESUMEN DE VENTAS ---")
print(ventas.describe())
"""
print("Ciudades ANTES de la limpieza:")
print(clientes["ciudad"].unique())


clientes_limpios = limpiar_clientes(clientes)

print("\nCIUDADES DESPUÉS:")
print(clientes_limpios["ciudad"].unique())