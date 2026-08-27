import pandas as pd

def calcolo_peso_navi():
  print("Calcolo del peso totale delle navi:")
  print("Dati calcoli peso totale delle navi caricate correttamente.")

  df = pd.read_csv('navi.csv')

  df['peso_singolo_tonnellate'] = df['peso_singolo_tonnellate'].fillna

  df.to_csv('calcoli_navi.csv', index=False)
  print(df)

calcolo_peso_navi() 
