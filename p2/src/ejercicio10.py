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

if __name__ == "__main__":
    estadisticas = inicializar_estadisticas(rounds)
    ronda = rounds[0]
    ganador, puntaje_ganador, puntajes = procesar_ronda(ronda, estadisticas)
    print(f"Ronda: {ronda['theme']}")
    print(f"Ganador: {ganador} ({puntaje_ganador} pts)")
    print("Puntajes de la ronda:", puntajes)
    print()
    print("Estadísticas acumuladas:")
    for participante, datos in estadisticas.items():
        print(participante, datos)