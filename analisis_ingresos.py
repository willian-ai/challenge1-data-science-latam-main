import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lista de archivos de las tiendas
archivos_tiendas = [
    'base-de-datos-challenge1-latam/tienda_1 .csv',
    'base-de-datos-challenge1-latam/tienda_2.csv',
    'base-de-datos-challenge1-latam/tienda_3.csv',
    'base-de-datos-challenge1-latam/tienda_4.csv'
]

# Diccionario para almacenar los ingresos por tienda
ingresos_por_tienda = {}
frecuencia_ventas = {}

# Analizar cada tienda
for i, archivo in enumerate(archivos_tiendas, 1):
    # Leer el archivo CSV
    df = pd.read_csv(archivo)
    
    # Calcular el ingreso total
    ingreso_total = df['Precio'].sum()
    
    # Calcular la frecuencia de ventas por categoría
    frec_categorias = df['Categoría del Producto'].value_counts()
    
    # Almacenar los resultados
    ingresos_por_tienda[f'Tienda {i}'] = ingreso_total
    frecuencia_ventas[f'Tienda {i}'] = frec_categorias

# Crear un DataFrame con los resultados
resultados = pd.DataFrame({
    'Tienda': list(ingresos_por_tienda.keys()),
    'Ingreso Total': list(ingresos_por_tienda.values())
})

# Calcular estadísticas descriptivas
media_ingresos = resultados['Ingreso Total'].mean()
desviacion_std = resultados['Ingreso Total'].std()
tienda_max = resultados.loc[resultados['Ingreso Total'].idxmax(), 'Tienda']
tienda_min = resultados.loc[resultados['Ingreso Total'].idxmin(), 'Tienda']

# Crear una figura con múltiples subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Comparación de Ventas Totales por Tienda', fontsize=16)

# 1. Gráfico de Torta (Pie Chart)
axes[0, 0].pie(resultados['Ingreso Total'], 
               labels=resultados['Tienda'],
               autopct='%1.1f%%',
               startangle=90,
               shadow=True,
               explode=(0.1, 0, 0, 0))
axes[0, 0].set_title('Distribución Porcentual de Ventas')

# 2. Gráfico de Líneas con Puntos
axes[0, 1].plot(resultados['Tienda'], 
                resultados['Ingreso Total'],
                marker='o',
                linestyle='-',
                linewidth=2,
                markersize=8)
axes[0, 1].set_title('Tendencia de Ventas')
axes[0, 1].grid(True, linestyle='--', alpha=0.7)
for i, v in enumerate(resultados['Ingreso Total']):
    axes[0, 1].text(i, v, f'{v:,.0f}', ha='center', va='bottom')

# 3. Gráfico de Área
axes[1, 0].fill_between(resultados['Tienda'],
                        resultados['Ingreso Total'],
                        color='skyblue',
                        alpha=0.4)
axes[1, 0].plot(resultados['Tienda'],
                resultados['Ingreso Total'],
                color='Slateblue',
                alpha=0.6,
                linewidth=2)
axes[1, 0].set_title('Distribución de Ventas (Área)')
axes[1, 0].grid(True, linestyle='--', alpha=0.7)

# 4. Gráfico de Dispersión con Tamaño
sizes = (resultados['Ingreso Total'] / resultados['Ingreso Total'].max()) * 1000
axes[1, 1].scatter(resultados['Tienda'],
                   resultados['Ingreso Total'],
                   s=sizes,
                   alpha=0.6,
                   c='green')
axes[1, 1].set_title('Comparación de Ventas (Tamaño)')
axes[1, 1].grid(True, linestyle='--', alpha=0.7)
for i, v in enumerate(resultados['Ingreso Total']):
    axes[1, 1].text(i, v, f'{v:,.0f}', ha='center', va='bottom')

# Ajustar el layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Guardar el gráfico
plt.savefig('comparacion_ventas.png', dpi=300, bbox_inches='tight')
plt.close()

# Imprimir el análisis
print("\n=== ANÁLISIS DE VENTAS POR TIENDA ===")
print("\n1. Ventas Totales:")
print(resultados)
print("\n2. Estadísticas Descriptivas:")
print(f"Media de ventas: {media_ingresos:,.2f} COP")
print(f"Desviación estándar: {desviacion_std:,.2f} COP")
print(f"Tienda con mayores ventas: {tienda_max}")
print(f"Tienda con menores ventas: {tienda_min}")

print("\n3. Frecuencia de Ventas por Categoría:")
for tienda, frecuencias in frecuencia_ventas.items():
    print(f"\n{tienda}:")
    print(frecuencias)

print("\nLos resultados han sido guardados en 'resultados_ingresos.csv'")
print("Las visualizaciones han sido guardadas como 'comparacion_ventas.png'") 