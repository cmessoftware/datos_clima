import json
from consultar_clima import obtener_clima_ciudad_owm
import dotenv
import os
import pandas as pd
dotenv.load_dotenv()

OPEN_WEATHERMAP_API_KEY = "cfdf93a93583d251d8c01ec7f2c3ab5c" #os.environ.get("OPEN_WEATHERMAP_API_KEY")


def mostrar_menu():
    print("=== Guardián Clima ITBA ===")
    print("1. Consultar Clima Actual y Guardar en Historial Global")
    print("2. Ver Mi Historial Personal de Consultas por Ciudad")
    print("3. Estadísticas Globales de Uso y Exportar Historial Completo")
    print("4. Consejo IA: ¿Cómo Me Visto Hoy?")
    print("5. Acerca De...")
    print("6. Cerrar Sesión")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        if opcion == "1":
            print("Funcionalidad: Consultar Clima Actual y Guardar en Historial Global")
            datos_clima = obtener_clima_ciudad_owm("Buenos Aires", OPEN_WEATHERMAP_API_KEY)
            datos_clima_df = pd.json_normalize(datos_clima)  # Convertir a DataFrame para guardar en historial
            print("Datos del clima recibidos:", datos_clima_df.T)
        elif opcion == "2":
            print("Funcionalidad: Ver Mi Historial Personal de Consultas por Ciudad")
            # TODO: Implementar funcionalidad
        elif opcion == "3":
            print("Funcionalidad: Estadísticas Globales de Uso y Exportar Historial Completo")
            # TODO: Implementar funcionalidad
        elif opcion == "4":
            print("Funcionalidad: Consejo IA: ¿Cómo Me Visto Hoy?")
            # TODO: Implementar funcionalidad
        elif opcion == "5":
            print("Guardián Clima ITBA - Proyecto de ejemplo para consulta y análisis de clima.")
        elif opcion == "6":
            print("Cerrando sesión. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
   main()