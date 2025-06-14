import genai

def obtener_consejo_ia_gemini(api_key_gemini, temperatura, condicion_clima, viento, humedad):
    """
    Obtiene un consejo de vestimenta usando la API de Gemini.
    """
    try:
        genai.configure(api_key=api_key_gemini)
        # Configuración del modelo (pueden explorar diferentes modelos si lo desean)
        # Para generación de texto simple, 'gemini-pro' suele ser una buena opción.
        model = genai.GenerativeModel('gemini-pro')
        # Diseñar el prompt (este es un ejemplo, ustedes deben crear el suyo)
        # Es importante dar contexto y ser específico para obtener mejores resultados.
        prompt_diseñado_por_equipo = (
        f"PROMPT"
        )
        print("\nGenerando consejo de vestimenta con IA...")
        # Generar contenido
        response = model.generate_content(prompt_diseñado_por_equipo)
        # Asegurarse de que hay texto en la respuesta
        if response.text:
            return response.text
        else:
            # A veces la API puede no devolver texto si hay problemas con el prompt o filtros de seguridad
            # Investigar response.prompt_feedback si hay problemas
            print("La IA no pudo generar un consejo. Razón (si está disponible):", response.prompt_feedback)
            return "No se pudo generar un consejo en este momento."
    except Exception as e:
        print(f"Error al contactar la API de Gemini o procesar la respuesta: {e}")
        return "Error al generar el consejo de IA."