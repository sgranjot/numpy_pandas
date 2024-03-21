import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('elecciones_generales_2023.csv')

df_pp = df[df['PARTIDO'] == 'PP']
pp_por_distrito = df_pp.groupby('DISTRITO')['NUM_VOTOS'].sum()

df_psoe = df[df['PARTIDO'] == 'PSOE']
psoe_por_distrito = df_psoe.groupby('DISTRITO')['NUM_VOTOS'].sum()

df_vox = df[df['PARTIDO'] == 'VOX']
vox_por_distrito = df_vox.groupby('DISTRITO')['NUM_VOTOS'].sum()

plt.figure(figsize=(14, 5))

plt.subplot(131)
plt.title('Partido Popular')
plt.xlabel('Distrito')
plt.ylabel('Votos')
pp_por_distrito.plot(kind='bar', color='blue')
#plt.bar(pp_por_distrito['DISTRITO'], pp_por_distrito['NUM_VOTOS'], color='blue')

plt.subplot(132)
plt.title('PSOE')
plt.xlabel('Distrito')
plt.ylabel('Votos')
psoe_por_distrito.plot(kind='bar', color='red')
#plt.bar(psoe_por_distrito['DISTRITO'], psoe_por_distrito['NUM_VOTOS'], color='red')

plt.subplot(133)
plt.title('VOX')
plt.xlabel('Distrito')
plt.ylabel('Votos')
vox_por_distrito.plot(kind='bar', color='green')
#plt.bar(vox_por_distrito['DISTRITO'], vox_por_distrito['NUM_VOTOS'], color='green')

plt.suptitle('Principales partidos por distritos')
plt.show()
