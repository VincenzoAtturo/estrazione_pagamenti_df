import pandas as pd
from datetime import datetime



def first_if_equal(series):
    if series.nunique() == 1:
        return series.iloc[0]  
    else:
        return ', '.join(series.dropna().astype(str))  
    
    
def merge_dati_cf(df):
    colonne_da_trasformare = ['Intestatario', 'Rata',  'Data allibramento']  
    for colonna in colonne_da_trasformare:
        df[colonna] = df.groupby(['Codice Fiscale'])[colonna].transform(first_if_equal)
    merge_df = df.groupby(['Codice Fiscale'], as_index=False).agg({ 
        'Intestatario':'first',
        'Rata':'first', 
        'Data allibramento':'first',
        'Importo': 'sum'})  
    return merge_df

    
def merge_dati_pi(df):
    colonne_da_trasformare = ['Intestatario', 'Rata',  'Data allibramento']  
    for colonna in colonne_da_trasformare:
        df[colonna] = df.groupby(['Partita Iva'])[colonna].transform(first_if_equal)
    merge_df = df.groupby(['Partita Iva'], as_index=True).agg({ 
        'Intestatario':'first',
        'Rata':'first', 
        'Data allibramento':'first',
        'Importo': 'sum'})  
   
    return merge_df
 

def merge_and_save_results(df_cf, df_pi):
    # Unisce i risultati per codice fiscale e partita IVA
    merged_df = pd.concat([df_cf, df_pi], ignore_index=True)
    
    # Ordina il DataFrame in base alla colonna 'Intestatario' in ordine alfabetico
    merged_df = merged_df.sort_values(by='Intestatario')
    
    # Ottieni la data corrente nel formato desiderato
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Genera il nome del file con la data corrente
    output_file = "pagamenti_def_{}.xlsx".format(current_date)
    
    # Salva i risultati in un nuovo file Excel
    merged_df.to_excel(output_file, index=False)
    print("Risultati salvati in '{}'".format(output_file))
