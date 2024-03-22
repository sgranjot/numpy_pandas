import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('suicidios_canarias_residentes_sexo_edad_año.csv')

# SUICIDIOS DE HOMBRES Y MUJERES POR AÑOS TODAS LAS EDADES
df_hombres = df[df['SEXO_CODE'] == 'M']
df_hombres_todas_edades = df_hombres[df_hombres['GRUPO_EDAD_CODE'] == '_T']
hombres_por_año = df_hombres_todas_edades.groupby('TIME_PERIOD_CODE')['OBS_VALUE'].sum()

df_mujeres = df[df['SEXO_CODE'] == 'F']
df_mujeres_todas_edades = df_mujeres[df_mujeres['GRUPO_EDAD_CODE'] == '_T']
mujeres_por_año = df_mujeres_todas_edades.groupby('TIME_PERIOD_CODE')['OBS_VALUE'].sum()

#SUICIDIOS DE HOMBRES Y MUJERES POR AÑOS ENTRE 40 Y 60 AÑOS
df_hombres_55_59 = df_hombres[df_hombres['GRUPO_EDAD_CODE'] == 'Y55T59']
df_hombres_50_54 = df_hombres[df_hombres['GRUPO_EDAD_CODE'] == 'Y50T54']
df_hombres_45_49 = df_hombres[df_hombres['GRUPO_EDAD_CODE'] == 'Y45T49']
df_hombres_40_44 = df_hombres[df_hombres['GRUPO_EDAD_CODE'] == 'Y40T44']
df_hombres_40_60 = pd.concat([df_hombres_55_59, df_hombres_50_54, df_hombres_45_49, df_hombres_40_44], ignore_index=True)
hombres_40_60_por_año = df_hombres_40_60.groupby('TIME_PERIOD_CODE')['OBS_VALUE'].sum()

df_mujeres_55_59 = df_mujeres[df_mujeres['GRUPO_EDAD_CODE'] == 'Y55T59']
df_mujeres_50_54 = df_mujeres[df_mujeres['GRUPO_EDAD_CODE'] == 'Y50T54']
df_mujeres_45_49 = df_mujeres[df_mujeres['GRUPO_EDAD_CODE'] == 'Y45T49']
df_mujeres_40_44 = df_mujeres[df_mujeres['GRUPO_EDAD_CODE'] == 'Y40T44']
df_mujeres_40_60 = pd.concat([df_mujeres_55_59, df_mujeres_50_54, df_mujeres_45_49, df_mujeres_40_44], ignore_index=True)
mujeres_40_60_por_año = df_mujeres_40_60.groupby('TIME_PERIOD_CODE')['OBS_VALUE'].sum()

# Crear la gráfica
plt.figure(figsize=(15, 5))

plt.subplot(121)
plt.title('Suicidios en Canarias por año y sexo en todas las edades')
plt.xlabel('Año')
plt.ylabel('Suicidios')
hombres_por_año.plot(color='c', label='Hombres')
mujeres_por_año.plot(color='m', label='Mujeres')
plt.legend()

plt.subplot(122)
plt.title('Suicidios en Canarias por año y sexo entre los 40 y 60 años de edad')
plt.xlabel('Año')
plt.ylabel('Suicidios')
hombres_40_60_por_año.plot(color='c', label='Hombres')
mujeres_40_60_por_año.plot(color='m', label='Mujeres')
plt.legend()

plt.show()



