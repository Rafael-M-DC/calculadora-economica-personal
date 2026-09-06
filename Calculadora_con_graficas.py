# Calculadora Económica Personal con Gráficas
# Agosto 2026 - Rafael Medina

import matplotlib.pyplot as plt

print("=== CALCULADORA ECONÓMICA PERSONAL ===")

# Plazo de tiempo
while True:
    try:
        periodo_años = int(input("\nIndique el plazo de tiempo en años (Ejemplo: 5): "))
        if periodo_años > 0:
            break
        print("Error: el plazo debe ser mayor que 0.")
    except ValueError:
        print("Error: debes ingresar un número")

# Tasa de interés anual
while True:
    try:
        tasa_interes_anual = float(input("\nIndique la tasa de interes anual(Ejemplo: 4%): ").replace("%", ""))/100
        if tasa_interes_anual >= 0:
            break
        print("Error: la tasa de interés no puede ser negativa.")
    except ValueError:
        print("Error: debes ingresar un número")

tasa_interes_mensual = (1 + tasa_interes_anual) ** (1/12) - 1
meses = 12 * periodo_años

# Inflación anual
while True:
    try:
        inflacion_anual = float(input("\nIndique la inflación anual promedio(Ejemplo: 2%): ").replace("%", ""))/100
        if inflacion_anual >= 0:
            break
        print("Error: la inflación no puede ser negativa.")
    except ValueError:
        print("Error: debes ingresar un número")

# Rendimiento real
rendimiento_real_acumulado = ((((1+tasa_interes_anual)/(1+inflacion_anual))**periodo_años)-1)*100

# Tipo de cambio
while True:
    try:
        tipo_de_cambio_a_dolares = float(input("Ingrese el tipo de cambio actual (USD a PEN): "))
        if tipo_de_cambio_a_dolares > 0:
            break
        print("Error: el tipo de cambio debe ser mayor a 0")
    except ValueError:
        print("Error: debes ingresar un número")

def moneda_salario():
    while True:
        try:
            salario_moneda = int(input(f"""\n
Elija el tipo de moneda para ingresar su salario
    1) Soles
    2) Dolares
Coloque solo el número deseado: """))
            if salario_moneda in (1, 2):
                return salario_moneda
            print(f"\nError! Selección inválida")
        except ValueError:
            print("Error: Selección invalida. Elige 1 o 2")

def moneda_resultados():
    while True:
        try:
            resultados_moneda = int(input(f"""\n
Elija el tipo de moneda para los resultados
    1) Soles
    2) Dolares
Coloque solo el número deseado: """))
            if resultados_moneda in (1, 2):
                return resultados_moneda
            print(f"\nError! Selección inválida")
        except ValueError:
            print("Error: Selección invalida. Elige 1 o 2")

def calculo_ahorro(salario_mensual, gastos_mensuales, meses, tasa_mensual):
    ahorro_mensual = salario_mensual - gastos_mensuales
    tasa_ahorro = (ahorro_mensual / salario_mensual) * 100

    saldo = 0
    saldo_por_mes = [0]  # Guardamos el saldo cada mes para la gráfica
    
    for mes in range(meses):
        saldo = saldo * (1 + tasa_mensual) + ahorro_mensual
        saldo_por_mes.append(saldo)

    return ahorro_mensual, tasa_ahorro, saldo, saldo_por_mes

def muestra_datos(salario_moneda, resultados_moneda):
    if salario_moneda == 1:
        simbolo = "S/"
    else:
        simbolo = "$"
        
    while True:
        try:
            salario_mensual = float(input(f"¿Cuál es tu salario mensual? {simbolo}"))
            if salario_mensual > 0:
                break
            print("Error: el salario debe ser mayor que 0.")
        except ValueError:
            print("Error: debes ingresar una cantidad válida.")
            
    while True:
        try:
            gastos_mensuales = float(input(f"¿Cuáles son tus gastos mensuales? {simbolo}"))
            if gastos_mensuales >= 0:
                break
            print("Error: los gastos no pueden ser negativos.")
        except ValueError:
            print("Error: debes ingresar una cantidad válida.")
                
    if salario_moneda == 1 and resultados_moneda == 2:
        salario_mensual /= tipo_de_cambio_a_dolares
        gastos_mensuales /= tipo_de_cambio_a_dolares
    elif salario_moneda == 2 and resultados_moneda == 1:
        salario_mensual *= tipo_de_cambio_a_dolares
        gastos_mensuales *= tipo_de_cambio_a_dolares

    return salario_mensual, gastos_mensuales, resultados_moneda

def resultados_calculadora(resultados_moneda, salario_mensual, gastos_mensuales, ahorro_mensual, 
                          tasa_ahorro, saldo_proyectado, periodo_años, inflacion_anual, 
                          tasa_interes_anual, rendimiento_real):
    if resultados_moneda == 1:
        simbolo = "S/"
    else:
        simbolo = "$"
    
    print(f"\n=== RESULTADOS ===")
    print(f"Salario mensual: {simbolo}{salario_mensual:,.2f}")
    print(f"Gastos mensuales: {simbolo}{gastos_mensuales:,.2f}")
    
    if ahorro_mensual == 0:
        print(f"No hubo ahorro ni déficit")
    else:
        if ahorro_mensual > 0:
            cambio, varia = "Ahorro", "ahorrarás"            
        else:
            cambio, varia = "Déficit", "tu déficit acumulado será"   
        
        print(f"{cambio} mensual: {simbolo}{abs(ahorro_mensual):,.2f}")
        print(f"Tasa de ahorro: {tasa_ahorro:,.2f}%")
        print(f"En {periodo_años} años, {varia}: {simbolo}{abs(saldo_proyectado):,.2f}")
        print(f"Promedio anual: {simbolo}{abs(saldo_proyectado)/periodo_años:,.2f}")

    print(f"\nNota: Con {inflacion_anual*100}% inflación anual y")
    print(f"con {tasa_interes_anual*100:,.1f}% de interés anual en tus ahorros,")
    print(f"el rendimiento real acumulado de tu dinero será ~{rendimiento_real:,.2f}%")

def generar_graficas(saldo_por_mes, periodo_años, ahorro_mensual, resultados_moneda):
    """Genera gráficas de la proyección de ahorros"""
    
    if resultados_moneda == 1:
        simbolo = "S/"
    else:
        simbolo = "$"
    
    meses = len(saldo_por_mes) - 1
    meses_lista = [i/12 for i in range(len(saldo_por_mes))]  # Convertir a años
    
    # Crear figura con 2 gráficas
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gráfica 1: Proyección de ahorros
    ax1.plot(meses_lista, saldo_por_mes, linewidth=2, color='#2E86AB', marker='o', markersize=3)
    ax1.fill_between(meses_lista, saldo_por_mes, alpha=0.3, color='#2E86AB')
    ax1.set_xlabel('Tiempo (años)', fontsize=11)
    ax1.set_ylabel(f'Saldo ({simbolo})', fontsize=11)
    ax1.set_title('Proyección de Ahorros', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K' if x >= 1000 else f'{x:.0f}'))
    
    # Gráfica 2: Ahorros anuales
    ahorros_anuales = []
    for año in range(periodo_años + 1):
        mes_inicio = año * 12
        mes_fin = (año + 1) * 12
        if mes_fin <= len(saldo_por_mes) - 1:
            ahorro_año = saldo_por_mes[mes_fin] - saldo_por_mes[mes_inicio]
            ahorros_anuales.append(ahorro_año)
    
    años = range(1, len(ahorros_anuales) + 1)
    ax2.bar(años, ahorros_anuales, color='#A23B72', alpha=0.8, edgecolor='black')
    ax2.set_xlabel('Año', fontsize=11)
    ax2.set_ylabel(f'Ahorro anual ({simbolo})', fontsize=11)
    ax2.set_title('Ahorro por Año', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K' if x >= 1000 else f'{x:.0f}'))
    
    plt.tight_layout()
    plt.savefig('proyeccion_ahorros.png', dpi=300, bbox_inches='tight')
    print(f"\n✅ Gráfica guardada como 'proyeccion_ahorros.png'")
    plt.show()

# Programa principal
salario_mensual, gastos_mensuales, resultados_moneda = muestra_datos(moneda_salario(), moneda_resultados())

ahorro_mensual, tasa_ahorro, saldo_proyectado, saldo_por_mes = calculo_ahorro(
    salario_mensual, gastos_mensuales, meses, tasa_interes_mensual
)

resultados_calculadora(resultados_moneda, salario_mensual, gastos_mensuales, ahorro_mensual,
                       tasa_ahorro, saldo_proyectado, periodo_años, inflacion_anual, 
                       tasa_interes_anual, rendimiento_real_acumulado)

# Generar gráficas
generar_graficas(saldo_por_mes, periodo_años, ahorro_mensual, resultados_moneda)