
import streamlit as st

# Títulos de las preguntas
questions = [
    "¿Qué es una infraestructura verde (GI)?",
    "¿Cuáles son los principales desafíos urbanos abordados por las GIs?",
    "¿Qué son los servicios ecosistémicos?",
    "¿Qué es una solución basada en la naturaleza (NBS)?",
    "¿Qué diferencia existe entre infraestructura verde y gris?",
    "¿Cómo afecta la urbanización al ciclo hidrológico?",
    "¿Qué rol juega el cambio climático en el incremento de amenazas hidro-meteorológicas?",
    "¿Qué es la isla de calor urbana?",
    "¿Qué tipo de beneficios co-laterales ofrece la GI?",
    "¿Cómo las GIs reducen el volumen de escorrentía superficial?",
    "¿Cuáles son las funciones principales de las GIs?",
    "Menciona al menos cinco tipos de infraestructura verde.",
    "¿Qué es un sistema híbrido gris-verde?",
    "¿Qué GIs son más efectivas para infiltración?",
    "¿Qué beneficios ofrecen los techos verdes?",
    "¿Qué es un modelo hidrológico-hidráulico?",
    "¿Qué variables se requieren para el modelado hidráulico?",
    "¿Qué indicadores se utilizan para evaluar GIs?",
    "¿Qué representa el indicador 'tiempo al pico'?",
    "¿Qué representa la eficiencia de infiltración?",
    "¿Por qué es importante la participación de actores sociales?",
    "¿Qué rol tiene la gobernanza en la implementación de GIs?",
    "¿Qué obstáculos sociales dificultan las GIs en países en desarrollo?",
    "¿Qué se entiende por co-creación de infraestructuras verdes?",
    "¿Qué son los indicadores OPP (openness of participatory processes)?",
    "¿Qué es el análisis de costo-beneficio (CBA)?",
    "¿Qué es el análisis de costo-efectividad (CEA)?",
    "¿Qué representa el valor presente neto (VPN) en una evaluación?",
    "¿Por qué es importante considerar el costo del ciclo de vida?",
    "¿Qué barreras económicas existen para implementar GIs?",
    "¿Cómo se mide la concentración de oxígeno disuelto?",
    "¿Qué valores límites se recomiendan para nitritos y fosfatos?",
    "¿Qué indica el 'coeficiente de escorrentía'?",
    "¿Cómo se cuantifica el confort térmico?",
    "¿Qué variables se monitorean en mantenimiento de GIs?",
    "¿Qué ejemplos de implementación de GIs en América Latina se presentan?",
    "¿Qué resultados se observaron en Nanjing con distintas GIs?",
    "¿Qué indicadores se usaron en el caso de Quito, Ecuador?",
    "¿Qué se concluyó en el estudio de Michigan sobre techos verdes?",
    "¿Cuáles fueron los beneficios en Barcelona con techos verdes y bioceldas?",
    "¿Qué limitaciones existen en la implementación de GIs en zonas montañosas?",
    "¿Por qué se considera necesario evaluar la efectividad de GIs?",
    "¿Qué rol juega la planificación urbana en el éxito de GIs?",
    "¿Cuál es el papel de las políticas públicas en GIs?",
    "¿Por qué es importante monitorear durante toda la vida útil del GI?",
    "¿Cuáles son los 12 criterios definidos en la metodología del estudio?",
    "¿Qué criterio está relacionado con el manejo de aguas pluviales?",
    "¿Qué criterio incluye la justicia social y cohesión?",
    "¿Qué criterio se relaciona con la regeneración urbana?",
    "¿Qué tipo de indicadores deben usarse antes, durante y después de la implementación?"
]

# Opciones de respuestas predefinidas
options = [
    "Es una infraestructura que emplea elementos naturales como vegetación, suelos y agua",
    "Busca mitigar impactos de cambio climático, urbanización rápida, crecimiento poblacional",
    "Son los beneficios que las personas obtienen de los ecosistemas",
    "Son enfoques inspirados y respaldados por la naturaleza",
    "La infraestructura gris es rígida y menos sostenible, mientras que la infraestructura verde usa soluciones naturales",
    "Aumenta las superficies impermeables, lo que incrementa la escorrentía superficial",
    "Aumenta la frecuencia e intensidad de eventos extremos como inundaciones y sequías",
    "Es un fenómeno donde las áreas urbanas presentan temperaturas significativamente más altas",
    "Mejora del microclima, aire y agua, aumento de biodiversidad",
    "Promueven la infiltración, retención y absorción del agua",
    "Control del volumen de inundación, retención e infiltración del agua",
    "Techos verdes, pavimentos permeables, jardines de lluvia, humedales, zanjas de infiltración",
    "Es la combinación de infraestructuras tradicionales (gris) y soluciones naturales (verde)",
    "Jardines de lluvia, zanjas de infiltración, pavimentos permeables, franjas filtrantes",
    "Reducen el volumen de escorrentía, mejoran la calidad del agua, regulan la temperatura urbana",
    "Es una herramienta que simula el comportamiento del agua en cuencas o sistemas urbanos",
    "Datos temporales (lluvia, caudal, evaporación), espaciales (uso de suelo, red de alcantarillado)",
    "Tiempo al pico, volumen de escorrentía, eficiencia de infiltración",
    "Es el tiempo que transcurre desde el inicio de un evento de lluvia hasta que se alcanza el caudal máximo",
    "Es el porcentaje del volumen total de agua que se logra infiltrar al suelo",
    "Porque su inclusión mejora la aceptación social, sostenibilidad y efectividad de las GIs",
    "La gobernanza proporciona políticas, normas y guías técnicas necesarias para planificar e implementar GIs",
    "Existen barreras culturales, financieras, institucionales y políticas",
    "Es un proceso participativo donde ciudadanos, técnicos, académicos y autoridades colaboran en el diseño de GIs",
    "Son métricas que miden el nivel de participación ciudadana en el proceso de planificación",
    "Es una herramienta económica que compara los beneficios totales con los costos de implementación de GIs",
    "Evalúa qué opción ofrece el mayor efecto deseado por unidad de costo",
    "Es el valor actual de los beneficios menos los costos a lo largo del tiempo",
    "Permite evaluar no solo la inversión inicial, sino también los costos de operación y mantenimiento",
    "Falta de financiamiento, prioridades en obras tradicionales y escasa inversión pública",
    "Porque indica la calidad del agua, esencial para evaluar el estado ecológico",
    "Se recomienda ≤0.2 mg/L de PO₄³⁻ para aguas salmonídeas y ≤0.4 mg/L para ciprínidas",
    "Es un parámetro que representa la fracción de precipitación que se convierte en escorrentía",
    "A través de la temperatura equivalente fisiológica (PET) y la reducción del efecto de isla de calor",
    "Nivel de agua, tasa de flujo, sólidos suspendidos, nitrógeno total",
    "Aún existen barreras como políticas deficientes, escaso conocimiento y falta de mantenimiento",
    "Zanjas verdes fueron las más rentables individualmente, y la combinación de cisternas con pavimentos fue la más efectiva",
    "El municipio ha incluido normativas para la planificación con infraestructura azul-verde en Quito",
    "Zanjas verdes, barriles de lluvia y estanques secos fueron los más costo-efectivos",
    "Se alcanzó una reducción del 56% en daños por inundaciones gracias a techos verdes y bioceldas",
    "Mayor riesgo de deslizamientos, falta de planificación urbana en zonas montañosas",
    "Porque permite entender su desempeño real y justificar su implementación ante tomadores de decisiones",
    "La planificación urbana estratégica debe integrar soluciones naturales como GIs",
    "Las políticas proporcionan el marco legal, normativo y técnico necesario para planificar e implementar GIs",
    "Permite recopilar datos para mejorar decisiones futuras y evaluar desempeño",
    "Gestión de drenaje urbano, urbanización, cambio climático, regeneración urbana, entre otros"
]

# Función para crear la app en Streamlit
def app():
    st.title("Cuestionario sobre Infraestructura Verde (GI) - Selección")

    respuestas_usuario = []

    for i, question in enumerate(questions):
        st.subheader(question)
        respuesta = st.selectbox(f"Selecciona tu respuesta para la pregunta {i+1}", options)
        respuestas_usuario.append(respuesta)
    
    if st.button("Ver respuestas correctas"):
        st.subheader("Respuestas Correctas")
        for i, correct_answer in enumerate(options):
            st.write(f"Pregunta {i+1}: {correct_answer}")

if __name__ == "__main__":
    app()
