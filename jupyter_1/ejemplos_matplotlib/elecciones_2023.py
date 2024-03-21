import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('elecciones_generales_2023.csv')

plt.figure(figsize=(14, 5))

plt.subplot(131)
plt.title('Partido Popular')
plt.xlabel('Distrito')
plt.ylabel('Votos')
df_PP = df['PARTIDO'] == 'PP'
#df_PP_agrupado = df_PP.groupby('DISTRITO')['NUM_VOTOS'].sum().reset_index()
plt.bar(df_PP['DISTRITO'], df_PP['NUM_VOTOS'], color='blue')

plt.subplot(132)
plt.title('PSOE')
plt.xlabel('Distrito')
plt.ylabel('Votos')
df_PSOE = df['PARTIDO'] == 'PSOE'
#df_PSOE_agrupado = df_PSOE.groupby('DISTRITO')['NUM_VOTOS'].sum().reset_index()
plt.bar(df_PSOE['DISTRITO'], df_PSOE['NUM_VOTOS'], color='red')

plt.subplot(133)
plt.title('VOX')
plt.xlabel('Distrito')
plt.ylabel('Votos')
df_VOX = df['PARTIDO'] == 'PP'
#df_VOX_agrupado = df_VOX.groupby('DISTRITO')['NUM_VOTOS'].sum().reset_index()
plt.bar(df_VOX['DISTRITO'], df_VOX['NUM_VOTOS'], color='green')

plt.suptitle('Principales partidos por distritos')
plt.show()
