# Guardián Clima ITBA

Guardián Clima ITBA es una aplicación de consola para consultar el clima actual de una ciudad, guardar el historial de consultas y obtener consejos personalizados usando IA.

## Estructura de Módulos

- **main.py**  
  Es el punto de entrada de la aplicación. Muestra un menú interactivo que permite al usuario:
  - Consultar el clima actual y guardar la consulta en un historial global.
  - Ver el historial personal de consultas por ciudad.
  - Obtener estadísticas globales y exportar el historial completo.
  - Recibir consejos de IA sobre cómo vestirse según el clima.
  - Ver información sobre el proyecto y cerrar sesión.

- **consultar_clima.py**  
  Contiene funciones para interactuar con la API de OpenWeatherMap.  
  - `obtener_clima_ciudad_owm(ciudad, api_key)`: Consulta el clima actual de una ciudad usando la API y devuelve los datos en formato JSON.

- **consultar_ia.py**  
  (Pendiente de implementación)  
  Este módulo está destinado a integrar funcionalidades de inteligencia artificial, como consejos personalizados sobre vestimenta según el clima.

- **.env**  
  Archivo de variables de entorno. Aquí se almacenan claves API y configuraciones sensibles que no deben subirse al repositorio.

## Requisitos

- Python 3.10+
- Las dependencias necesarias están listadas en `requirements.txt`.

## Instalación

1. Clona el repositorio.
2. Crea un entorno virtual y actívalo:
   ```sh
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```
3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
4. Crea un archivo `.env` en la carpeta `src/` con tus claves de API:
   ```
   OPEN_WEATHER_API_URL=https://api.openweathermap.org/data/2.5/weather
   OPEN_WEATHERMAP_API_KEY=TU_API_KEY
   ```

## Uso

Ejecuta la aplicación desde la carpeta `src`:
```sh
python main.py
```

---

**Autores:**  
Proyecto de ejemplo para ITBA.
