import pandas as pd
import funzioni as fn


# Carica il file Excel considerando la prima riga come header delle colonne
df = pd.read_excel( r"NewFile.xlsx")

# Stampa i nomi delle colonne
print(df.columns)

# Filtra le righe in cui la colonna "Entrata" è vuota
righe_entrata_vuota = df[df['Entrata'].isna()]

df = pd.read_excel( r"NewFile.xlsx")

# Stampa i nomi delle colonne
print(df.columns)

# Filtra le righe in cui la colonna "Entrata" è vuota
righe_entrata_vuota2 = df[df['Entrata'].isna()]




# Salva i risultati in un nuovo file Excel
#righe_entrata_vuota.to_excel('pagamenti_def_30-04.xlsx', index=False)

#print("Risultati salvati in 'pagamenti_def_30-04.xlsx'")
merge_cf=fn.merge_dati_cf(righe_entrata_vuota)
merge_pi=fn.merge_dati_pi(righe_entrata_vuota2)
fn.merge_and_save_results(merge_cf,merge_pi)
print('programma concluso')