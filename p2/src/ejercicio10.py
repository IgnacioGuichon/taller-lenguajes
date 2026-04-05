# Entrega (Práctica 2, Ejercicio 10)
# ------------------------------------------

# Datos de entrada: rondas de la competencia
rounds = [
    {
        "theme": "Entrada",
        "scores": {
            "Valentina": {"judge_1": 8, "judge_2": 7, "judge_3": 9},
            "Mateo": {"judge_1": 7, "judge_2": 8, "judge_3": 7},
            "Camila": {"judge_1": 9, "judge_2": 9, "judge_3": 8},
            "Santiago": {"judge_1": 6, "judge_2": 7, "judge_3": 6},
            "Lucía": {"judge_1": 8, "judge_2": 8, "judge_3": 8},
        },
    },
    {
        "theme": "Plato principal",
        "scores": {
            "Valentina": {"judge_1": 9, "judge_2": 9, "judge_3": 8},
            "Mateo": {"judge_1": 8, "judge_2": 7, "judge_3": 9},
            "Camila": {"judge_1": 7, "judge_2": 6, "judge_3": 7},
            "Santiago": {"judge_1": 9, "judge_2": 8, "judge_3": 8},
            "Lucía": {"judge_1": 7, "judge_2": 8, "judge_3": 7},
        },
    },
    {
        "theme": "Postre",
        "scores": {
            "Valentina": {"judge_1": 7, "judge_2": 8, "judge_3": 7},
            "Mateo": {"judge_1": 9, "judge_2": 9, "judge_3": 8},
            "Camila": {"judge_1": 8, "judge_2": 7, "judge_3": 9},
            "Santiago": {"judge_1": 7, "judge_2": 7, "judge_3": 6},
            "Lucía": {"judge_1": 9, "judge_2": 9, "judge_3": 9},
        },
    },
    {
        "theme": "Cocina internacional",
        "scores": {
            "Valentina": {"judge_1": 8, "judge_2": 9, "judge_3": 9},
            "Mateo": {"judge_1": 7, "judge_2": 6, "judge_3": 7},
            "Camila": {"judge_1": 9, "judge_2": 8, "judge_3": 8},
            "Santiago": {"judge_1": 8, "judge_2": 9, "judge_3": 7},
            "Lucía": {"judge_1": 7, "judge_2": 7, "judge_3": 8},
        },
    },
    {
        "theme": "Final libre",
        "scores": {
            "Valentina": {"judge_1": 9, "judge_2": 8, "judge_3": 9},
            "Mateo": {"judge_1": 8, "judge_2": 9, "judge_3": 8},
            "Camila": {"judge_1": 7, "judge_2": 7, "judge_3": 7},
            "Santiago": {"judge_1": 9, "judge_2": 9, "judge_3": 9},
            "Lucía": {"judge_1": 8, "judge_2": 8, "judge_3": 7},
        },
    },
]

# ------------------------------------------
# Flujo de programa a grandes rasgos (pseudocódigo):

# 1. Poner en cero los valores de cada competidor (puntaje total, rondas ganadas, mejor ronda y puntaje por ronda).
# 2. Recorrer ronda: sumar la puntuación de cada competidor (guardarlo para luego calcular promedio) y encontrar mejor puntaje de ronda.
# 3. Imprimir el ganador de la ronda (contabilizarlo en rondas ganadas) + tabla de posiciones progresiva luego de esa ronda (acumulado).
# 4. Al finalizar las 5 rondas, imprimir tabla general en orden decreciente por puntaje total.
# ------------------------------------------

def calcular_puntajes_ronda(scores):
    puntajes = {}
    for competidor, jueces in scores.items():
        puntaje_total = sum(jueces.values())
        puntajes[competidor] = puntaje_total
    
    return puntajes

def inicializar_estadisticas(rounds):
    """
    Inicializa las estadísticas acumuladas para cada participante.
    Devuelve un diccionario con la estructura base.
    """
    estadisticas = {}

    for round in rounds:
        for participante in round["scores"]:
            if participante not in estadisticas:
                estadisticas[participante] = {
                    "total": 0,
                    "rondas_ganadas": 0,
                    "mejor_ronda": 0,
                    "puntaje_por_ronda": []
                }

    return estadisticas

def procesar_ronda(round, estadisticas):
    """
    Procesa una ronda completa:
    - calcula puntajes
    - actualiza estadísticas acumuladas
    - determina el ganador de la ronda

    Devuelve:
    - ganador (str)
    - puntaje del ganador (int)
    - puntajes de la ronda (dict)
    """
    scores = round["scores"]

    # 1. Calcular puntajes de la ronda
    puntajes_ronda = calcular_puntajes_ronda(scores)

    # 2. Actualizar estadísticas acumuladas
    for competidor, puntaje in puntajes_ronda.items():
        estadisticas[competidor]["total"] += puntaje
        estadisticas[competidor]["puntaje_por_ronda"].append(puntaje)

        if puntaje > estadisticas[competidor]["mejor_ronda"]:
            estadisticas[competidor]["mejor_ronda"] = puntaje

    # 3. Determinar ganador de la ronda
    ganador = max(puntajes_ronda, key=puntajes_ronda.get)
    puntaje_ganador = puntajes_ronda[ganador]

    # 4. Sumar ronda ganada
    estadisticas[ganador]["rondas_ganadas"] += 1

    return ganador, puntaje_ganador, puntajes_ronda

# Muestra tabla de posiciones sin acumular puntajes de rondas pasadas.
# No se invoca en el flujo principal porque se pide mostrar la PROGRESIÓN. (me dí cuenta tarde)
def mostrar_tabla_ronda(puntajes_ronda):
    """
    Muestra la tabla de posiciones de una ronda,
    ordenada por puntaje descendente.
    """
    print("Tabla de posiciones:")

    # Ordenar por puntaje de mayor a menor
    ordenados = sorted(
        puntajes_ronda.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for competidor, puntaje in ordenados:
        print(f"{competidor}: {puntaje} pts")

# Muestra tabla de posiciones acumulada hasta la ronda actual, ordenada por puntaje total.
# Se invoca porque muestra PROGRESIÓN como pide la consigna.
def mostrar_tabla_progresiva(estadisticas):
    """
    Muestra la tabla de posiciones con puntajes acumulados
    hasta la ronda actual, ordenada por puntaje total.
    """
    print("Tabla de posiciones (acumulada):")

    # Construir diccionario {participante: total}
    acumulados = {
        competidor: datos["total"]
        for competidor, datos in estadisticas.items()
    }

    # Ordenar por puntaje total descendente
    ordenados = sorted(
        acumulados.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for competidor, total in ordenados:
        print(f"{competidor}: {total} pts")

def calcular_resultados_finales(estadisticas):
    """
    A partir de las estadísticas acumuladas, calcula los resultados finales.
    Devuelve una lista de diccionarios con los datos por participante.
    """
    resultados = []

    for competidor, datos in estadisticas.items():
        rondas_jugadas = len(datos["puntaje_por_ronda"])
        promedio = (
            sum(datos["puntaje_por_ronda"]) / rondas_jugadas
            if rondas_jugadas > 0
            else 0
        )

        resultados.append({
            "nombre": competidor,
            "total": datos["total"],
            "rondas_ganadas": datos["rondas_ganadas"],
            "mejor_ronda": datos["mejor_ronda"],
            "promedio": promedio
        })

    # Ordenar por puntaje total descendente
    resultados.sort(key=lambda r: r["total"], reverse=True)

    return resultados


def mostrar_tabla_final(resultados):
    """
    Muestra la tabla final de posiciones.
    """
    print("\nTabla de posiciones final:")
    print(
        "Cocinero".ljust(15),
        "Puntaje".ljust(10),
        "Rondas ganadas".ljust(15),
        "Mejor ronda".ljust(12),
        "Promedio"
    )
    print("-" * 65)

    for r in resultados:
        print(
            r["nombre"].ljust(15),
            str(r["total"]).ljust(10),
            str(r["rondas_ganadas"]).ljust(15),
            str(r["mejor_ronda"]).ljust(12),
            f"{r['promedio']:.1f}"
        )


if __name__ == "__main__":
    pass