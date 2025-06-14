import os
import requests
import json
import dotenv

# Cargar variables de entorno desde un archivo .env
dotenv.load_dotenv()

OPEN_WEATHER_API_URL = os.environ.get("OPEN_WEATHER_API_URL")

def obtener_clima_ciudad_owm(ciudad, api_key):
    base_url = OPEN_WEATHER_API_URL

    print(f"URL base de OpenWeatherMap: {base_url}")
    print(f"API Key de OpenWeatherMap: {api_key}")

    parametros = {
        'q': ciudad,
        'appid': api_key,
        'units': 'metric',
        'lang': 'es'
    }
    print(f"\nConsultando el clima (OpenWeatherMap) para: {ciudad}...")
    try:
        respuesta = requests.get(base_url, params=parametros, timeout=10)
        respuesta.raise_for_status()
        datos_clima = respuesta.json()
        return datos_clima
    except requests.exceptions.HTTPError as errh:
        if respuesta.status_code == 401:
            print(f"❌ Error de autenticación OWM: API Key inválida.")
        elif respuesta.status_code == 404:
            print(f"❌ Error OWM: Ciudad '{ciudad}' no encontrada.")
        else:
            print(f"❌ Error HTTP OWM: {errh}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"❌ Error de conexión/petición OWM: {err}")
        return None
    except json.JSONDecodeError:
        print("❌ Error OWM: La respuesta de la API no es JSON válido.")
    return None

    # --- Ejemplo de cómo extraer datos (dentro de tu lógica de Opción 1) ---
    # mi_clave_owm = "TU_OPENWEATHERMAP_API_KEY"
    # datos_clima_recibidos = obtener_clima_ciudad_owm("Buenos Aires", mi_clave_owm)
    # if datos_clima_recibidos:
    # try:
    # temperatura = datos_clima_recibidos['main']['temp']
    # descripcion = datos_clima_recibidos['weather'][0]['description']
    # # ... extraer más datos según necesidad ...
    # print(f"Temperatura en Buenos Aires: {temperatura}°C, {descripcion.capitalize()}")
    # except KeyError:
    # print("Error: Formato inesperado en datos de OWM.")