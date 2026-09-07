# Calculadora Económica Personal 💰

Una herramienta interactiva para proyectar tus ahorros considerando inflación e intereses, diseñada para contexto económico peruano.

## 🎯 Características

- ✅ Proyección de ahorros a n años con tasa de interés
- ✅ Cálculo de rendimiento real (ajustado por inflación)
- ✅ Conversión automática PEN/USD
- ✅ Análisis de tasa de ahorro mensual
- ✅ Validación de entrada para evitar errores

## 🚀 Uso

### Requisitos
- Python 

### Ejecución

```bash
python Calculadora Economica Personal 1.0.py
```

El programa te pedirá:
1. Plazo de tiempo (en años)
2. Tasa de interés anual (%)
3. Inflación promedio anual (%)
4. Tipo de cambio actual (USD a PEN)
5. Moneda para ingresar datos (Soles o Dólares)
6. Salario mensual
7. Gastos mensuales

## 📊 Resultados

El programa calcula:
- Ahorro mensual y tasa de ahorro (%)
- Saldo proyectado después de n años
- Promedio anual de ahorros
- Rendimiento real acumulado (descontando inflación)

## 📈 Próximas mejoras

- [ ] Gráficas de proyección con matplotlib
- [ ] Interfaz gráfica con tkinter

**Fecha**: Agosto 2026  

---

## 📊 Versión con Gráficas

Ahora hay una versión mejorada que genera gráficas automáticas:

```bash
python Calculadora_con_graficas.py
```

### Características de la versión con gráficas

- 📈 **Gráfica de Proyección**: Visualiza cómo crecen tus ahorros en el tiempo
- 📊 **Gráfica de Ahorros Anuales**: Compara cuánto ahorras cada año
- 💾 **Exportación**: Las gráficas se guardan como `proyeccion_ahorros.png`

### Instalación de matplotlib

```bash
pip install matplotlib
```

### Ejemplo de salida

El programa genera dos gráficas:
1. Línea de tendencia con área sombreada (proyección total)
2. Gráfica de barras (ahorros por año)

## 📈 Próximas mejoras

✅ Gráficas de proyección con matplotlib
- [ ] Interfaz gráfica con tkinter
- [ ] Exportar a CSV

**Fecha**: Septiembre 2026  

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de hacer fork del proyecto.

## 📝 Licencia

Este proyecto es de código abierto bajo licencia MIT.

---

**Autor**: Rafael Medina